from Circle import Circle
from Rectangle import Rectangle
from Square import Square

class FactoryPattern:

    def get_shape(self, shape=Circle()):

        SHAPES = {"CIRCLE": Circle(),"RECTANGLE": Rectangle(), "SQUARE": Square()}
        return SHAPES.get(shape,None)