from fastapi import FastAPI, HTTPException,Query
from typing import List
from app.arkeselOTPHelper import generateOTP, verifyOTP, sendSMS
from app.schema import Response, SendSMS

app = FastAPI(
    title = "OTP with Arkesel API"
)

@app.get("/")
async def hello_world():
    return {"message": "Hello World"}


@app.post("/v1/otp/generate/{phone_number}", response_model= Response)
async def generate_OTP(phone_number):
    if len(phone_number) < 12:
       raise HTTPException(status_code=418, detail="Phone Number less than 12 eg. 233249643365")
    else:
        return generateOTP(phone_number)


@app.post("/v1/otp/verify/{phone_number}", response_model= Response)
async def verify_OTP(code: str, phone_number):
    if len(code) < 6:
        raise HTTPException(status_code=418, detail="code must be 6 numeric figure")
    elif len(phone_number) < 12:
         raise HTTPException(status_code=418, detail="Phone Number less than 12 eg. 233249643365")
    else:
        return verifyOTP(code,phone_number)

@app.post("/v1/message/send", response_model = SendSMS)
async def send_SMS(message: str, phone_numbers: List[str] = Query(...)):
    if len(phone_numbers) < 0:
        raise HTTPException(status_code=418, detail="Enter at least a Phone Number")
    elif len(message) < 0:
         raise HTTPException(status_code=418, detail="Message cannot be empty")
    else:
        return sendSMS(message,phone_numbers)