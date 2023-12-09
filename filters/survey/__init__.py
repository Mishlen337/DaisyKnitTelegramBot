"""Package to declare filters for a survey and its questions."""
from aiogram import Dispatcher

from .response import ResponseTypeValidFilter
from .survey import SurveyValidFilter


def setup(dp: Dispatcher):
    dp.filters_factory.bind(ResponseTypeValidFilter)
    dp.filters_factory.bind(SurveyValidFilter)
