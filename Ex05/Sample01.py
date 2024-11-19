'''
return the sum of the given two numbers
'''
def add(first : int, second : int) -> int:
    return first + second

def div(first, second) -> float:
    try :
        result = first / second
    except:
        result = "Error"
        
    return result
