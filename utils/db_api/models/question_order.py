"""Module to declare question order model."""

from .question import Question
from .survey import Survey
from numpy import uint32


class QuestionOrder:
    """Class to declare question order model."""
    def __init__(self, question: Question, survey: Survey):
        self.question = question
        self.survey = survey
        self.order: uint32 = None
   
    def save(self):
        """Saves question in mysql db table."""
        # TODO save question in mqsql db
        pass
