import aiogram
from aiogram import Dispatcher
from data import config


if __name__ == "__main__":
    bot = aiogram.Bot(token=config.BOT_TOKEN,
                      parse_mode=aiogram.types.ParseMode.HTML)
    dp = Dispatcher(bot)
    import filters
    import handlers
    import middlewares
    filters.setup(dp)
    middlewares.setup(dp)
    handlers.errors.setup(dp)
    handlers.user.setup(dp)
    aiogram.executor.start_polling(dispatcher=dp)
