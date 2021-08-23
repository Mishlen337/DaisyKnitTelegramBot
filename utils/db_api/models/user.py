"""Model to declare classes related with user."""

from contracts import contract
from datetime import datetime
from numpy import uint32
# from utils.db_api.consts import RawConnection as cn


class User:
    """Class to declare Daisy Knit user."""
    def __init__(self, user_id_tel: uint32):
        self.user_id_tel = user_id_tel
        self.first_name: str = None
        self.last_name: str = None
        self.middle_name: str = None
        self.telephone: int = None
        # time when user joined in telegram bot
        self.created_at: datetime = None

    @property
    async def is_authorized(self) -> bool:
        """Checks whether user is authorized in MindBox or not

        :return: authorized in MindBox or not
        :rtype: bool
        """
        # TODO check in database
        return False

    @property
    def is_registered(self) -> bool:
        """Checks whether user shared his/her telephone or not

        :return: shared his/her telephone or not
        :rtype: bool
        """
        return False

    async def set_info_db(self):
        """Sets info about user from mysql.
        """
        # TODO fil fields from db
        pass

    @staticmethod
    @contract
    def get_user_by_telephone(tel: str):
        """Returns user by his telephone in db

        :param tel: telephone number
        :type tel: uint64
        :return: users instance
        :rtype: User
        """
        # TODO Determine user_id in telegram bot by telephone
        # Make user instance
        pass

    async def save(self):
        """Saves user in mysql db

        """
        # TODO put info in user table
        # info: users info
        pass
