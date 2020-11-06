from app import create_app
from dotenv import load_dotenv

load_dotenv('.env') #the path to your .env file

app = create_app()
