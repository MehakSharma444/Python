import random

"""
0 -> gun
1 -> water
-1 -> snake 
"""

computer = random.choice(["s","w","g"])
youstr = input("enter your choice (s for snake , w for water , g for gun) : ")
youDict = {"s": -1,"w": 1,"g" : 0}
revDict = { -1: "Snake", 1: "Water",0:"Gun"}
if(youstr not in youDict ):
    print("Invalid choice...")
else:
    print(f"you choose {revDict[youDict[youstr]]} \nComputer choose {revDict[youDict[computer]]}")
    if (computer == youstr):
        print("It's Draw !")
    else:
        if(computer == "s" and youstr == "g"):
            print("You Win!")
        elif(computer == "s" and youstr == "w"):
            print("You Lose!")
        elif(computer == "g" and youstr == "s"):
            print("You Lose!")
        elif(computer == "g" and youstr == "w"):
            print("You Win!")
        elif(computer == "w" and youstr == "g"):
            print("You Lose!")
        else:
            print("You Win!")