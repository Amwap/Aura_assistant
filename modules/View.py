from aiogram import types
from modules.BotCallback import bot, logging
import modules.KeyBoards as kb
import modules.LanguagePack as lp

lang = 'en'


async def disclaimerView(message):
    # TODO Запрос языка
    text = lp.messages['disclaimer'][lang]
    await message.answer(text, reply_markup=kb.common['disclaimer'][lang])
    # TODO установить сцену


async def languageView(callback):
    # TODO Запрос языка
    text = lp.messages['select language'][lang]
    await bot.send_message(callback.from_user.id, text, reply_markup=kb.common['select language'][lang])
    # TODO установить сцену
    

async def currencyView(callback):
    # TODO Запрос языка
    text = lp.messages['select currency'][lang]
    await bot.send_message(callback.from_user.id, text, reply_markup=kb.common['select currency'][lang])
    # TODO установить сцену


async def getCashView(callback):
    # TODO Запрос языка
    text = lp.messages['enter cash'][lang]
    await bot.send_message(callback.from_user.id, text) 
    # TODO установить сцену


# async def feedView(message):
#     text = """
# `Балланс:  1000$`
# `Cегодня:  -50$`
# `Неделя:   -100$`
# `Месяц:    -560$`
# `Экономия: 300$`
# `-------------------------------`
# `Регулярные платежи: 5`
#     """
#     await message.answer(text, reply_markup=kb.feed, parse_mode=types.ParseMode.MARKDOWN)


# async def transactionView(message):
#     text = """
# `Сумма: -50$`
# `Категория: Продукты`
# `Описание: молоко кефир батон`
#     """
#     await message.answer(text, reply_markup=kb.new_transaction, parse_mode=types.ParseMode.MARKDOWN)