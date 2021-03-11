import logging
from modules.BotCallback import dp, types


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!nI'm EchoBot!nPowered by aiogram.")


@dp.message_handler(regexp='(^cat[s]$puss)')
async def cats(message: types.Message):
    with open('datacats.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Cats are here 😺')


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)