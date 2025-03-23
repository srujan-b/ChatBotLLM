from pydantic import BaseSettings

class Settings(BaseSettings):

    MODEL_NAME:str = "llama3:vision-preview" 

settings = Settings()