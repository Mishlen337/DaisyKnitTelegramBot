"""Module to declare survey manager."""

from typing import Set
from notifiers.abstracts import AbstractNotificationManager,\
                                AbstractSurveyObserver
from .event_args import SurveyEventArgs


class SurveyManager(AbstractNotificationManager):
    """Manager to notify about a survey."""

    def __init__(self):
        self.__subscribers: Set[AbstractSurveyObserver] = set()

    def subscribe(self, subscriber: AbstractSurveyObserver):
        """Subscribes observer to handle a survey event.

        :param subscriber: observer
        :type subscriber: AbstractSurveyObserver
        """
        self.__subscribers.add(subscriber)

    def unsubscribe(self, subscriber: AbstractSurveyObserver):
        """Unsubscribes observer to handle a survey event.

        :param subscriber: observer
        :type subscriber: AbstractSurveyObserver
        """
        self.__subscribers.remove(subscriber)
        # TODO handle Key Error

    async def notify(self, event_args: SurveyEventArgs):
        """Notifies observers of a survey event.

        :param event_args: data of an event
        :type event_args: SurveyResponse
        """
        for subscriber in self.__subscribers:
            await subscriber.update(event_args)
