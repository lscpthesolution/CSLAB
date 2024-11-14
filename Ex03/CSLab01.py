names = ["Daeju", "Richard", "Kevin", "James", "Warren", "Hwanmin", "Donghyuk", "Taehoon", "Taeyoon", "Beomkyu", "Sieon", "Devyn", "Seoyoung", "Hayoung"]
bDays = ["05_07_06", "05_12_13", "07_08_17", "06_08_25", "06_09_27", "06_05_23", "07_10_01", "06_02_01", "06_07_05", "07_06_02", "06_03_17", "05_11_17", "06_04_03", "07_07_11"]

d = dict(zip(names, bDays))

# return a list which consists of integer lists
def helper(target : list) -> list:
    result = list()
    for each in target:
        temp = list()
        for eachNum in each.split("_"):
            temp.append(int(eachNum))
        result.append(temp)

    return result

# return a dictionary with the given lists
def makeDict(list01 : list, list02: list) -> dict:
    return dict(zip(list01, list02))

# return a list of students whose bday year is the given number
def thisMonth(target : dict, year : int) -> list:
    result = list()
    for each in target:
        if target[each][0] == year:
            result.append(each)
    return result

# find the oldest kid. Return his/her name
def finder01(target : dict) -> str:   
    pass

# find the youngeset kid. Return his/her name
def finder02(taret : dict) -> str:
    pass






###################### RUN ####################3
newDict = makeDict(names, helper(bDays))
print(newDict)
thisMonth(newDict, 5)