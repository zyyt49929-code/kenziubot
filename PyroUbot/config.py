import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "999"))

DEVS = list(map(int, os.getenv("DEVS", "7369828453").split()))

API_ID = int(os.getenv("API_ID", "25610"))

API_HASH = os.getenv("API_HASH", "c02e1955293080d711883ef40ea")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8425610564:AAFeXvpnZtVkDSVny1J1-QzzIrdLpGcyxoU")

OWNER_ID = int(os.getenv("OWNER_ID", "7369828453"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002886184276").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://kenzidev3:KenziDev2025@cluster0.d8bxa8a.mongodb.net/?appName=Cluster0
LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1003558835687"))
