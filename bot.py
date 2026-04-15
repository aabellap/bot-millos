import requests
from bs4 import BeautifulSoup
import time
from telegram import Bot

TOKEN = "TU_TOKEN"
CHAT_ID = "TU_CHAT_ID"

URL = "https://www.entradasmillonarios.com/"

bot = Bot(token=TOKEN)

def revisar():
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(URL, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    texto = soup.get_text().lower()

    if "vs" in texto or "comprar" in texto:
        bot.send_message(chat_id=CHAT_ID, text="🔥 YA SALIERON BOLETAS DE MILLONARIOS")
        return True
    return False

while True:
    try:
        print("Revisando...")
        revisar()
        time.sleep(180)
    except Exception as e:
        print(e)
        time.sleep(180)
