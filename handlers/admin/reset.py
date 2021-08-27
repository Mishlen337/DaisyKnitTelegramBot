"""Module to declare handler to reset state."""

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


async def reset(msg: types.Message, state: FSMContext):
    """Resets state for admin."""

    await state.reset_state(with_data=False)
