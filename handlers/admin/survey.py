"""Module to declare survey handlers for admin"""

from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from notifiers.survey.manager import SurveyManager
from notifiers.survey.subscribers import LoggerSurveyNotifier,\
    TelegramBotSurveyNotifier
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
        user = User(msg.from_user.id)
        await user.set_info_db()
        survey = Survey("Работа команды DaisyKnit")
        await survey.set_info_db()
        event_args = SurveyEventArgs(user, survey)
        await self.survey_manager.notify(event_args)
