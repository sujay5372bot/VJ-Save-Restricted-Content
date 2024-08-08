import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "23850382"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "df22460e007e9a50eb7f688d6d8ee2c2")

#Database 
DB_URI = os.environ.get("DB_URI", "")
