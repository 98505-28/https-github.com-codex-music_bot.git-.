import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")
OWNER_USERNAME = getenv("OWNER_USERNAME","Rishu1286")
BOT_USERNAME = getenv("BOT_USERNAME" , "Vip_music_vc_bot")
BOT_NAME = getenv("BOT_NAME" , "RISHU")
ASSUSERNAME = getenv("ASSUSERNAME" , "Rishu_music")
MONGO_DB_URI = getenv("MONGO_DB_URI", None)
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
LOGGER_ID = int(getenv("LOGGER_ID"))
OWNER_ID = int(getenv("OWNER_ID"))
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/RishuBot/RishuManagement",)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)
PRIVACY_LINK = getenv("PRIVACY_LINK", "https://telegra.ph/Privacy-Policy-for-RishuMusic-01-09-2")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me