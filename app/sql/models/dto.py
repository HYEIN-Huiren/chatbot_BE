from pydantic import BaseModel

class Test(BaseModel):
    question: str = "How many users we have?"
    language: str = "en"