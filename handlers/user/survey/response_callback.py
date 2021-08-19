"""Module to handle response to a callback question."""
from aiogram import types
from contracts import contract


@contract
async def get_response(message: types.CallbackQuery):
    """Callback handler to get response to a callback type question

    :param message: Callback instance caused by callback from inline button
    :type message: types.CallbackQuery
    """
    # TODO Получить тестовое представление ответа
    # Сделать pop
    # Положить ответ в БД.
    # Посмотреть пуст ли список вопросов
    # Да - отправить в MindBox
    # Нет - оптравить новый вопрос с учетом типа
    pass


@contract
async def get_response_error(message: types.CallbackQuery):
    """Callback handler to send message about finishing
    previous survey

    :param message: Callback instance caused by callback from inline button
    :type message: types.CallbackQuery
    """
    # TODO send message about finishing previous survey
    pass
