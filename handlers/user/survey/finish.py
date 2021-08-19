"""Module to declare handler to finish survey"""

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


async def finish(message: types.Message, state: FSMContext):
    """Handler to finish survey."""
    # TODO Delete data related with survey
    # Set initial state
    pass
