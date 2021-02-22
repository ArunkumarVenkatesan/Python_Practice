import timeit
def decorator(function):
    def wrapper(*args,**Kwargs):
        print("inner")
        startTime=timeit.default_timer()
        function(*args,**Kwargs)
        endTime=timeit.default_timer()
        print("Execution time: ", endTime - startTime)
    
    print("outer")
    return wrapper

@decorator
def function(value):
    for i in range(value):
        print(i)

function(5)