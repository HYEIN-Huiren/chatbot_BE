from pydantic import BaseModel

class ChatRequest(BaseModel):
    projectCode: str = 'TY-01'
    userId: str | None = None

class InsertChatRequest(ChatRequest):
    question: str

class Request(BaseModel):
    uuid: str

class AnswerRequest(Request):
    userId: str
    answer: str