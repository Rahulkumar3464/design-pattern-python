from .NotificationAlertObserver import NotificationAlertObserver


class MobileAlertObserver(NotificationAlertObserver):

    def __init__(self, mobile_no, observable):
        super(MobileAlertObserver,self).__init__(communication_channel=mobile_no,observable=observable)

    def update(self):
        self.send_sms("Product is in stock, hurry up!!")

    def send_sms(self, msg):
        print("sms is sent to mobile_no:: %s, msg:: %s"%(self.communication_channel, msg))