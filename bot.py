from modules.BotCallback import dp, executor
from modules.Handlers import dp

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)