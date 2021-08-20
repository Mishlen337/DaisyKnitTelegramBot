"""Module to declare registration filter."""

from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from contracts import contract


class RegistrationFilter(BoundFilter):
    """Filter to check whether user have registered in telegram or not"""

    key = "is_registered"

    @contract
    def check(self, message: types.Message) -> bool:
        """Checks whether user have registered in telegram or not

        :param message: Message to register user
        :type message: types.CallbackQuery
        :return: whether user have registered in telegram or no
        :rtype: bool
        """
        pass
