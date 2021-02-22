# Index and key error
try:
    ages = {'Jim': 30, 'Pam': 28, 'Kevin': 33}
    ages['Michael']
    

except KeyError:
    print("Key Error")