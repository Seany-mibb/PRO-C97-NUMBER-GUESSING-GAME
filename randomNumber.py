import random
randomNumber = random.randrange(1,9)
chances = 0
print("Please enter a number between 1-9. You only have 3 chances, Take a Big 😵😵😵😵😵😵😵")
while chances < 5:
    print("This is your try number: " + str(chances + 1))
    guess = int(input())
    chances += 1
    if(guess < randomNumber):
            print("The number is bigger!")
    elif(guess > randomNumber):
            print("The number is smaller!")
    else:
        print("You won!")
        break
    