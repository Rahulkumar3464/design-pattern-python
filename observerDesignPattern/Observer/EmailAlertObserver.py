from .NotificationAlertObserver import NotificationAlertObserver

class EmailAlertObserver(NotificationAlertObserver):

    def __init__(self,email_id,observable):
        super(EmailAlertObserver,self).__init__(communication_channel=email_id,observable=observable)

    def update(self):
        self.send_mail("Product is in stock, hurry up!!")

    def send_mail(self, msg):
        print("email is sent to email_id:: %s, msg:: %s" %(self.communication_channel,msg))