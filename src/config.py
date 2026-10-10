import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    COMPANY_NAME = os.getenv("COMPANY_NAME", "Home Credit")
    AGENT_NAME = os.getenv("AGENT_NAME", "Sharukh")
    AGENT_GENDER = os.getenv("AGENT_GENDER", "Male")
    PORT = int(os.getenv("PORT", 8000))
    DEBUG = os.getenv("DEBUG", "True").lower() == "true"