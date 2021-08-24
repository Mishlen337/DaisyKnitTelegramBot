"""Module to declare registration filter."""

from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from contracts import contract
from utils.db_api.models.user import User


class RegistrationFilter(BoundFilter):
    """Filter to check whether user have registered in telegram or not"""

    key = "is_registered"

    def __init__(self, is_registered):
        self.is_registered = is_registered

    async def check(self, message: types.Message) -> bool:
        """Checks whether user should register in telegram or not

        :param message: Message to register user
        :type message: types.CallbackQuery
        :return: whether user should register in telegram or not
        :rtype: bool
        """
        user = User(message.from_user.id)
        await user.set_info_db()
        return user.is_registered == self.is_registered
