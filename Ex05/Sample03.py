class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def getName(self):
        return self.__name

class Student(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.stdID = id

class Teacher(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.fcID = id

    def getName(self):
        return "Hello " + self.name
    
############### RUN ###############
t01 = Teacher("Adam", 100, "ABC123")
print(t01.getName())