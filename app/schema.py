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
   sender: str
   message: str
   phone_numbers: List[str]
   class Config():
        orm_mode = True

class RespondSMS(BaseModel):
    status: str
    data: List[SMSResponse]

    class Config():
        orm_mode = True


class RequestOTP(BaseModel):
    sender: str
    phone_number: str

    class Config():
        orm_mode = True

class VerifyOTP(BaseModel):
    sender: str
    phone_number: str
    code: str

    class Config():
        orm_mode = True



