# chatbot_BE
## Python Server 환경구성
|구분|SW|버전|비고|
|---|---|---|---|
|IDE|VSCode|VSCodeUserSetup-x64-1.80.1 |
|Python|Python11|11.x|
|패키지매니저|pip|최신|
|Framework|FastAPI|최신|
|ORM|sqlalchemy|2.0|
|개발환경|pipenv|최신|
|형상관리|gitlab|Git-2.41.0.3-64-bit|
|redis|||

### 환경변수 설정

파이썬 설치 경로 환경변수 추가
`고급시스템설정 > 환경변수 추가 > Path > 새로만들기  설치경로 주소입력`
ex) `C:\Users\TY\AppData\Local\Programs\Python\Python311\Scripts`

아래 내용은 가상환경을 설정할 폴더(코드 위치)로 이동한 후 진행합니다.
가상환경 생성
`pipenv --python 11`
가상환경 활성화
`pipenv shell`
파이썬 버전으로 인한 호환 문제가 생길 시 Pipfile 파일 제일 아래의 하위 버전 내용을 삭제합니다.
 ```
# Pipfile

 [requires]
 python_version = "3.11"
 # python_full_version = "3.11.4" # 주석처리
```

정상적으로 접속 성공시 커맨드 창에서 
`(가상환경명) 주소>`로 표시 됩니다. 
가상환경 내에서 필요 패키지 설치를 진행합니다.
 `pip install -r requirements.txt`
아래 명령어를 이용해 fastapi 서버를 실행합니다.
 `uvicorn app.main:app --host 호스트 --port PORT`

가상환경 종료 
`exit`


### DataBase
|구분|SW|버전|비고|
|---|---|---|---|
||Postgresql|최신|`creae extension vector;`|
||DBeaver|23.2.3||

## API 설계
|요구사항|중요도|비고|
|---|---|---|
|각 사용자는 서비스에 질문을 보내며 하나의 질문 당 하나의 대답을 리
턴한다.|높음|단건 조회/추가|
|대답은 비슷한 질문에 대한 답을 DB에서 불러오거나 LLM이 생성한다.|높음|단건 조회/추가|
|모든 질문과 대답은 저장된다.||단건 추가|
|각 사용자는 자신이 한 이전 질문을 확인하고 비활성화 할 수 있다.||단건 수정|
|관리자는 담당 프로젝트의 전체 질문과 대답을 확인할 수 있지만 각 질
문을 한 사용자는 식별할 수 없다||다건 조회|
|관리자는 전체 질문의 갯수와 그 비중 그리고 자주 사용되는 질문을 확
인할 수 있다||다건 조회|
|관리자는 사용자의 질문으로 생성된 대답을 올바르게 수정할 수 있다||단건 수정|
