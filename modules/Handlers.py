import logging
from modules.BotCallback import dp, types
import modules.View as view


@dp.message_handler(commands=['start'])
async def take_disclaimer(message: types.Message):
    await view.disclaimerView(message)

@dp.callback_query_handler(lambda d: d.data and d.data.startswith("disclaimer accept"))
async def ask_language(callback: types.CallbackQuery):
    # TODO удалить предыдущую сцену
    # TODO Создание профиля через функцию 
    await view.languageView(callback)

@dp.callback_query_handler(regexp='(^language)')
async def ask_currency(callback: types.CallbackQuery):
    # TODO удалить предыдущую сцену
    # TODO Добавить язык в профиль БД
    await view.currencyView(callback)

@dp.callback_query_handler(regexp='(^currency)')
async def ask_cash(callback: types.CallbackQuery):
    # TODO удалить предыдущую сцену
    # TODO Добавить валюту в профиль БД
    # TODO Изменить состояние на "ожидание ввода блланса"
    await view.getCashView(callback)

# TODO хендлер для введёной суммы с проверкой на число + добавить ответ в сцену






