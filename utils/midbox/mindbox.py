"""Module to communicate with mindbox api."""
from utils.db_api.models.user import User
from utils.db_api.models.survey_response import SurveyResponse


class MindBox:
    """Class to communicate with mindbox api."""

    def __init__(self):
        # TODO initialize variables
        pass

    async def set_user_info(self, user: User):
        """Sets users info quering MindBox API

        :param user: [description]
        :type user: User

        """ 
        # TODO response
        pass

    async def send_survey_response(self, survey_response: SurveyResponse):
        """Sends survey response to mindbox API

        :param survey_response: [description]
        :type survey_response: SurveyResponse
        """
        pass
