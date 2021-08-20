"""Module to declare class of survey event args."""

from utils.db_api.models.user import User
from utils.db_api.models.survey import Survey


class SurveyEventArgs:
    """Class of survey event args."""
    def __init__(self, user: User, survey: Survey):
        self.user = user
        self.survey = survey
