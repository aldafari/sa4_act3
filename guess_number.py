number = 10

print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? "))
if guess == number:
    print("Congrats! You guessed the right number.")
elif guess == 0:
    print("Quiting already? The number was",number)
else:
    while guess != number and guess != 0:
        
        if guess < 10:
            print(f"Sorry! Try a higher number or enter 0 to quit.")
            guess = int(input())
        elif guess > 10:
            print(f"Sorry! Try a lower number or enter 0 to quit.")
            guess = int(input())
        elif guess == 0:
            print("Quiting already? The number was",number)
if guess==10:
    print("Congrats! You guessed the right number.")