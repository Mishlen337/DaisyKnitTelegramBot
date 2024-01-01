from aiogram import Dispatcher
from . import help
from . import start_registration
from . import get_contact
from . import start
from . import survey
from . import initiate_survey

def setup(dp: Dispatcher):
    survey.setup(dp)
    # dp.register_message_handler(start_registration.bot_start_registration, commands="start",
    #                             is_registered=False)

    # dp.register_message_handler(start_registration.bot_start_registration, commands="start",
    #                             is_registered=True)

    dp.register_message_handler(initiate_survey.SurveyInvitation().survey_invitation,
                                commands="start", state="initial_state")

    dp.register_message_handler(help.bot_help,
                                state="initial_state")

    dp.register_message_handler(help.bot_help, commands="help",
                                state="initial_state")

    # dp.register_message_handler(get_contact.get_contact,
    #                             content_types="contact",
    #                             state="telephone_state")
    
    # dp.register_message_handler(get_contact.get_contact_error,
    #                             state="telephone_state")
    dp.register_message_handler(start.bot_start, commands='start', state="*")
