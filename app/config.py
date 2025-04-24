# app/config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-to-guess-string'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Market data API configurations
    MARKET_API_KEY = os.environ.get('MARKET_API_KEY')
    MARKET_API_BASE_URL = os.environ.get('MARKET_API_BASE_URL')
    
    # WebSocket configurations
    WS_SERVER = os.environ.get('WS_SERVER')
    WS_PORT = os.environ.get('WS_PORT', 6789)
    WS_API_KEY = os.environ.get('WS_API_KEY')