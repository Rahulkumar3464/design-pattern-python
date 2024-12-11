from FarmHousePizza import FarmHousePizza
from MargheritaPizza import MargheritaPizza
from Mushroom import Mushroom
from ExtraCheese import ExtraCheese

if __name__ == '__main__':

    pizza1 = Mushroom(ExtraCheese(FarmHousePizza()))
    pizza2 = Mushroom(ExtraCheese(MargheritaPizza()))
    print(pizza1.cost())
    print(pizza2.cost())