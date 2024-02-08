number = 10
limit = 5

print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? "))

if guess == number:
    print("Congrats! You guessed the right number.")
elif guess == 0:
    print("Quiting already? The number was",number)
else:
    while guess != number and guess != 0 and limit != 0:
        limit = limit -1 
        print(f"Sorry! try again. Or enter 0 to quit. You have",limit,"left")
        guess = int(input())
        
        if guess == number:
            print("Congrats! You guessed the right number.")
        elif guess == 0:
            print("Quiting already? The number was",number)
        

    