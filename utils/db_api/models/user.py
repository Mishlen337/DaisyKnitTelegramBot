"""Model to declare classes related with user."""

from contracts import contract
from datetime import datetime
from numpy import uint32
from utils.db_api.consts import RawConnection as cn


class User:
    """Class to declare Daisy Knit user."""
    def __init__(self, user_id_tel: uint32):
        self.user_id_tel = user_id_tel
        self.id: uint32 = None
        self.first_name: str = None
        self.middle_name: str = None
        self.last_name: str = None
        self.email: str = None
        self.telephone: str = None
        self.is_authorized: bool = None
        # time when user joined in telegram bot
        self.created_at: datetime = None

    @property
    def is_registered(self) -> bool:
        """Checks whether user shared his/her telephone or not

        :return: shared his/her telephone or not
        :rtype: bool
        """
        if not (self.telephone is None):
            return True
        return False

    async def set_info_db(self):
        """Sets info about user from mysql."""
        # TODO fil fields from db
        sql = """
        SELECT id, first_name, middle_name, last_name, email,
        telephone, authorized, created FROM daisyKnitSurvey.user
        WHERE user_tel_id = (?,);
        """
        params = (self.user_id_tel,)
        info = await cn._make_request(sql, params, True)
        self.id = info[0]
        self.first_name = info[1]
        self.middle_name = info[2]
        self.last_name = info[3]
        self.email = info[4]
        self.telephone = info[5]
        self.is_authorized = info[6]
        # time when user joined in telegram bot
        self.created_at = info[7]

    @staticmethod
    @contract
    async def get_user_by_telephone(tel: str):
        """Returns user by his telephone in db

        :param tel: telephone number
        :type tel: str
        :return: users instance
        :rtype: User
        """
        # TODO Determine user_id in telegram bot by telephone
        # Make user instance
        sql = """
        SELECT user_id_tel FROM daisyKnitSurvey.user
        WHERE telephone = (?,);
        """
        params = (tel,)
        user_id_tel = await cn._make_request(sql, params, True)
        return User(user_id_tel)

    async def save(self):
        """Saves user in mysql db."""
        sql = """
        INSERT IGNORE INTO daisyKnitSurvey.user
        (user_id_tel, first_name, middle_name, second_name,
        email, telephone, authorized, created)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
        """
        self.created_at = datetime.now()
        params = (self.user_id_tel, self.first_name, self.middle_name,
                  self.last_name, self.email, self.telephone,
                  self.is_authorized, self.created_at)
        await cn._make_request(sql, params)
