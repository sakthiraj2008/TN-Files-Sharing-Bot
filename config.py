# ©Dp_botz©




import os, re
import logging
from logging.handlers import RotatingFileHandler

id_pattern = re.compile(r'^.\d+$')

#Bot token @Botfather
TG_BOT_TOKEN = t("7637355126:AAF4pLwacEQJhGoiYON1TNd3neWfnM4P3E8")

#Your API ID from my.telegram.org
APP_ID = int("11472991"))

#Your API Hash from my.telegram.org
API_HASH = ("c78c50d54baf2173e8b3f75c359c0c72")

#Your db channel Id
CHANNEL_ID = int("-1002318167392"))

#OWNER ID
OWNER_ID = int("1430742022"))

#Port
PORT = ("8080")

#Database 
DB_URI = ("mongodb+srv://KarthikMovies:KarthikUK007@cluster0.4l5byki.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = ("mongodb")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int("-1002378206551"))


REACTIONS = ["🤝", "😇", "🤗", "😍", "👍", "🎅", "😐", "🥰", "🤩", "😱", "🤣", "😘", "👏", "😛", "😈", "🎉", "⚡️", "🫡", "🤓", "😎", "🏆", "🔥", "🤭", "🌚", "🆒", "👻", "😁"] #don't add any emoji because tg not support all emoji reactions




TG_BOT_WORKERS = int( "4"))

#start message
START_MSG = ("Hello 👋 {first} 💙 I can store private files in Specified Channel and other users can access it from special link ✅ Developer @TN_Botz")
try:
    ADMINS=[]
    for x in (os.environ.get("7188069786","1430742022").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = t("hello - {username} join my channel 👍 Next Click , Try again ✅ Developer channel @TN_botz")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = ("{previouscaption}\n\n𝐉ᴏɪɴ ➠ @TAMIL_HQ_LINKZZ ✅")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if ("False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = (None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot! you need Own Bot Contact To My owner @Coding_Kakashi_Bot"

ADMINS.append(OWNER_ID)
ADMINS.append(1430742022)

# Set to False inside the bracket if you don't want to use Request Channel else set it to Channel ID
REQ_CHANNEL = os.environ.get("-1002298937998")
REQ_CHANNEL = int(REQ_CHANNEL) if REQ_CHANNEL and id_pattern.search(REQ_CHANNEL) else False
JOIN_REQS_DB = os.environ.get("mongodb+srv://KarthikMovies:KarthikUK007@cluster0.4l5byki.mongodb.net/?retryWrites=true&w=majority")

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
