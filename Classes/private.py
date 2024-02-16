#private access modifier in python attribute and method

class Game:
    def __init__(self):
        self.__name = "GTA V"
        self.__version = 5
        self.__company = "Rockstar Games"
        
    def show(self):
        print(f"Name: {self.__name}\nVersion: {self.__version}\nCompany: {self.__company}")

g = Game()
g.show()
print(g.__name) #Error: AttributeError: 'Game' object has no attribute '__name'
print(g.__version) #Error: AttributeError: 'Game' object has no attribute '__version'
print(g.__company) #Error: AttributeError: 'Game' object has no attribute '__company'

#In the above example, we have used private access modifier for the attributes of the class Game.
#We can't access these attributes outside the class.
#If we try to access these attributes outside the class, it will give an error.

#We can access these attributes using the class method show
#We can also access these attributes using the object of the class Game
#But, we can't access these attributes using the object of the class Game outside the class Game.
