from fastapi import APIRouter, Depends, HTTPException, status

from core.config import getConfig, getChatModel, getRetriever
from core.bearer import JWTBearer

from db.connection import get_db
from langchain_core.output_parsers import StrOutputParser

from sql.impl import translate_text, parseSQL, getChain

from sql.models.dto import Test
from sqlalchemy.orm import Session

sql = APIRouter(
    prefix="/sql",
    tags=['SQL'],
    dependencies=[Depends(JWTBearer())],
)

config=getConfig()
chat = getChatModel()

@sql.post("/")
async def sqlAnswer(request:Test, db: Session = Depends(get_db)):

    question = request.question
    try:
        if not request.question.encode().isalpha():
            question = translate_text(question)
        retriever = getRetriever()
        if retriever.invoke(question):
            chain, sqlChain = getChain()
            answer = chain.invoke({'input':question})
            sql = parseSQL(sqlChain.invoke({'input':question}))
            if not request.question.encode().isalpha():
                answer=translate_text(answer, sorce_language='en',target_language='ko')
            return {
                    "message": {"question": request.question,
                                "sql": sql,
                                "answer":answer
                                },
                    "isSuccess": True,}
        else: 
            chatChain = chat | StrOutputParser()
            answer = chatChain.invoke(request.question)
            # answer = 'Can not find any relative target table from database.'
            return{
                "message": {"question":request.question,
                            "answer": answer},
                "isSuccess": True,
            }
    except:
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail = None,
                headers={"WWW-Authenticate": "Bearer"}
        )