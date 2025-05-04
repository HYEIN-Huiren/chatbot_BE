import os
from dotenv import dotenv_values

from langchain_google_vertexai import ChatVertexAI
from langchain_google_vertexai.embeddings import VertexAIEmbeddings
from langchain_community.vectorstores.pgvector import PGVector
from google.oauth2 import service_account

def settings(mode: str = "local"):
    path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    config = dotenv_values(f"{path}/app/env/.env.{mode}")
    config['GOOGLE_APPLICATION_CREDENTIALS'] = f"{path}/{config.get('GOOGLE_APPLICATION_CREDENTIALS')}"

    config['ALGORITHM'] = ""
    config['SECRET_KEY'] = ""

    return config

def getConfig():
    config = {}
    if os.getenv("MODE") == 'dev':
        config = settings('dev')
    else:
        config = settings()
    return config


def getRetriever():
    config = getConfig()
    embeddings = getEmbeddingModel()
    vector_store = PGVector.from_existing_index(embeddings, connection_string=config.get('DBR_URL'))
    retriever = vector_store.as_retriever(
    search_type="similarity_score_threshold",
        search_kwargs={
            "score_threshold": 0.6,
            "k": 4
        })
    return retriever

def getEmbeddingModel():
    config = getConfig()
    credentials = service_account.Credentials.from_service_account_file(config.get('GOOGLE_APPLICATION_CREDENTIALS'))
    embeddings = VertexAIEmbeddings(credentials = credentials, project=config.get('PROJECT_ID'), location=config.get('PROJECT_RESION'))
    return embeddings

def getChatModel():
    config = getConfig()
    credentials = service_account.Credentials.from_service_account_file(config.get('GOOGLE_APPLICATION_CREDENTIALS'))
    chat = ChatVertexAI(temprature = 0,
                    credentials = credentials,
                        # model_name = 'gemini-pro',
                    max_output_tokens=2048,
                    verbose = True,
                    project=config.get('PROJECT_ID'),
                    location=config.get('PROJECT_RESION')
                    )
    return chat
