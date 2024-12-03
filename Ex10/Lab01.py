import random
'''
You will be given a list, TARGET, which consists of alphabets from A to Z.
Some of them are lower cases while others are upper cases. 
Make a lambda function which replaces lowercases with uppercases and vice versa.
It should return its result as a list at the end. 
'''
lower = lambda:list(chr(each) for each in range(65, 91))
upper = lambda:list(chr(each) for each in range(97, 123))
lowerCase = lower()
upperCase = upper()
mix = lambda:list(lowerCase[index] if random.randint(1,2) == 1 else upperCase[index] for index in range(26))
TARGET = mix()
#print(TARGET)

