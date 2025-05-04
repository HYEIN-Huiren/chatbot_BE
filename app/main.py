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

@app.get("/carClasses")
async def root():
    return  [
    {
      "carClassId": 1,
      "carClassName": "더뉴아반떼",
      "carModel": "준중형",
      "image": "https://image.socar.kr/car_image/car086_detail1.png",
      "drivingDistance": 5000,
      "year": 2021,
      "price": 225123,
      "discountPercent": 25,
      "regionGroups": ["서울/경기/인천", "광주"],
      "carTypeTags": ["특가", "인기"]
    },
    {
      "carClassId": 2,
      "carClassName": "올뉴아반떼",
      "carModel": "준중형",
      "image": "https://image.socar.kr/car_image/car144_detail1.png",
      "drivingDistance": 15000,
      "year": 2021,
      "price": 325448,
      "discountPercent": 37,
      "regionGroups": ["광주", "대전"],
      "carTypeTags": ["빠른대여", "인기"]
    },
    {
      "carClassId": 3,
      "carClassName": "아반떼AD",
      "carModel": "준중형",
      "image": "https://image.socar.kr/car_image/car022_detail1.png",
      "drivingDistance": 100000,
      "year": 2017,
      "price": 245852,
      "discountPercent": 20,
      "regionGroups": ["서울/경기/인천"],
      "carTypeTags": ["인기"]
    },
    {
      "carClassId": 4,
      "carClassName": "스포티지",
      "carModel": "SUV",
      "image": "https://image.socar.kr/car_image/car024_detail1.png",
      "drivingDistance": 100000,
      "year": 2017,
      "price": 343142,
      "discountPercent": 15,
      "regionGroups": ["서울/경기/인천"],
      "carTypeTags": ["특가", "인기"]
    },
    {
      "carClassId": 5,
      "carClassName": "K5",
      "carModel": "중형/대형",
      "image": "https://image.socar.kr/car_image/car047_detail1.png",
      "drivingDistance": 100000,
      "year": 2017,
      "price": 316000,
      "discountPercent": 0,
      "regionGroups": ["서울/경기/인천"],
      "carTypeTags": ["인기"]
    },
    {
      "carClassId": 6,
      "carClassName": "K5 (LPG)",
      "carModel": "중형/대형",
      "image": "https://image.socar.kr/car_image/car030_detail1.png",
      "drivingDistance": 100000,
      "year": 2017,
      "price": 342000,
      "discountPercent": 10,
      "regionGroups": ["서울/경기/인천"],
      "carTypeTags": []
    },
    {
      "carClassId": 7,
      "carClassName": "카니발 11인승",
      "carModel": "SUV",
      "image": "https://image.socar.kr/car_image/car034_detail1.png",
      "drivingDistance": 50000,
      "year": 2017,
      "price": 324000,
      "discountPercent": 14,
      "regionGroups": ["서울/경기/인천"],
      "carTypeTags": []
    },
    {
      "carClassId": 8,
      "carClassName": "코나",
      "carModel": "경형/소형",
      "image": "https://image.socar.kr/car_image/car060_detail1.png",
      "drivingDistance": 50000,
      "year": 2019,
      "price": 215000,
      "discountPercent": 30,
      "regionGroups": ["서울/경기/인천", "대구/경북"],
      "carTypeTags": ["특가"]
    },
    {
      "carClassId": 9,
      "carClassName": "더뉴레이",
      "carModel": "경형/소형",
      "image": "https://image.socar.kr/car_image/car064_detail1.png",
      "drivingDistance": 10000,
      "year": 2021,
      "price": 198000,
      "discountPercent": 15,
      "regionGroups": ["서울/경기/인천", "대전"],
      "carTypeTags": ["인기"]
    },
    {
      "carClassId": 10,
      "carClassName": "싼타페",
      "carModel": "SUV",
      "image": "https://image.socar.kr/car_image/car072_detail1.png",
      "drivingDistance": 100000,
      "year": 2019,
      "price": 387000,
      "discountPercent": 17,
      "regionGroups": ["서울/경기/인천"],
      "carTypeTags": ["빠른대여", "인기"]
    },
    {
      "carClassId": 11,
      "carClassName": "셀토스",
      "carModel": "SUV",
      "image": "https://image.socar.kr/car_image/car136_detail1.png",
      "drivingDistance": 10000,
      "year": 2021,
      "price": 375000,
      "discountPercent": 28,
      "regionGroups": ["광주", "서울/경기/인천"],
      "carTypeTags": ["빠른대여", "인기"]
    },
    {
      "carClassId": 12,
      "carClassName": "더뉴K3",
      "carModel": "준중형",
      "image": "https://image.socar.kr/car_image/car174_detail1.png",
      "drivingDistance": 24000,
      "year": 2021,
      "price": 366000,
      "discountPercent": 26,
      "regionGroups": ["광주"],
      "carTypeTags": ["인기"]
    },
    {
      "carClassId": 13,
      "carClassName": "2021 쏘나타DN8",
      "carModel": "중형/대형",
      "image": "https://image.socar.kr/car_image/car188_detail1.png",
      "drivingDistance": 500,
      "year": 2021,
      "price": 389000,
      "discountPercent": 8,
      "regionGroups": ["서울/경기/인천"],
      "carTypeTags": ["신차급"]
    },
    {
      "carClassId": 14,
      "carClassName": "투싼(경유)",
      "carModel": "SUV",
      "image": "https://image.socar.kr/car_image/car050_detail1.png",
      "drivingDistance": 100000,
      "year": 2017,
      "price": 376000,
      "discountPercent": 0,
      "regionGroups": ["서울/경기/인천"],
      "carTypeTags": ["특가"]
    },
    {
      "carClassId": 15,
      "carClassName": "쏘나타 뉴라이즈(LPG)",
      "carModel": "중형/대형",
      "image": "https://image.socar.kr/car_image/car061_detail1.png",
      "drivingDistance": 51000,
      "year": 2019,
      "price": 346000,
      "discountPercent": 12,
      "regionGroups": ["서울/경기/인천"],
      "carTypeTags": []
    },
    {
      "carClassId": 16,
      "carClassName": "G80",
      "carModel": "중형/대형",
      "image": "https://image.socar.kr/car_image/car068_detail1.png",
      "drivingDistance": 50000,
      "year": 2019,
      "price": 567000,
      "discountPercent": 25,
      "regionGroups": ["서울/경기/인천"],
      "carTypeTags": ["프리미엄"]
    },
    {
      "carClassId": 17,
      "carClassName": "쏘나타 뉴라이즈",
      "carModel": "중형/대형",
      "image": "https://image.socar.kr/car_image/car077_detail1.png",
      "drivingDistance": 126000,
      "year": 2019,
      "price": 287000,
      "discountPercent": 25,
      "regionGroups": ["서울/경기/인천"],
      "carTypeTags": []
    },
    {
      "carClassId": 18,
      "carClassName": "벤츠 A220",
      "carModel": "수입",
      "image": "https://image.socar.kr/car_image/car122_detail1.png",
      "drivingDistance": 10000,
      "year": 2019,
      "price": 578000,
      "discountPercent": 27,
      "regionGroups": ["서울/경기/인천"],
      "carTypeTags": ["프리미엄"]
    },
    {
      "carClassId": 19,
      "carClassName": "카니발 프레스티지 9인승",
      "carModel": "SUV",
      "image": "https://image.socar.kr/car_image/car034_detail1.png",
      "drivingDistance": 50000,
      "year": 2019,
      "price": 354000,
      "discountPercent": 25,
      "regionGroups": ["부산/창원"],
      "carTypeTags": ["특가"]
    },
    {
      "carClassId": 20,
      "carClassName": "더뉴아반떼",
      "carModel": "준중형",
      "image": "https://image.socar.kr/car_image/car086_detail1.png",
      "drivingDistance": 5000,
      "year": 2021,
      "price": 225123,
      "discountPercent": 25,
      "regionGroups": ["서울/경기/인천", "광주"],
      "carTypeTags": ["특가", "인기"]
    },
    {
      "carClassId": 21,
      "carClassName": "올뉴아반떼",
      "carModel": "준중형",
      "image": "https://image.socar.kr/car_image/car144_detail1.png",
      "drivingDistance": 44300,
      "year": 2021,
      "price": 325448,
      "discountPercent": 37,
      "regionGroups": ["광주", "대전"],
      "carTypeTags": ["빠른대여", "인기"]
    },
    {
      "carClassId": 22,
      "carClassName": "아반떼AD",
      "carModel": "준중형",
      "image": "https://image.socar.kr/car_image/car022_detail1.png",
      "drivingDistance": 100000,
      "year": 2017,
      "price": 245852,
      "discountPercent": 20,
      "regionGroups": ["서울/경기/인천"],
      "carTypeTags": ["인기"]
    },
    {
      "carClassId": 23,
      "carClassName": "스포티지",
      "carModel": "SUV",
      "image": "https://image.socar.kr/car_image/car024_detail1.png",
      "drivingDistance": 100000,
      "year": 2017,
      "price": 343142,
      "discountPercent": 15,
      "regionGroups": ["서울/경기/인천"],
      "carTypeTags": ["특가", "인기"]
    },
    {
      "carClassId": 24,
      "carClassName": "K5",
      "carModel": "중형/대형",
      "image": "https://image.socar.kr/car_image/car047_detail1.png",
      "drivingDistance": 100000,
      "year": 2017,
      "price": 316000,
      "discountPercent": 0,
      "regionGroups": ["서울/경기/인천"],
      "carTypeTags": ["인기"]
    },
    {
      "carClassId": 25,
      "carClassName": "K5 (LPG)",
      "carModel": "중형/대형",
      "image": "https://image.socar.kr/car_image/car030_detail1.png",
      "drivingDistance": 100000,
      "year": 2017,
      "price": 342000,
      "discountPercent": 10,
      "regionGroups": ["서울/경기/인천"],
      "carTypeTags": []
    },
    {
      "carClassId": 26,
      "carClassName": "카니발 11인승",
      "carModel": "SUV",
      "image": "https://image.socar.kr/car_image/car034_detail1.png",
      "drivingDistance": 50000,
      "year": 2017,
      "price": 324000,
      "discountPercent": 14,
      "regionGroups": ["서울/경기/인천"],
      "carTypeTags": []
    },
    {
      "carClassId": 27,
      "carClassName": "코나",
      "carModel": "경형/소형",
      "image": "https://image.socar.kr/car_image/car060_detail1.png",
      "drivingDistance": 50000,
      "year": 2019,
      "price": 215000,
      "discountPercent": 30,
      "regionGroups": ["서울/경기/인천", "대구/경북"],
      "carTypeTags": ["특가"]
    },
    {
      "carClassId": 28,
      "carClassName": "더뉴레이",
      "carModel": "경형/소형",
      "image": "https://image.socar.kr/car_image/car064_detail1.png",
      "drivingDistance": 10000,
      "year": 2021,
      "price": 198000,
      "discountPercent": 15,
      "regionGroups": ["서울/경기/인천", "대전"],
      "carTypeTags": ["인기"]
    },
    {
      "carClassId": 29,
      "carClassName": "싼타페",
      "carModel": "SUV",
      "image": "https://image.socar.kr/car_image/car072_detail1.png",
      "drivingDistance": 100000,
      "year": 2019,
      "price": 387000,
      "discountPercent": 17,
      "regionGroups": ["서울/경기/인천"],
      "carTypeTags": ["빠른대여", "인기"]
    },
    {
      "carClassId": 30,
      "carClassName": "셀토스",
      "carModel": "SUV",
      "image": "https://image.socar.kr/car_image/car136_detail1.png",
      "drivingDistance": 10000,
      "year": 2021,
      "price": 375000,
      "discountPercent": 28,
      "regionGroups": ["광주", "서울/경기/인천"],
      "carTypeTags": ["빠른대여", "인기"]
    },
    {
      "carClassId": 31,
      "carClassName": "더뉴K3",
      "carModel": "준중형",
      "image": "https://image.socar.kr/car_image/car174_detail1.png",
      "drivingDistance": 10000,
      "year": 2021,
      "price": 366000,
      "discountPercent": 26,
      "regionGroups": ["광주"],
      "carTypeTags": ["인기"]
    },
    {
      "carClassId": 32,
      "carClassName": "2021 쏘나타DN8",
      "carModel": "중형/대형",
      "image": "https://image.socar.kr/car_image/car188_detail1.png",
      "drivingDistance": 500,
      "year": 2021,
      "price": 389000,
      "discountPercent": 8,
      "regionGroups": ["서울/경기/인천"],
      "carTypeTags": ["신차급"]
    },
    {
      "carClassId": 33,
      "carClassName": "투싼(경유)",
      "carModel": "SUV",
      "image": "https://image.socar.kr/car_image/car050_detail1.png",
      "drivingDistance": 100000,
      "year": 2017,
      "price": 376000,
      "discountPercent": 0,
      "regionGroups": ["서울/경기/인천"],
      "carTypeTags": ["특가"]
    },
    {
      "carClassId": 34,
      "carClassName": "쏘나타 뉴라이즈(LPG)",
      "carModel": "중형/대형",
      "image": "https://image.socar.kr/car_image/car061_detail1.png",
      "drivingDistance": 50000,
      "year": 2019,
      "price": 346000,
      "discountPercent": 12,
      "regionGroups": ["서울/경기/인천"],
      "carTypeTags": []
    },
    {
      "carClassId": 35,
      "carClassName": "G80",
      "carModel": "중형/대형",
      "image": "https://image.socar.kr/car_image/car068_detail1.png",
      "drivingDistance": 50000,
      "year": 2019,
      "price": 567000,
      "discountPercent": 25,
      "regionGroups": ["서울/경기/인천"],
      "carTypeTags": ["프리미엄"]
    },
    {
      "carClassId": 36,
      "carClassName": "쏘나타 뉴라이즈",
      "carModel": "중형/대형",
      "image": "https://image.socar.kr/car_image/car077_detail1.png",
      "drivingDistance": 100000,
      "year": 2019,
      "price": 287000,
      "discountPercent": 25,
      "regionGroups": ["서울/경기/인천"],
      "carTypeTags": []
    },
    {
      "carClassId": 37,
      "carClassName": "벤츠 A220",
      "carModel": "수입",
      "image": "https://image.socar.kr/car_image/car122_detail1.png",
      "drivingDistance": 10000,
      "year": 2019,
      "price": 578000,
      "discountPercent": 27,
      "regionGroups": ["서울/경기/인천"],
      "carTypeTags": ["프리미엄"]
    },
    {
      "carClassId": 38,
      "carClassName": "카니발 프레스티지 9인승",
      "carModel": "SUV",
      "image": "https://image.socar.kr/car_image/car034_detail1.png",
      "drivingDistance": 50000,
      "year": 2019,
      "price": 354000,
      "discountPercent": 25,
      "regionGroups": ["부산/창원"],
      "carTypeTags": ["특가"]
    }
  ]

if __name__ == "__main__":
    uvicorn.run("main:app",
                host="localhost",
                port= 8090,
                reload = True,
                # workers = 8,
                )