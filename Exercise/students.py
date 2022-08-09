from datetime import datetime

year = datetime.now().year

class Student():
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.year = year
        self.ID = str(firstname[0:2] + lastname[0:2]) + str(year)[2:]

    def __str__(self):
        return f"Year : {self.year} Name: {self.lastname}, {self.firstname} is: {self.age} years old- ID: {self.ID}"


class Staff():
    def __init__(self, name, id):
        self.name = name
        self.id = id


class Teacher(Staff):
        ...


class CalculateRoom():
    def __init__(self, squareM):
        self.squareM = squareM

    def squareFeet(self):
        return self.squareM * 10.76391042


    def price(self, price):
        return self.squareM / price




def main():
    derek = Student("Dereck", "Cuntbag", 20)
    print(derek)
    steve = Teacher("Geoff", 2903)
    print (steve.__dict__)

    randRoom = CalculateRoom(100)
    print(randRoom.squareFeet())
    print(randRoom.price(10))

if __name__ == "__main__":
    main()