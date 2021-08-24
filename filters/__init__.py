from aiogram import Dispatcher

from .is_admin import AdminFilter
from .is_registered import RegistrationFilter
from . import survey


def setup(dp: Dispatcher):
    survey.setup(dp)
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(RegistrationFilter)
