#class and instance attributes

class Dog:
    #class attribute
    species = 'mammal'
    #instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

#instantiate the Dog class
        
philo = Dog("Philo", 5)

mikey = Dog("Mikey", 6)

#access the instance attributes

print("{} is {} and {} is {}".format(philo.name, philo.age, mikey.name, mikey.age))

#access the class attributes

print("{} is a {}".format(philo.name, philo.__class__.species))
print("{} is a {}".format(mikey.name, mikey.__class__.species))


#class attributes are the common attributes for all the instances of the class

#instance attributes are the attributes that are specific to each instance of the class
