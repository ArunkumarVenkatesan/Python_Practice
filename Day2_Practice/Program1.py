numbers = []
for i in range(3):
    guessNumber = int(input("Guess number: "))
    print(guessNumber)
    default=50
    if guessNumber < default:
        print(f"{guessNumber} is lessor than default value")
    else:
        print(f"{guessNumber} is greater than default value")    
    numbers.append(guessNumber)
    #print(numbers)