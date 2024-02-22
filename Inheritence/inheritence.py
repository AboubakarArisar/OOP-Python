#inheritence in python

class Car:
    @staticmethod

    def start():
        print("Car is starting")

    @staticmethod
    def stop():
        print("Car is stopping")



class BMW(Car):
    def __init__(self, name):
        self.name = name;




car = BMW("BMW")
car.start()
car.stop()
