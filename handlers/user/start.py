from aiogram import types
from loguru import logger
from aiogram.dispatcher.storage import FSMContext

from data import config
from .initiate_survey import SurveyInvitation
from utils.db_api.models.user import User
from utils.db_api.models.survey import Survey
from notifiers.survey.event_args import SurveyEventArgs


hello_message = """Мы привозим для вас самую свежую форель в городе Бар, Черногория! 🙂

По лучшей цене из форелевых хозяйств севера Черногории в течение пары часов после вылова 💕

❗Рыба вылавливается только по предварительному заказу из прудов в Никшиче и Плужине в ночь накануне доставки.❗
"""
survey_invitation = SurveyInvitation()


async def bot_start(msg: types.Message, state: FSMContext):
    """Handler to start bot in a first entry

    :param msg: Message instance caused by received message
    :type msg: types.Message
    :param state: FSMContext instance
    :type state: FSMContext
    """
    try:
        await msg.answer(f'Привет, {msg.from_user.full_name}!')
        await msg.answer(hello_message)
        user = User(msg.from_user.id)
        user.telephone = '0'
        user.username = msg.from_user.username if msg.from_user.username else ''
        await user.save()
        await state.set_state("initial_state")

        # send survey
        survey = Survey(config.SURVEY_NAME)
        await survey.set_info_db()
        if survey.id is None:
            await msg.answer("Нет активного заказа/опроса!")
        else:
            event_args = SurveyEventArgs(user, survey)
            await survey_invitation.survey_manager.notify(event_args)

    except Exception as ex:
        logger.error(ex)
        await msg.answer("Проблемы с базой данных. Попробуйте позже! Поддержка @mishlen25")
