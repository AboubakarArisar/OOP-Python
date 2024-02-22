#dunder functions in python


class Parrot:
    def fly(self):
        print("Parrot can fly")
    def swim(self):
        print("Parrot can't swim")
    def __str__(self):
        return "Parrot"
    def __len__(self):
        return 20
    def __del__(self):
        print("Parrot is no more")

class Penguin:
    def fly(self):
        print("Penguin can't fly")
    def swim(self):
        print("Penguin can swim")
    def __str__(self):
        return "Penguin"
    def __len__(self):
        return 10
    def __del__(self):
        print("Penguin is no more")


#common interface
def flying_test(bird):
    bird.fly()


#instantiate objects
    
blu = Parrot()
peggy = Penguin()


#passing the object

flying_test(blu)
flying_test(peggy)

print(blu)
print(peggy)

print(len(blu))
print(len(peggy))

del blu
del peggy

