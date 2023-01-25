from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from app.arkeselOTPHelper import generateOTP, verifyOTP, sendSMS
from app.schema import Response, SendSMS, RespondSMS, RequestOTP, VerifyOTP

app = FastAPI(
    title = "OTP with Arkesel API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def hello_world():
    return {"message": "Hello World"}


@app.post("/v1/otp/generate", response_model= Response)
async def generate_OTP(request: RequestOTP):
    if len(request.phone_number) < 12:
       raise HTTPException(status_code=418, detail="Phone Number less than 12 eg. 233249643365")
    else:
        return generateOTP(request.sender, request.phone_number)


@app.post("/v1/otp/verify", response_model= Response)
async def verify_OTP(request: VerifyOTP):
    if len(request.code) < 6:
        raise HTTPException(status_code=418, detail="code must be 6 numeric figure")
    elif len(request.phone_number) < 12:
         raise HTTPException(status_code=418, detail="Phone Number less than 12 eg. 233249643365")
    else:
        return verifyOTP(request.sender, request.code,request.phone_number)

@app.post("/v1/message/send", response_model = RespondSMS)
async def send_SMS(request:SendSMS):
    if len(request.phone_numbers) < 0:
        raise HTTPException(status_code=418, detail="Enter at least a Phone Number")
    elif len(request.message) < 0:
         raise HTTPException(status_code=418, detail="Message cannot be empty")
    else:
        return sendSMS(request.sender, request.message, request.phone_numbers)