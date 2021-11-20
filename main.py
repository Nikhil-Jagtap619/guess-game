import random

correct = 0
incorrect = 0
game = True
rand_num = random.randint(1,10)
print("Welcome to Guessing Game")

while game:
    ans = input("Guess number between 1 and 10 : ")
    if ans.isnumeric():
        ans = int(ans)
        if ans == rand_num:
            correct+=1
            print("you guessed it right!")
        elif ans < rand_num:
            incorrect+=1
            print("incorrect! too low")
        else:
            incorrect+=1
            print("incorrect! too high")
    elif ans.isalpha():
        if ans.lower() == "quit":
            game = False
        else:
            print("type 'quit' to exit the game \n or enter the number")
    else:
        print("Invalid Input!")


print("Thank you for playing")
print(f"your score \n correct: {correct} \n incorrect: {incorrect} \n total attempt: {correct+incorrect}")