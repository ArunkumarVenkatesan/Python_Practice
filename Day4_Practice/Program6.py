# type and Value error

try:
    a=input("enter numnber: ")
    b =int(a) + 5
    if b > a:
        raise ValueError()



except TypeError as err:
    print("Type error: {0}".format(err))
    
except ValueError:
    print("Value error: value should not equal to 5")