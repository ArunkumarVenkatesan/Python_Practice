names=["john","jake","jack","george","jenny","jason"]
print(names)
uniqueNames=set(names)
print(uniqueNames)
for name in names:
    if len(name) < 5 and ("e" not in name):
        print(name)