guessNumber=int(input("Guess number: "))
default=50
if guessNumber < default:
    print(f"{guessNumber} is lessor than default value")
else:
    print(f"{guessNumber} is greater than default value")