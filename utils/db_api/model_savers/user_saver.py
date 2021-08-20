"""Module to declare saver to put user model in mysql db."""
from contracts import contract
from utils.db_api.model_savers.abstract_saver import AbstractSaver
from utils.db_api.models.user import User
from utils.db_api.consts import RawConnection


class SurveyResponseSaver(AbstractSaver):
    """Class to declare saver to put user model in mysql db."""

    @contract
    @staticmethod
    async def save(model: User):
        """Saves survey response in mysql db

        :param model: User instance
        :type model: User
        """
        # TODO put info in user table
        # info: users info
        pass
