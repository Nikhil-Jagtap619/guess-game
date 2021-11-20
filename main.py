import random

correct = 0
incorrect = 0
game = True
rand_num = random.randint(1,9)

while game:
    print("Welcome to the Guesing Game")
    ans = input("Enter your number between 1 and 10 : ")
    if ans.isnumeric():
        ans = int(ans)
        if ans == rand_num:
            correct+=1
            print("Congrats","you guessed it right!")
        elif ans < rand_num:
            incorrect+=1
            print("Warning","incorrect! too low")
        else:
            print("Warning","incorrect! too high")
    elif ans.isalpha():
        if ans.lower() == "exit":
            game = False
        else:
            print("Warning","type 'exit' to quit the game \n or enter the number")
    else:
        print("Warning","Invalid Input!")
print("Thank you for playing")
print(f"your score \n correct: {correct} \n incorrect: {incorrect} \n total attempt: {correct+incorrect}")