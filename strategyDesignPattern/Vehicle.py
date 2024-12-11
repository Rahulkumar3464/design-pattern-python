from strategy import  DriveStrategy

class Vehicle:

    def __init__(self, driveStragey_obj : DriveStrategy):
        self.driveStragey_obj = driveStragey_obj

    def drive(self):
        self.driveStragey_obj.drive()