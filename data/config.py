import os

from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")  # Забираем значение типа str
ADMINS = [os.getenv("ADMINS") ] # Тут у нас будет список из админов
IP = os.getenv("ip")  # Тоже str, но для айпи адреса хоста
