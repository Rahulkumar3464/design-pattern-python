from NormalDriveStrategy import NormalDriveStrategy
from Vehicle import Vehicle

class GoodsServiceVehicle(Vehicle):

    def __init__(self):
        super(GoodsServiceVehicle,self).__init__(NormalDriveStrategy())