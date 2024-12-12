from datetime import datetime

class EntranceGate:

    def __init__(self,level):
        self.parking_level_objs = [ ParkingLevel(level_number) for level_number in range(level)]

    def find_parking_space(self,vehicle):
        for parking_level_obj in self.parking_level_objs:
            spot = parking_level_obj.find_parking_space(vehicle)
            if spot:
                break
        return spot

    def park_vehicle(self,spot,vehicle):
        spot.park_vehicle(vehicle)
        return self.generate_ticket(spot, vehicle.vehicle_type)

    def generate_ticket(self,spot,vehicle_type):
        ticket = Ticket(spot,vehicle_type)
        return ticket

    def cancel_reservation(self,spot):
        spot.cancel_reservation()

class Ticket:
    def __init__(self,spot,vehicle_type):
        self.entry_time = datetime.now()
        self.spot = spot
        self.vehicle_type = vehicle_type
        self.spot_number = spot.spot_number

class ExitGate:

    def calculate_price(self,ticket):
        return ticket.spot.get_price()

    def take_payment(self,ticket):
        print("Bill is paid Now")
        ticket.spot.remove_vehicle()


class ParkingLevel:

    def __init__(self,level_number,capacity_for_two_wheeler=5,capacity_for_four_wheeler=5):
        self.level_number = level_number
        self.two_wheeler_spots = [ TwoWheelerSpot(spot_number) for spot_number in range(capacity_for_two_wheeler)]
        self.four_wheeler_spots = [FourWheelerSpot(spot_number) for spot_number in range(capacity_for_four_wheeler)]

    def find_parking_space(self,vehicle):
        spots = self.get_spots(vehicle.vehicle_type)
        for spot in spots:
            if spot.is_empty():
                spot.is_reserved = True
                print("spot found")
                return spot
        print("No spot found")
        return None

    def get_spots(self,vehicle_type):
        spots_type = {"TWO_WHEELER":self.two_wheeler_spots,"FOUR_WHEELER": self.four_wheeler_spots}
        return spots_type.get(vehicle_type)

class ParkingSpot:

    price = 0
    def __init__(self,spot_number):
        self.spot_number = spot_number
        self.vehicle = None
        self.is_reserved = False

    def park_vehicle(self, vehicle):
        self.vehicle = vehicle

    def remove_vehicle(self):
        self.vehicle = None

    @classmethod
    def update_price(cls,price):
        cls.price = price

    def is_empty(self):
        if self.vehicle is None and not self.is_reserved:
            return True
        return False

    def cancel_reservation(self):
        self.is_reserved = False

class TwoWheelerSpot(ParkingSpot):

    def __init__(self,spot_number):
        super().__init__(spot_number)

    def get_price(self):
        return self.price

class FourWheelerSpot(ParkingSpot):

    def __init__(self,spot_number):
        super().__init__(spot_number)

    def get_price(self):
        return self.price


class Vehicle:

    def __init__(self,vehicle_type):
        self.vehicle_type = vehicle_type

if __name__ == "__main__":

    entrance_gate = EntranceGate(1)
    exit_gate = ExitGate()
    print(entrance_gate.__dict__)
    TwoWheelerSpot.update_price(30)
    FourWheelerSpot.update_price(100)
    vehicle = Vehicle("FOUR_WHEELER")
    spot = entrance_gate.find_parking_space(vehicle)
    print(spot.__dict__)
    ticket = entrance_gate.park_vehicle(spot,vehicle)
    print(ticket)

    price = exit_gate.calculate_price(ticket)
    print(price)
    exit_gate.take_payment(ticket)
