from curses.textpad import rectangle

from factory import FactoryPattern

if __name__ == '__main__':

    shapeFactoryObj = FactoryPattern()
    circle = shapeFactoryObj.get_shape(shape="CIRCLE")
    rectangle = shapeFactoryObj.get_shape(shape='RECTANGLE')
    square = shapeFactoryObj.get_shape(shape="SQUARE")

    circle.draw()
    rectangle.draw()
    square.draw()
