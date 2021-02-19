class factorial:

    def fact(self,number):
      for i in range(1,number+1): 
        fact = fact * i 
      
print ("The factorial of 23 is : ",end="") 
print (fact) 


fac=factorial()
fac.fact(num)