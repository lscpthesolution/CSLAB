class Person:
    def __init__(self) -> None:
        self.age = 10

    def __str__(self) -> str:
        return "This is Person class"
    
    '''
    receive a new value for age and assign it to the variable, age
    '''
    def setAge(self, newAge : int) -> None:
        self.age = newAge


    def getAge(self) -> int:
        return self.age

taehoon = Person()
taehoon.setAge(19)
print(taehoon.getAge())