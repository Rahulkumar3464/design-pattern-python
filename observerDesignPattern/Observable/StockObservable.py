from abc import ABC, abstractmethod

#from ..Observer.NotificationAlertObserver import NotificationAlertObserver


class StockObservable(ABC):

    def __init__(self):
        self.observerList = []
        self.stockCount = 0

    @abstractmethod
    def add(self, observer):
        pass

    @abstractmethod
    def remove(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass

    @abstractmethod
    def set_stock_count(self, count):
        pass

    @abstractmethod
    def get_stock_count(self):
        pass