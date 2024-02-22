#inheritence in python
#Multi-level inheritence
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

class BMW_X1(BMW):
    def __init__(self, name):
        self.name = name    


car = BMW_X1("BMW_X1")
car.start()
car.stop()
