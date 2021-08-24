"""Module to handle results of getting contact."""

from contracts import contract
from aiogram.dispatcher.storage import FSMContext
from aiogram import types
from data import events
from utils.db_api.models.user import User
from utils.db_api.models.survey import Survey
from notifiers.survey.event_args import SurveyEventArgs


@contract
async def get_contact(msg: types.Message, state: FSMContext):
    """Handler to get telephone number

    :param msg: Message instance caused by sending contact
    :type msg: types.Message
    :param state: FSMContext instance
    :type state: FSMContext
    """
    user = User(msg.from_user.id)
    user.telephone = msg.contact.phone_number
    # TODO get info from MindBox
    await user.save()
    user.first_name = 'lol'
    # Reply user that user is saved in db
    keyboard = types.ReplyKeyboardRemove()
    await msg.bot.send_message(msg.from_user.id,
                               "Вы успешно отправили свой номер",
                               reply_markup=keyboard)
    # Generate event to send a survey
    survey = Survey("Работа команды DaisyKnit")
    event_args = SurveyEventArgs(user, survey)
    await events.survey_manager.notify(event_args)
    await state.set_state("initial_state")
