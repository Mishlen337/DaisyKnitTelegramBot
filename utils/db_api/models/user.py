"""Model to declare classes related with user."""

from contracts import contract
from datetime import datetime
# from utils.db_api.consts import RawConnection as cn
from numpy import uint32, uint64


class User:
    """Class to declare Daisy Knit user."""
    async def __init__(self, user_id: uint32):
        self.user_id = user_id
        self.first_name: str = None
        self.last_name: str = None
        self.middle_name: str = None
        self.telephone: uint64 = None
        # time when user joined in telegram bot
        self.created_at: datetime = None
        self._set_user_info_db(user_id)

    @property
    async def is_authorized(self) -> bool:
        """Checks whether user is authorized in MindBox or not

        :return: authorized in MindBox or not
        :rtype: bool
        """
        # TODO check in database
        return False

    @property
    async def is_registered(self) -> bool:
        """Checks whether user shared his/her telephone or not

        :return: shared his/her telephone or not
        :rtype: bool
        """
        return False

    @contract
    async def _set_user_info_db(self, user_id: uint32):
        """Gets info about user from mysql

        :param user_id: user id in Telegram Bot chat
        :type user_id: uint32
        """
        # TODO fil fields from db
        pass

    @staticmethod
    @contract
    async def get_user_by_telephone(tel: uint64):
        """Returns user by his telephone in db

        :param tel: telephone number
        :type tel: uint64
        :return: users instance
        :rtype: User
        """
        # TODO Determine user_id in telegram bot by telephone
        # Make user instance
        pass
