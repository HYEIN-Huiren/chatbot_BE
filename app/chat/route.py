from core.config import getConfig, getEmbeddingModel, getRetriever

from core.bearer import JWTBearer
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from db.connection import get_db
from chat.repo import getProjectCode
from chat.models.dto import ChatRequest, Request, AnswerRequest, InsertChatRequest
from chat.models.entity import Chat
from sql.impl import translate_text, parseSQL, getChain, getChatChain

from uuid import uuid4 as uuid

config=getConfig()

chat = APIRouter(
    prefix="/chat", # url 앞에 고정적으로 붙는 경로추가
    tags=['Chat'],
    dependencies=[Depends(JWTBearer())],
)

embeddings = getEmbeddingModel()
chain, sqlChain = getChain()
chatChain = getChatChain()

@chat.post("/")
async def answer(request: InsertChatRequest, db: Session = Depends(get_db)):
    """
    대답의 방식은 db/sql/chat 3가지가 있다.
    질문의 언어에 따라 답변한다 (영어, 한글)
    1. 우선 chat을 제외한 다른 방식의 대답 중 질문한 내용과 유사한 질문이 존재하는지 확인하여
    존재하는 경우 해당 질문의 답변을 return 한다.
    2. 질문과 관련된 사전에 정보가 등록된 Table이 존재하는지 확인 후
    존재하는 경우 sql 쿼리를 작성하여 가져온 데이터에 기반한 답변을 return 한다.
    쿼리 실행 중 문제가 발생하는 경우 에러메시지를 return 한다.
    3. 마지막으로 생성한 답변을 return 하며 동시에 정보가 정확하지 않을 수 있음을 명시한다. 
    """

    # API KEY와 대조 project 가져오는 것으로 수정 필요
    project = getProjectCode(db, request.projectCode)
    if project:
        if request.question.encode().isalpha():
            question = request.question
        else:
            question = translate_text(request.question)

        embededQuestion = embeddings.embed_query(question)
        # 유클리드 거리 기준 답 (제일 유사한 답)현재  0.7 < n < 0.75
        result = db.scalar(select(Chat)
                           .filter(Chat.projectCode == request.projectCode)
                           .filter(Chat.answerType != 'chat')
                           .where(Chat.embedding.l2_distance(embededQuestion) 
                                  < 0.74))
        if not result:#hasattr(result, 'answer'):
            retriever = getRetriever()

            if retriever.invoke(question): # 쿼리 상태 체크 필요
                try:
                    sql = sqlChain.invoke({'input': question})
                    answer = chain.invoke({'input': question})
                    if not request.question.encode().isalpha():
                        answer=translate_text(answer, sorce_language='en',target_language='ko')
                    data = Chat(
                        uuid=uuid(),
                        projectCode = request.projectCode,
                        userId = request.userId,
                        question = request.question,
                        active = True,
                        sql = parseSQL(sql),
                        answerType = 'sql',
                        answer = answer,
                        embedding = embededQuestion
                    )
                    db.add(data)
                    db.commit()
                    return {
                        "message": None,
                        "data": {"question": request.question,
                                    "sql": parseSQL(sql),
                                    "answer":answer
                                    },
                        "pageInfo": None,
                        "isSuccess": True
                    }
                except:
                    answer = '질문이 명확하지 않아서 정확히 답변해 드릴 수 없어요. 조금 더 명확하게 질문해 주시겠어요?'
                    if request.question.encode().isalpha():
                        answer=translate_text(answer)
                    return {
                        "message": None,
                        "data":{"question": request.question,
                                    "answer":answer
                                    },
                        "pageInfo": None,
                        "isSuccess": False
                    }
            else:
                answer = chatChain.invoke(request.question)
                data = Chat(
                                uuid=uuid(),
                                projectCode = request.projectCode,
                                userId = request.userId,
                                question = request.question,
                                active = True,
                                sql = None,
                                answerType = 'chat',
                                answer = answer,
                                embedding = embededQuestion)
                db.add(data)
                db.commit()
                warning = '/n *이 답변은 정확하지 않을 수 있습니다.*'
                if request.question.encode().isalpha():
                    warning = translate_text(warning)
                return {
                            "message": None,
                            "data":{"question": request.question,
                                        "answer":answer + warning,
                            },
                            "pageInfo": None,
                            "isSuccess": True
                        }
        
        else:
            answer = result.answer
            return {
                        "message": None,
                        "data":{"question": request.question,
                                    "answer":answer,
                        },
                        "pageInfo": None,
                        "isSuccess": True
                    }
    else:
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail = "No such project",
                headers={"WWW-Authenticate": "Bearer"}
        )

@chat.put("/disable")
async def disableChat(request: Request, db: Session = Depends(get_db)):
    db.query(Chat).filter(Chat.uuid == request.uuid).update({'active': False})
    db.commit()
    return {
        "message": None,
        "data": None,
        "pageInfo": None,
        "isSuccess": True
    }

@chat.put("/update")
async def updateAnswer(request: AnswerRequest, db: Session = Depends(get_db)):
    db.query(Chat).filter(Chat.uuid ==request.uuid).update({'answer': request.answer, 'answerType': 'db'})
    db.commit()
    return {
        "message": None,
        "data": None,
        "pageInfo": None,
        "isSuccess": True
    }

@chat.get('/list/')
async def typeList(projectCode, type = None, db: Session = Depends(get_db)):
    query = db.query(Chat.uuid, Chat.question, Chat.answer, Chat.active).filter(Chat.projectCode == projectCode)
    if type:
        query = query.filter(Chat.answerType == type)
    results = query.all()
    response = list()
    for uuid, question, answer, active in results:
        dic = {'uuid': uuid, 'question':question, 'answer': answer, 'active': active}
        response.append(dic)
    return {
        "message": None,
        "data":
        {
            "list":response,
            "count": len(response),
        },
        "pageInfo": None,
        "isSuccess": True
    }

@chat.post('/list')
async def userChatList(request: ChatRequest, db: Session = Depends(get_db)):
    results = db.query(Chat.uuid, Chat.question, Chat.answer).filter(Chat.projectCode == request.projectCode).filter(Chat.userId == request.userId).filter(Chat.active == True).all()
    response = list()
    for uuid, question, answer in results:
        dic = {'uuid': uuid, 'question':question, 'answer': answer}
        response.append(dic)
    return { 
        "message": None,
        "data": {
            "list": response,
        },
        "pageInfo": None,
        "isSuccess": True
    }

@chat.get("/{uuid}")
async def prevChat(uuid: str, db: Session = Depends(get_db)):
    result = db.query(Chat.question, Chat.answer).filter(Chat.uuid == uuid).first()
    data = {'uuid': uuid, 'question': result[0], 'answer': result[1]}
    print(result)
    return { 
        "message": None,
        "data": data,
        "pageInfo": None,
        "isSuccess": True
    }