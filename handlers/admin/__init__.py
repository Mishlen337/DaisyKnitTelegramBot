"""Package to declare admin filters"""

from aiogram import Dispatcher
from .survey import SurveyInvitation
from .reset import reset


def setup(dp: Dispatcher):
    dp.register_message_handler(SurveyInvitation().survey_invitation,
                                commands="survey", state="initial_state",
                                is_admin=True)

    dp.register_message_handler(reset, commands="reset", state="*",
                                is_admin=True)
