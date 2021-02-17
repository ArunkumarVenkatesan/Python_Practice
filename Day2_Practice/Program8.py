def arg(*args,**kwargs):
 print(len(args) + len(kwargs))
 argCount=0
 kwargsCount=0
 for i in args:
   argCount=argCount+1
 print(f"print argument count: {argCount} ")

 for x in kwargs:
   kwargsCount=kwargsCount+1

 print(f"print argument count: {kwargsCount} ")

arg('arg1','arg2',name='ford',model='1998',make='Honda')