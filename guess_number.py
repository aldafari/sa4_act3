number = 10

print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? "))
if guess == number:
    print("Congrats! You guessed the right number.")
elif guess == 0:
    print("Quiting already? The number was",number)
else:
    while guess != number and guess != 0:
        print(f"Sorry! try again. Or enter 0 to quit.")
        guess = int(input())
        if guess == number:
            print("Congrats! You guessed the right number.")
        elif guess == 0:
            print("Quiting already? The number was",number)
        

    