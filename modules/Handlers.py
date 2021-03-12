import logging
from modules.BotCallback import dp, types
import modules.View as view


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    # await message.reply("Hi!nI'm EchoBot!nPowered by aiogram.")
    await view.mainView(message)


@dp.message_handler(regexp='(^cat[s]$puss)')
async def cats(message: types.Message):
    with open('datacats.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Cats are here 😺')


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


@dp.callback_query_handler(regexp='(^language)')
async def initialize_mailing(callback: types.CallbackQuery):
    print(callback.data)