n=int(11)
i=int(1)
print("No. of guesses is limited to 5")
print("Type 'break' to exit.")
while(i<=5):
    print("Current guess count: ",i)
    print("Enter your Guess :-)")
    guess=int(input())
    if guess<11:
        print("No. is greater than your guess.")
    elif guess==11:
        print("You have guessed the no. >.<")
        print("No. of guesses used: ",i)
        exit()
    elif guess>11:
        print("No. is smaller than your guess.")
    elif guess=="break":
        exit()
    else:
        print("Invalid input.")
    i=i+1

if i>5:
    print("Game Over!! Guessing limit reached.")
