from ToppingsDecorator import ToppingsDecorator

class ExtraCheese(ToppingsDecorator):

    def __init__(self, pizza):
        super().__init__(pizza)

    def cost(self):
        return self.basePizza.cost() + 50