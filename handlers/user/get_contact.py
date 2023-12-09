"""Module to handle results of getting contact."""
from loguru import logger
from aiogram.dispatcher.storage import FSMContext
from aiogram import types

from data import config
from data import events
from utils.db_api.models.user import User
from utils.db_api.models.survey import Survey
from utils.midbox.mindbox import MindBox
from notifiers.survey.event_args import SurveyEventArgs


async def get_contact(msg: types.Message, state: FSMContext):
    """Handler to get telephone number

    :param msg: Message instance caused by sending contact
    :type msg: types.Message
    :param state: FSMContext instance
    :type state: FSMContext
    """
    try:
        user = User(msg.from_user.id)
        user.telephone = msg.contact.phone_number
        await user.save()

        # Reply user that user is saved in db
        keyboard = types.ReplyKeyboardRemove()
        await msg.bot.send_message(msg.from_user.id,
                                "Вы успешно отправили свой номер",
                                reply_markup=keyboard)

        text = [
            'Список команд: ',
            '/help - Получить справку',
            '/survey - Начать опрос',
            '/finish - Завершить опрос',
        ]
        await msg.answer('\n'.join(text))
        # # Generate event to send a survey
        # survey = Survey(config.SURVEY_NAME)
        # await survey.set_info_db()
        # event_args = SurveyEventArgs(user, survey)
        # await events.survey_manager.notify(event_args)
        # await state.set_state("initial_state")

    except Exception as ex:
        logger.error(ex)
        await msg.answer("Проблемы с базой данных. Попробуйте позже! Поддержка @mishlen25")


async def get_contact_error(msg: types.Message, state: FSMContext):
    """Handler to get telephone number error

    :param msg: Message instance caused by sending contact
    :type msg: types.Message
    :param state: FSMContext instance
    :type state: FSMContext
    """
    await msg.bot.send_message(msg.from_user.id, "Пожалуста, поделитесь телефоном")
