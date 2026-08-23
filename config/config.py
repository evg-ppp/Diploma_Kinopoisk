import os

from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
API_URL = os.getenv("API_URL")
API_KEY = os.getenv("API_KEY")
print(API_URL)
print(API_KEY)