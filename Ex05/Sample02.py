class Student:
    def __init__(self, name, age, id, parent):
        self.name = name
        self.age = age
        self.stdID = id
        self.parent = parent
    
    # getter
    def getID(self) -> str:
        return self.stdID

    # setter
    def setID(self, id) -> None:
        self.setID = id

class Teacher:
    def __init__(self, name, age, id, courseList):
        self.name = name
        self.age = age
        self.fcID = id
        self.course = courseList

        # getter
    def getID(self) -> str:
        return self.fcID

    # setter
    def setID(self, id) -> None:
        self.fcID = id





################### RUN ################



s01 = Student("Seoyeong", 19, "abc123", "ABC")
s02 = Student("Daeju", 12, "ccb123", "BGT")
s03 = Student("Beomkyu", 8, "bbc445", "BTS")


t01 = Teacher("Adam", 100, "fff123", ["CS", "Math"])
t02 = Teacher("Seoneun", 50, "fff4111", ["History", "Spanish"])