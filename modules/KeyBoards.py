from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


client_main = InlineKeyboardMarkup()
client_main.add(InlineKeyboardButton('Русский', callback_data='language ru'))
client_main.add(InlineKeyboardButton('English', callback_data='language en'))