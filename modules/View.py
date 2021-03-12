
from modules.BotCallback import bot, logging
import modules.KeyBoards as kb
import modules.LanguagePack as lp

async def mainView(message):
    text = lp.welcome_text['ru']
    a = await message.answer(text, reply_markup=kb.client_main)
    print(a)