from SportyDriveStrategy import SportyDriveStrategy
from Vehicle import Vehicle

class SportsVehicle(Vehicle):

    def __init__(self):
        super(SportsVehicle,self).__init__(SportyDriveStrategy())