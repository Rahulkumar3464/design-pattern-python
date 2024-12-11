from SportyDriveStrategy import SportyDriveStrategy
from Vehicle import Vehicle

class OffRoadVehicle(Vehicle):

    def __init__(self):
        super(OffRoadVehicle,self).__init__(SportyDriveStrategy())