class Student:
    def __init__(self, name : str, id : str):
        self.name = name
        self.__id = id

    def setName(self, newName : str) -> None:
        self.name = newName

    def setID(self, newID : str) -> None:
        self.__id = newID

    def getName(self) -> str:
        return self.name
    
    def getID(self) -> str:
        return self.__id
    

###### RUN #####
s1 = Student("Seoyeong", "121212")
s2 = Student("Hayeong", "050505")
print(s1.getID())
# pritn(s1.__id)
print(s2.getName())
print(s2.name)
