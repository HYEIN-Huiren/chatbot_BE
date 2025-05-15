# chatbot_BE

 Python
환경변수 설정
구분
SW
버전
비고
IDE
 Python
패키지매니저
Framework
 ORM
개발환경
형상관리
redis   
VSCode
 Python11
 pip
 FastAPI
 sqlalchemy
 VSCodeUserSetup-x64-1.80.1 
11.x 
최신 
최신 
2.0 
pipenv
 git
파이썬 설치 경로 환경변수 추가
최신pi
 Git-2.41.0.3-64-bit 
고급시스템설정 > 환경변수 추가 > Path > 새로만들기  설치경로 주소입력
ex) 
C:\Users\TY\AppData\Local\Programs\Python\Python311\Scripts
아래 내용은 가상환경을 설정할 폴더(코드 위치)로 이동한 후 진행합니다.
가상환경 생성
pipenv --python 11 
가상환경 활성화
pipenv shell
 p install pipenv
파이썬 버전으로 인한 호환 문제가 생길 시 Pipfile 파일 제일 아래의 하위 버전 내용을 삭제합니다.
 1 # Pipfile
 2
 3 [requires]
 4 python_version = "3.11"
 5 # python_full_version = "3.11.4" # 주석처리
정상적으로 접속 성공시 커맨드 창에서 
(가상환경명) 주소>로 표시 됩니다. 
가상환경 내에서 필요 패키지 설치를 진행합니다.
 pip install -r requirements.txt
아래 명령어를 이용해 fastapi 서버를 실행합니다.
 uvicorn app.main:app --host 호스트 --port PORT
 5
가상환경 종료 
exit
 FastAPI
 SQLAlchemy
 DataBase
구분
pipenv
 SW
버전
Postgresql
비고
최신
DBeaver
 23.2.3 
CREATE EXTENSION vector
