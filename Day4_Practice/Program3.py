# print python file name list in current directory
import os, fnmatch
print(os.listdir('.'))

listOfFiles = os.listdir('.')
pattern = "*.py"
for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
            print (entry)