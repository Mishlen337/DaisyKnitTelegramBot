from aiogram import Dispatcher
from . import help
from . import start
from . import get_contact
from . import survey
from . import initiate_survey

def setup(dp: Dispatcher):
    dp.register_message_handler(start.bot_start, commands="start",
                                is_registered=False)

    dp.register_message_handler(start.bot_start_error, commands="start",
                                is_registered=True)

    dp.register_message_handler(initiate_survey.SurveyInvitation().survey_invitation,
                                commands="survey", state="initial_state")

    dp.register_message_handler(help.bot_help,
                                state="initial_state")

    dp.register_message_handler(help.bot_help, commands="help",
                                state="initial_state")

    dp.register_message_handler(get_contact.get_contact,
                                content_types="contact",
                                state="telephone_state")
    
    dp.register_message_handler(get_contact.get_contact_error,
                                state="telephone_state")
    survey.setup(dp)
