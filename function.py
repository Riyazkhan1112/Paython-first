


def calculateaddition (a,b):
    profit = 1 + 2 + a + b
    return profit


print(calculateaddition(2,3))



# type hind (varible hint)
def calculateaddition (a:int,b:int) -> int:
    profit = 1 + 2 + a + b
    return profit

#args used passed the dynamic parameter 
def calculate (*args):
    print(args)


print(calculate("d",3,4))