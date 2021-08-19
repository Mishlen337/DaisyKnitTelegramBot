"""Module to handle response to a message question."""
from aiogram import types
from contracts import contract


@contract
async def get_response(message: types.Message):
    """Message handler to get response to a message type question

    :param message: Message instance caused by received message
    :type message: types.Message
    """
    # TODO Получить тестовое представление ответа
    # Сделать pop
    # Положить ответ в БД.
    # Посмотреть пуст ли список вопросов
    # Да - отправить в MindBox
    # Нет - оптравить новый вопрос с учетом типа
    pass


@contract
async def get_response_error(message: types.Message):
    """Message handler to send message about finishing
    previous survey

        :param message: Message instance caused by received message
        :type message: types.Message
        """
    # TODO send message about finishing previous survey
    pass
