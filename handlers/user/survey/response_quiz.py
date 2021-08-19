"""Module to handle response to a quiz question."""
from aiogram import types
from contracts import contract
from aiogram.dispatcher import FSMContext


@contract
async def get_response(poll_answer: types.PollAnswer, state: FSMContext):
    """PollAnswer handler to get response to a pollAnswer type question

    :param poll_answer: PollAnswer instance caused by received quiz
    :type poll_answer: types.PollAnswer
    """
    state.set_data({"poll": []})
    # TODO Получить тестовое представление ответа
    # Сделать pop
    # Положить ответ в БД.
    # Посмотреть пуст ли список вопросов
    # Да - отправить в MindBox
    # Нет - оптравить новый вопрос с учетом типа
    pass


@contract
async def get_response_error(message: types.PollAnswer):
    """PollAnswer handler to send message about finishing
    previous survey

    :param message: PollAnswer instance caused by received quiz
    :type message: types.PollAnswer
    """
    # TODO send message about finishing previous survey
    pass
