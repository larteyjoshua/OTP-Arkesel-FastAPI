import requests
from app.schema import GenerateObject
from app.config import settings
import json



def generateOTP(phone_number: str):

    message: str = 'This is a test OTP from Arkesel API {}otp_code{}'.format('%','%')

    data = GenerateObject(
        expiry = settings.EXPIRY_TIME,
        length =settings.OTP_LENGTH,
         medium = settings.MEDIUM,
         message = message,
         number = phone_number,
         sender_id = settings.SENDER_ID,
         type = settings.TYPE 
    )

    headers = {
        'api-key': settings.API_KEY,
        "Content-Type": "application/json"
    } 

    params = json.dumps(data.__dict__)
    print('data', params)
    generateResponse = requests.post(
    url = settings.OTP_GENERATE_URL, 
    data =params,
    headers = headers)

    print('generate response', generateResponse)
    return generateResponse.json()


def verifyOTP(code:str, phone_number: str):

        data = {
            "api_key": settings.API_KEY,
            "code": code,
            "number": phone_number
        }

        headers = {
        'api-key':settings.API_KEY,
        "Content-Type": "application/json"
        } 
        params = json.dumps(data)
        print('data', params)
        verifyResponse = requests.post(
           url = settings.OTP_VERIFY_URL, 
            data = params,
            headers = headers)

        print('generate response', verifyResponse)
        return verifyResponse.json()

def sendSMS( message: str, phone_numbers):
        data = {
        'sender': settings.SENDER_ID,
        'message': message,
        'recipients': phone_numbers
        }
    
        headers = {
        'api-key':settings.API_KEY,
        "Content-Type": "application/json"
        } 
        params = json.dumps(data)
        print('data', params)
        messageResponse = requests.post(
           url = settings.SEND_SMS_URL, 
            data = params,
            headers = headers)

        print('send response', messageResponse)
        return messageResponse.json()
   