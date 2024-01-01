"""Model to declare classes related with user."""


from datetime import datetime
from numpy import uint32
from utils.db_api.consts import RawConnection as cn


class User:
    """Class to declare Daisy Knit user."""
    def __init__(self, user_id_tel: uint32):
        self.user_id_tel = user_id_tel
        self.username = None
        self.id: uint32 = None
        self.first_name: str = None
        self.middle_name: str = None
        self.last_name: str = None
        self.email: str = None
        self.telephone: str = None
        self.authorized: bool = None
        # time when user joined in telegram bot
        self.created: datetime = None

    @property
    def is_registered(self) -> bool:
        """Checks whether user shared his/her telephone or not

        :return: shared his/her telephone or not
        :rtype: bool
        """
        if self.telephone is None:
            return False
        return True

    async def set_info_db(self):
        """Sets info about user from mysql."""
        # TODO fil fields from db
        sql = """
        SELECT id, username, first_name, middle_name, last_name, email,
        telephone, authorized, created FROM daisyKnitSurvey.user
        WHERE user_id_tel = %s;
        """
        params = (self.user_id_tel,)
        info = await cn._make_request(sql, params, True)
        if info is None:
            return
        self.id = info['id']
        self.username = info['username']
        self.first_name = info['first_name']
        self.middle_name = info['middle_name']
        self.last_name = info['last_name']
        self.email = info['email']
        self.telephone = info['telephone']
        self.authorized = info['authorized']
        # time when user joined in telegram bot
        self.created = info['created']

    @staticmethod
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
        WHERE telephone = %s;
        """
        params = (tel,)
        user_id_tel = await cn._make_request(sql, params, True)
        return User(user_id_tel)

    async def save(self):
        """Saves user in mysql db."""
        sql = """
        INSERT INTO daisyKnitSurvey.user
        (user_id_tel, username, first_name, middle_name, last_name,
        email, telephone, authorized, created)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        AS new(u, un, f, m, l, e, t, a, c)
        ON DUPLICATE KEY UPDATE
        username = un,
        first_name = f,
        middle_name = m,
        last_name = l,
        email = e,
        authorized = a,
        created = c;
        """
        self.created = datetime.now()
        params = (self.user_id_tel, self.username, self.first_name, self.middle_name,
                  self.last_name, self.email, self.telephone,
                  self.authorized, self.created)
        await cn._make_request(sql, params)
