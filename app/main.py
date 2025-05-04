import uvicorn

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

# from auth.route import auth
# from chat.route import chat
# from sql.route import sql
# from routes.textToSQL import sql

from core.config import getConfig

config=getConfig()

origins = [
            config.get('FE_URL'),
            config.get('BE_URL'),
            "http://localhost:8888",
            "http://localhost:8090",
            "http://localhost:5173",
        ]

description = """
RAG 기술을 이용해 사실에 근거한 대답을 하는 챗봇입니다.

기존 질문을 DB에 저장해 대답합니다.

DB에 존재하지 않는 데이터에 대해서는 사실과 다른 대답을 할 수 있습니다.
"""

tags_metadata = [
    {
        "name": "Auth",
        "description": "로그인/로그아웃 인증 관련 표준 API",
    },
    {
        "name": "Chat",
        "description": "챗봇기능",
        # "externalDocs": {
        #     "description": "Items external docs",
        #     "url": "https://fastapi.tiangolo.com/",
        # },
    },
]

app = FastAPI(
    swagger_ui_parameters={"tryItOutEnabled": True},
    openapi_tags=tags_metadata,
    title="TYS-ChatbotApp",
    description=description,
    summary="LLM을 이용한 챗봇 서비스 입니다.",
    version="0.0.1",
    # terms_of_service="http://example.com/terms/",
    # contact={
    #     "name": "TONGYANG SYSTEMS",
    #     "url": "http://x-force.example.com/contact/",
    #     "email": "dp@x-force.example.com",
    # },
    # license_info={
    #     "name": "Apache 2.0",
    #     "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    # },
    )
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(auth)
# app.include_router(chat)
# app.include_router(sql)

if __name__ == "__main__":
    uvicorn.run("main:app",
                host="localhost",
                port= 8090,
                reload = True,
                # workers = 8,
                )
