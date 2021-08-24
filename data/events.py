"""Module to declare events instances."""

from notifiers.survey.manager import SurveyManager
from notifiers.survey.subscribers import LoggerSurveyNotifier,\
    TelegramBotSurveyNotifier


# Survey event declaration 
_subscribers = [LoggerSurveyNotifier(), TelegramBotSurveyNotifier()]
survey_manager = SurveyManager()
for sub in _subscribers:
    survey_manager.subscribe(sub)

