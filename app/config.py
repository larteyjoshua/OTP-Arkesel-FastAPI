import os
from functools import lru_cache
from pydantic import BaseSettings, AnyHttpUrl, validator
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class Settings(BaseSettings):
    PROJECT_NAME: str = "OTP With Arkesel API"
    API_KEY: str = os.environ.get("API_KEY")
    API_V1_STR: str = "/api/v1"
    EXPIRY_TIME: int =  os.environ.get("EXPIRY_TIME")
    OTP_LENGTH: int = os.environ.get("OTP_LENGTH")
    SENDER_ID: str = os.environ.get("SENDER_ID")
    TYPE: str = os.environ.get("TYPE")
    OTP_GENERATE_URL: str = os.environ.get("OTP_GENERATE_URL")
    OTP_VERIFY_URL: str = os.environ.get("OTP_VERIFY_URL")
    MEDIUM: str =  os.environ.get("MEDIUM")
    SEND_SMS_URL =  os.environ.get("SEND_SMS_URL")
   

    class Config:
        case_sensitive = True
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()