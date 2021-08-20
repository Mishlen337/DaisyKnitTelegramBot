from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.helper import Helper, HelperMode, ListItem


class DaisyKnitStates(StatesGroup):
    mode = HelperMode.snake_case

    initial_state = State()
