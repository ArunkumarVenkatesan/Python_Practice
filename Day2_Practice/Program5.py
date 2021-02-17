# type hints
def add(num1: int,num2:int):
    """ Add 2 numbers """
    return num1+num2

num1=int(input("Enter number1: "))
num2=int(input("Enter number2: "))
print(add(num1,num2))

# Doc string
print(add.__doc__)