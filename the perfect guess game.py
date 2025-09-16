from random import randint

computer_select = randint(1,100)
chance = 0
for i in range(1,11):
    you_select = int(input("Guess the no. : "))
    chance +=1
    if(you_select == computer_select):
        print(f"YOU GOT IT RIGHT...!\nIN {chance} GUESS")
        break
    elif (you_select > computer_select):
         print(f"Please Lower Your Guess...\n{10 - chance} CHANCE LEFT")
    elif(you_select < computer_select):
         print(f"Please Higher Your Guess...\n{10 - chance} CHANCE LEFT")
else:
    print(f"YOU LOST...! AS NUMBER IS {computer_select}")