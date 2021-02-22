# l = [1, 2, 3]
# # get an iterable
# it = iter(l)
# # get next item from the iterable
# next(it)
# # until you stop iteration
# when you see StopIteration error
# Hello Iteration class
class HelloIteration:
    """Iterator for looping over a sequence backwards."""
    def __init__(self,data):
        self.data = data
        self.count=len(data)
        print(self.count)
        self.index = 0

   # def __iter__(self):
       # return self

    def __next__(self):
       
        for d in self.data:
            if self.count < self.index:
                raise StopIteration
            print(self.data[self.index])
            self.index = self.index + 2
            

str = HelloIteration('Hello')
#it = iter(str)
print(next(str))
