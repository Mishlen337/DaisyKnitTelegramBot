"""Module to declare notification managers and their subscribers."""
from abc import ABC, abstractmethod


class AbstractNotificationManager(ABC):
    """Abstract manager for event generation."""

    @abstractmethod
    def subscribe(self, subscriber):
        """Subscribes observer to handle event.

        :param subscriber: observer
        """
        pass

    @abstractmethod
    def unsubscribe(self, subscriber):
        """Unsubscribes observer to handle an event.

        :param subscriber: observer
        """
        pass

    @abstractmethod
    async def notify(self, event_args):
        """Notifies observers of an event.

        :param event_args: data of an event
        """
        pass


class AbstractSurveyObserver(ABC):
    """Abstract observer to handle survey event."""

    @abstractmethod
    async def update(self, event_args):
        """Sends invitation to take a survey.

        :param event_args: data of an event
        :type event_args: [type]
        """
        pass


class AbstractResponsesSurveyObserver(ABC):
    """Abstract observer to handle responses to a survey event."""

    @abstractmethod
    async def update(self, event_args):
        """Sends survey responses.

        :param event_args: data of an event
        :type event_args: [type]
        """
        pass
