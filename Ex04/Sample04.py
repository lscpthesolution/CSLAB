class Bank:
    def __init__(self, t, n):
        self.__total = t
        self.__name = n

    def getTotal(self) -> float:
        return self.__total

    # def getName(self) -> str:
    #     return self.__name
    
    def setName(self, newName : str) -> None:
        self.__name = newName

    def setTotal(self, newTotal : float) -> None:
        self.__total = newTotal 

    def __str__(self):
        return self.__name


bank01 = Bank(99999.000, 'shinhan')
bank01.setName('KB')
bank01.setTotal('12334.33')
print(bank01.getTotal())
# print(bank01.getName())
print(bank01)
