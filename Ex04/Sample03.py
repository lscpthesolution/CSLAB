class Bank:
    def __init__(self, money: float) -> None:
        self.__total = money

    def setTotal(self, newTotal : float) -> None:
        self.__total = newTotal

    def getTotal(self) -> float:
        return self.__total
    
woori = Bank(999999)
print(woori.getTotal())
woori.setTotal(777777)
print(woori.getTotal())
print(woori)