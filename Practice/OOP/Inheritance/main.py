#single Inheritance
# class Animal:
#     def __init__(self,name):
#         self.name = name
    
#     def speak(self):
#         print(f"woof") 
        
# class Dog(Animal):
#     def __init__(self,name,owner):
#         super().__init__(name)
#         self.owner = owner
        
# dog = Dog("Tommy","Krish")
# print(dog.name)
# dog.speak()

#multiple Inheritance
# class Animal:
#     def __init__(self,name):
#         self.name = name
        
    
        
# class Pet:
#     def __init__(self,owner):
#         self.owner = owner
        
# class Dog(Animal,Pet):
#     def __init__(self,name,owner):
#         Animal.__init__(self,name)
#         Pet.__init__(self,owner)
        
#     def speak(self):
#         return f"{self.name} say woof"
        
# dog = Dog("Tommy","Krish")
# print(dog.name)
# print(dog.speak())

#hierarchical inheritance
# class Animal:
#     def speak(self):
#         return "Animal sound"

# # Derived class 1
# class Dog(Animal):
#     def bark(self):
#         return "Woof!"

# # Derived class 2
# class Cat(Animal):
#     def meow(self):
#         return "Meow!"

# # Create objects of the derived classes
# dog = Dog()
# cat = Cat()

# print(dog.speak())  # Inherited from Animal
# print(dog.bark())   # Defined in Dog
# print(cat.speak())  # Inherited from Animal
# print(cat.meow())   # Defined in Cat
    
#mulilevel inheritance
# class Animal:
#     def speak(self):
#         return "Animal sound"

# class Dog(Animal):
#     def bark(self):
#         return "Dog barks"
        
# class Bulldog(Dog):
#     def size(self):
#         return "Medium sized dog"
        
# dog = Bulldog()
# print(dog.bark())

    
    