from abc import ABC, abstractmethod

class NotificationAlertObserver(ABC):

    def __init__(self,communication_channel="email_id", observable=None):
        self.communication_channel = communication_channel
        self.observable = observable

    @abstractmethod
    def update(self):
        pass