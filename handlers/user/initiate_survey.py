from aiogram import types
from loguru import logger
from aiogram.dispatcher.storage import FSMContext
from notifiers.survey.manager import SurveyManager
from notifiers.survey.subscribers import LoggerSurveyNotifier,\
    TelegramBotSurveyNotifier

from data import config
from utils.db_api.models.user import User
from utils.db_api.models.survey import Survey
from notifiers.survey.event_args import SurveyEventArgs


class SurveyInvitation:
    """Class to declare handler to send invitation of a survey for admin"""

    def __init__(self):
        _subscribers = [LoggerSurveyNotifier(), TelegramBotSurveyNotifier()]
        self.survey_manager = SurveyManager()
        for sub in _subscribers:
            self.survey_manager.subscribe(sub)

    async def survey_invitation(self, msg: types.Message, state: FSMContext):
        """Sends message to initiate a survey

        :param message: Message instance
        :type message: types.Message
        :param state: [description]
        :type state: FSMContext
        """
        try:
            user = User(msg.from_user.id)
            await user.set_info_db()
            survey = Survey(config.SURVEY_NAME)
            await survey.set_info_db()

            if survey.id is None:
                await msg.answer("Нет активного опроса!")
            else:
                event_args = SurveyEventArgs(user, survey)
                await self.survey_manager.notify(event_args)

        except Exception as ex:
            logger.error(ex)
            await msg.answer("Проблемы с базой данных. Попробуйте позже! Поддержка @mishlen25")
