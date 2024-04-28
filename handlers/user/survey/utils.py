"""Module to send question in Telegram Bot."""

import datetime
from typing import Dict, List
from numpy import uint32
from aiogram.bot import Bot
from utils.db_api.models.question import Question
from utils.db_api.models.survey_response import SurveyResponse
from keyboards.inline.consts import InlineConstructor as ic
from aiogram.utils.callback_data import CallbackData


def get_date_by_weekday(weekday_name):
    # Словарь для преобразования названия дня недели в номер
    weekdays = {
        'пн': 0,
        'вт': 1,
        'ср': 2,
        'чт': 3,
        'пт': 4,
        'сб': 5,
        'вс': 6
    }
    if weekday_name.lower() not in weekdays:
        return None

    # Получение текущей даты
    current_date = datetime.date.today()
    # Получение номера текущего дня недели
    current_weekday = current_date.weekday()
    # Получение номера нужного дня недели
    target_weekday = weekdays[weekday_name.lower()]

    # Расчет разницы между текущим днем и нужным днем недели
    days_ahead = target_weekday - current_weekday
    if days_ahead < 0:  # Если нужный день уже прошел
        days_ahead += 7

    # Расчет и вывод даты следующего нужного дня недели
    target_date = current_date + datetime.timedelta(days=days_ahead)
    return target_date


async def send_next_question(bot: Bot, user_id_tel: uint32,
                             state_data: Dict[str, List[str]]):
    survey_response_id = next(iter(state_data))
    # Get question name from state data
    question_name = state_data[survey_response_id][0]['name']
    question = Question(question_name)
    await question.set_info_db()

    survey_response = SurveyResponse(survey_response_id)
    await survey_response.set_info_db()
    question_count = len(await survey_response.survey.get_questions())
    question_num = question_count - len(state_data[survey_response_id]) + 1

    question_template = f"[{question_num}/{question_count}] {question_name}"

    # if question.type == "quiz":
    #     responses_choice = await question.get_response_choices()
    #     list_responses_choice = []
    #     for choice in responses_choice:
    #         list_responses_choice.append(choice['name'])

    #     return await bot.send_poll(chat_id=user_id_tel, question=question_template,
    #                         options=list_responses_choice, type='quiz',
    #                         correct_option_id=len(list_responses_choice) - 1,
    #                         is_anonymous=False)

    if question.type == "callback":
        responses_choice = await question.get_response_choices()
        action_list = []
        for response in responses_choice:
            action_list.append((response['name'],
                                response,
                                CallbackData("question", "name")))
        keyboard = ic._create_kb(actions=action_list, schema=[1 for _ in range(len(responses_choice))])
        return await bot.send_message(user_id_tel, text=question_template,
                               reply_markup=keyboard)

    if question.type == "schedule":
        responses_choice = await question.get_response_choices()
        responses = await question.get_responses()
        responses_set = set([res['answer'] for res in responses])
        print(responses_set)
        print(responses_choice)

        action_list = []
        for response in responses_choice:
            weekday, time = response["name"].split()
            date = get_date_by_weekday(weekday)
            action = date.strftime('%d.%m') + ' ' + time
            if action not in responses_set:
                action_list.append((action,
                                    {'name': action},
                                    CallbackData("question", "name")))
        if action_list:
            keyboard = ic._create_kb(actions=action_list, schema=[1 for _ in range(len(action_list))])
            return await bot.send_message(user_id_tel, text=question_template,
                                reply_markup=keyboard)
        else:
            return await bot.send_message(user_id_tel, text="Cвободных дат нет!\nНапишите /finish, чтобы преждевременно завершить запись!")

    if question.type == "message":
        return await bot.send_message(user_id_tel, text=question_template)
