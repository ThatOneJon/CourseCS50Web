class Vehicle:
    color = "white"
    def __init__(self, max, milage):
        self.max_speed = max
        self.mileage = milage
        self.tax = 350

    def seating(self, capacity):
        return f"seating : {capacity}"

    def fare(self):
        fares = self.tax * 0,25 + self.tax 
        return fares

    def __str__(self):
        return(f"Max speed: {self.max_speed}  \nMileage: {self.mileage} \nDefault-Color: {self.color} fare: {self.fare}" )

class Motorcycle(Vehicle):
    def seating(self, capacity=2):
        return super().seating(capacity=2)

class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        return amount[1] + 25


def main():
    car = Vehicle(150, 200000)
    R1 = Motorcycle(250,50000)
    print(R1)
    print(R1.tax)
    schoolbus = Bus(100, 100000)
    print(f"the fare on the schoolbus is: {schoolbus.fare()} \nis schoolbus a bus? {isinstance(schoolbus, Vehicle)}")









if __name__ == "__main__":
    main()