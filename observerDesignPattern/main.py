from Observable.IphoneObservable import IphoneObservable
from Observer.EmailAlertObserver import EmailAlertObserver
from Observer.MobileAlertObserver import MobileAlertObserver

if __name__=='__main__':

    iphone_stock_observable = IphoneObservable()
    observer1 = EmailAlertObserver(email_id = "xyz@gmail.com",observable=iphone_stock_observable)
    observer2 = MobileAlertObserver(mobile_no="+917321938939", observable=iphone_stock_observable)
    observer3 = EmailAlertObserver(email_id='shgvds@gmail.com', observable=iphone_stock_observable)

    iphone_stock_observable.add(observer1)
    iphone_stock_observable.add(observer2)
    iphone_stock_observable.add(observer3)

    iphone_stock_observable.set_stock_count(10)

