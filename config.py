from pydantic_settings import BaseSettings
from getpass import getpass
OPENAI_API_KEY = getpass()

class Settings(BaseSettings):
    open_api_key:str = OPENAI_API_KEY

settings = Settings()