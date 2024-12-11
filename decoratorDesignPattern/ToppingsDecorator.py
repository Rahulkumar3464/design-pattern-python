from BasePizza import BasePizza

class ToppingsDecorator(BasePizza):

    def __init__(self,pizza):
        self.basePizza = pizza

    def cost(self):
        return self.basePizza.cost()