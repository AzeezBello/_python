class Car:
    doors = 4
    side_mirror =  2
    headlight = 2
    wipper = 2

    def __init__(self, color = "black"):
        self.color = color

    def start_car(self):
        print("Starting engine")
        print("car started")
    
    def driveCar(self):
        print("Driving car at 85k/h")

    def toggleLight(self):
        print("light is on ")





