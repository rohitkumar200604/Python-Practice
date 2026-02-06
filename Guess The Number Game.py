import random


print("============================================ Number Guessing Game ===========================================")
rand_num = random.randint(0,10)
ans = True
n = 0
while ans == True:
    num = int(input("\nEnter a number between 1 to 10: "))
    if num == rand_num:
        print("\nYes, you guessed it Right!!!")
        print("Congratulations! You Won\n")
        print(f"You tried {n} times.")
        print("==============================================================================================================")
        ans = False
    else:
        print("\nNah, Guess Again...\n")
        n += 1
        ans = True