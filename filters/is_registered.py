"""Module to declare registration filter."""

from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from contracts import contract
from utils.db_api.models.user import User


class RegistrationFilter(BoundFilter):
    """Filter to check whether user have registered in telegram or not"""

    key = "is_registered"

    @contract
    async def check(self, message: types.Message) -> bool:
        """Checks whether user have registered in telegram or not

        :param message: Message to register user
        :type message: types.CallbackQuery
        :return: whether user have registered in telegram or no
        :rtype: bool
        """
        user = User(message.from_user.id)
        await user.set_info_db()
        print(user.is_registered)
        return user.is_registered
