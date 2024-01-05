"""Module to declare fastApi web server to get webhooks from telegram."""
import uvicorn

import aiogram
import pandas as pd
from fastapi import FastAPI
from fastapi import Request

from aiogram import types, Dispatcher, Bot
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InputFile

import handlers, filters
from utils.db_api.models.user import User
from utils.db_api.models.survey import Survey
from utils.db_api.models.survey_response import SurveyResponse
from notifiers.survey.subscribers import TelegramBotSurveyNotifier
from notifiers.survey.event_args import SurveyEventArgs


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


@app.post(config.NOTIFICATION_SURVEY_PATH)
async def bot_notification_survey(request: Request):
    try:
        text = (await request.body()).decode("utf-8")
        print(text)
        survey_response_ids = list(set([int(val) for val in text.split('\n')]))
    except Exception as ex:
        logger.error(ex)
        return 400, "Incorrect request body"

    users = []
    for survey_response_id in survey_response_ids:
        survey_response = SurveyResponse(survey_response_id)
        await survey_response.set_info_db()
        if not survey_response.user:
            logger.info("No such servey response")
            continue

        user = survey_response.user
        if user not in users:
            users.append(user)
            dp.bot.send_message(user.user_id_tel, "Ваши ближашие заказы: ")

        responses = await survey_response.get_responses_db()
        excel_filename = f"results_{user.user_id_tel}.xlsx"
        ##########
        writer = pd.ExcelWriter(excel_filename, engine='xlsxwriter')
        pd.DataFrame(responses).to_excel(writer, sheet_name='Sheet1', index=False)

        worksheet = writer.sheets['Sheet1']
        worksheet.autofit()
        writer.close()
        ############
        f = InputFile(excel_filename, "results.xlsx")
        await dp.bot.send_document(chat_id=user.user_id_tel, document=f, caption=survey_response.survey.name)
    
    notification_survey = Survey(config.NOTIFICATION_SURVEY_NAME)
    await notification_survey.set_info_db()
    if notification_survey.id is None:
        return 400, "No such notification survey"

    for user in users:
        event_args = SurveyEventArgs(user, notification_survey)
        TelegramBotSurveyNotifier().update(event_args)

@app.on_event("shutdown")
async def on_shutdown():
    """Closes all connections."""
    await dp.bot.close()
    await dp.storage.close()
    await dp.storage.wait_closed()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7777)
