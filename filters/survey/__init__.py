"""Package to declare filters for a survey and its questions."""
from aiogram import Dispatcher

from .question import QuestionValidFilter
from .survey import SurveyValidFilter


def setup(dp: Dispatcher):
    dp.filters_factory.bind(SurveyValidFilter)
