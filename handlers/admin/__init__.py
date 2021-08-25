"""Package to declare admin filters"""

from aiogram import Dispatcher
from .survey import SurveyInvitation


def setup(dp: Dispatcher):
    dp.register_message_handler(SurveyInvitation().survey_invitation,
                                commands="survey", state="initial_state")
