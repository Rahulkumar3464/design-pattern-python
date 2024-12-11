from GoodsServiceVehicle import GoodsServiceVehicle
from SportsVehicle import SportsVehicle
from OffRoadVehicle import OffRoadVehicle

if __name__ == '__main__':

    VehicelList = []
    VehicelList.append(GoodsServiceVehicle())
    VehicelList.append(SportsVehicle())
    VehicelList.append(OffRoadVehicle())

    for vehicle in VehicelList:
        vehicle.drive()