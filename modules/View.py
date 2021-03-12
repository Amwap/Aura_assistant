import logging
from modules.BotCallback import bot


async def send_text(message):
    await bot.send_message(message.from_user.id, 'text')