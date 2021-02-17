#Kwargs number of arguments
def arg(**args):
 count=0
 for i in enumerate(args):
     count=1+count
 print(count)

arg(name="Ford",model='1981')