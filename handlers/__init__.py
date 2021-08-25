from aiogram.dispatcher.dispatcher import Dispatcher
from . import errors
from . import user
from . import admin


def setup(dp: Dispatcher):
    user.setup(dp)
    errors.setup(dp)
    admin.setup(dp)
