import logging
from aiogram import Bot, Dispatcher, types, executor
from modules.Config import *


API_TOKEN = TOKEN

logging.basicConfig(level=logging.INFO, handlers=[logging.FileHandler("bot.log"), logging.StreamHandler()])

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)