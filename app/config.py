import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise EnvironmentError("OPENAI_API_KEY .env dosyasında bulunamadı")

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY