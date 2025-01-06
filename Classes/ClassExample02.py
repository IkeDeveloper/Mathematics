class Vehicle:
    def __init__(self, n_wheels=0):
        self.n_wheels = n_wheels
        self.drive()

    def drive(self):
        print("No wheels to drive")

class Car(Vehicle):
    def __init__(self):
        super().__init__()

        self.s=self.n_wheels = 4
        self.s_belt_make = "xenon design"

class MotorBike(Vehicle):
    def __init__(self):
        super().__init__()
        self.s=self.n_wheels = 2
        self.windsheild_make = "Star industrial"

class SinclairC5(Vehicle):
    pass





my_car =Car()
print("car has " + str(my_car.s)+" wheels")
print("The car seat belt manufacturer is "+my_car.s_belt_make)

my_motorbike=MotorBike()
print("motobike has "+str(my_motorbike.s)+" wheels")
print("The motorbike wind sheild manufacurer is "+my_motorbike.windsheild_make)

print("The Sinclair C5 has "+str(SinclairC5(3).n_wheels)+" wheels")





