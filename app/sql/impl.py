from google.cloud import translate_v3
from core.config import getConfig, getRetriever, getChatModel
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_community.utilities.sql_database import SQLDatabase

from sql.prompt_templates.prompt_templates import TEMPLATE_SQL, TEMPLATE_ANSWER

config = getConfig()

def parseSQL(_:str):
        import re
        p = re.compile('\s+')
        sql = re.sub(p, ' ', _)
        p = re.compile(r'```sql(.*)```', re.DOTALL)
        result = p.findall(sql)

        return result[0]

def translate_text(text: str, sorce_language: str = 'ko', target_language: str = 'en', project_id: str = config.get('PROJECT_ID')):

    client = translate_v3.TranslationServiceClient()
    location = "global"
    parent = f"projects/{project_id}/locations/{location}"
    response = client.translate_text(
    request={
            "parent": parent,
            "contents": [text],
            "mime_type": "text/plain",
            "source_language_code": sorce_language,
            "target_language_code": target_language,
        }
    )
    return response.translations[0].translated_text

def get_schema(_:dict):
    retriever = getRetriever()
    response = retriever.invoke(_.get('input'))
    schema=""
    for i in range(len(response)):
        schema += response[i].to_json()['kwargs']['page_content']
    return schema

def getChain():
    config = getConfig()
    db = SQLDatabase.from_uri(config.get('DBR_URL'))
    chat = getChatModel()
    prompt_sql = ChatPromptTemplate.from_template(TEMPLATE_SQL)
    prompt_response = ChatPromptTemplate.from_template(TEMPLATE_ANSWER)
    sql_response = (
        RunnablePassthrough.assign(context=get_schema)
            | prompt_sql
            | chat.bind(stop=["\nSQLResult:"])
            | StrOutputParser()
    )

    chain = (
        RunnablePassthrough.assign(query=sql_response).assign(
                response=lambda x: db.run(parseSQL(x["query"])))
            | prompt_response
            | chat
            | StrOutputParser()
        )
    
    return chain, sql_response

def getChatChain():
    chat = getChatModel()
    chatChain = chat | StrOutputParser()
    return chatChain