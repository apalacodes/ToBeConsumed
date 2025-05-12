import os 
from dotenv import load_dotenv
load_dotenv(dotnev_path='.env')
APP_NAME = os.getenv('APP_NAME', 'ToBeConsumed')
DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'

