#encapsultion with protected access modifier
# class Person:
#     def __init__(self,name):
#         self._name = name
        
# class Employee(Person):
#     def __init__(self,name,gender):
#         super().__init__(name)
#         self.gender = gender
        
# emp = Employee("Atharva","Male")
# print(emp._name)
# print(emp.gender)

class Person:
    def __init__(self,name):
        self.__name = name
        
    def get_name(self):
        return self.__name
        
    def set_name(self,name):
        self.__name = name
        
person = Person("Atharva")
print(person.get_name())
person.set_name("Krish")
print(person.get_name())

    