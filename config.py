from pydantic_settings import BaseSettings
from getpass import getpass

# TODO: switch before submitting!
OPENAI_API_KEY = "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"
# OPENAI_API_KEY = getpass()

class Settings(BaseSettings):
    open_api_key:str = OPENAI_API_KEY

settings = Settings()