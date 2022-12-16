from pydantic import BaseModel
from typing import List

class GenerateObject(BaseModel):
    expiry: int
    length: int
    medium: str
    message: str
    number: str
    sender_id: str
    type: str

    class Config():
        orm_mode = True

class Response(BaseModel):
    message: str
    code: str

    class Config():
        orm_mode = True

class SMSResponse(BaseModel):
    recipient: str
    id: str

    class Config():
        orm_mode = True

class SendSMS(BaseModel):
    status: str
    data: List[SMSResponse]

    class Config():
        orm_mode = True

