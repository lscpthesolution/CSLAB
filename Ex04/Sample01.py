# ageList = list()
# for each in range(5):
#     age = input("Enter your age : ")
#     ageList.append(age)



# for each in ageList:
#     print(int(each)+10)








ageList = ['11', '55', '22', '33', '44']
def addTen(givenList : list) -> list:
    result = list()
    for each in ageList:
        result.append(int(each)+ 10)

    return result

print(addTen(ageList))