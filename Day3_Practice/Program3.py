# Account details - comprehension
accDetails=[("Guido", 2000, 500), ("Raymond", -52, 1000),
 ("Jack", 900, 1000), ("Brandon", 2000, 0)]

# disc comprehension     
dcomp={cus[0]:cus[1] for cus in accDetails if cus[1] > cus[2]}
print(dcomp) 

# set comprehension
scomp={cus[1] for cus in accDetails}
print(scomp)
    
# List comprehension
lcomp=[cus[0] for cus in accDetails]
print(lcomp)
    
#disc comprehension
minCus={cus[0]:(cus[2]- cus[1]) for cus in accDetails}
cusList={k:v for k,v in minCus.items() if v > 0}
print(minCus)
print(cusList)

#tuple comprehension
tcomp=[(cus[0],cus[1]) for cus in accDetails if cus[1] > 0]
print(tcomp)