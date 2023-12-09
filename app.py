"""Module to declare fastApi web server to get webhooks from telegram."""
import uvicorn

import aiogram
import asyncio
from aiogram import types, Dispatcher, Bot
from aiogram.contrib.fsm_storage.redis import RedisStorage2
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
from fastapi import FastAPI

import handlers, filters

from loguru import logger

from data import config

storage = RedisStorage2(**config.aiogram_redis)
# storage = MemoryStorage()
bot = aiogram.Bot(token=config.BOT_TOKEN, parse_mode=aiogram.types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    """Initializes filters, middlewares, handlers and webhook."""
    await bot.set_webhook(url=config.WEBHOOK_BOT_URL)
    filters.setup(dp)
    handlers.setup(dp)


@app.post(config.WEBHOOK_BOT_PATH)
async def bot_webhook(update: dict):
    """Process update from tg

    Args:
        update (dict): update from tg
    """
    telegram_update = types.Update(**update)
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    # try:
    await dp.process_update(telegram_update)
    # except Exception as e:
    #     logger.error(e)


@app.on_event("shutdown")
async def on_shutdown():
    """Closes all connections."""
    await dp.bot.close()
    await dp.storage.close()
    await dp.storage.wait_closed()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7777)
