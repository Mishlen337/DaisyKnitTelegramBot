import aiogram
from aiogram import Dispatcher
from data import config
# from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.contrib.fsm_storage.memory import MemoryStorage


async def on_startup(dp: Dispatcher):
    import filters
    import handlers
    import middlewares
    filters.setup(dp)
    middlewares.setup(dp)
    handlers.setup(dp)


async def on_shutdown(dp: Dispatcher):
    await dp.bot.close()
    await dp.storage.close()
    await dp.storage.wait_closed()


if __name__ == "__main__":
    # storage = RedisStorage2(**config.aiogram_redis)
    storage = MemoryStorage()
    bot = aiogram.Bot(token=config.BOT_TOKEN,
                      parse_mode=aiogram.types.ParseMode.HTML)
    dp = Dispatcher(bot, storage=storage)
    aiogram.executor.start_polling(dispatcher=dp, on_startup=on_startup,
                                   on_shutdown=on_shutdown, skip_updates=True)
