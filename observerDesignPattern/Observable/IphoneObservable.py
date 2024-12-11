from .StockObservable import StockObservable
# from ..Observer.NotificationAlertObserver import NotificationAlertObserver


class IphoneObservable(StockObservable):

    def __init__(self):
        super(IphoneObservable,self).__init__()

    def add(self,observer ):
        self.observerList.append(observer)

    def remove(self, observer):
        self.observerList.remove(observer)

    def notify(self):

        for observer in self.observerList:
            observer.update()
    def set_stock_count(self, count):
        if self.stockCount ==0:
            self.notify()
        self.stockCount += count

    def get_stock_count(self):
        return self.stockCount

