from pathlib import Path
from dotenv import load_dotenv
import os
load_dotenv(dotenv_path='.env')
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
CLIENT_SECRET_FILE = os.getenv('CLIENT_SECRET_FILE')
SCOPES = os.getenv('SCOPES', '')
APPLICATION_NAME = os.getenv('APPLICATION_NAME', '')
BOT_BASE_SERVER_ID = os.getenv('BOT_BASE_SERVER_ID')
BOT_USER_ID = os.getenv('BOT_USER_ID')
BOT_LOGGER_CHANNEL_ID = os.getenv('BOT_LOGGER_CHANNEL_ID')
PROJECT_DOMAIN = os.getenv("PROJECT_DOMAIN")
PORT = os.getenv("PORT")
GPVLU = os.getenv("GPVLU")
