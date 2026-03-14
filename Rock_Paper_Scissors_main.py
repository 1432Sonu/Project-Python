import random
'''
Game is Rock Paper Scissors
1 for Rock 
-1 for Paper 
0 for Scissors
'''
computer = random.choice([-1,0,1])
youstr = input("Enter your choise: ")
youDict = {"r":1, "p":-1, "s":0}
reverseDict = {1: "Rock", -1:"Paper", 0:"Scissors"}

you = youDict[youstr]

# By now we have 2 number (variables), you and computer

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("Its a drew")

else:
    
    if(computer == 0 and you == 1):
        print("You Win!")     
    elif(computer == -1 and you == 0):
        print("You Win!")    
    elif(computer == 1 and you == -1):
        print("You Win!")    
    elif(computer == 1 and you == 0):
        print("You Lose!")    
    elif(computer == 0 and you == -1):
        print("You Lose!")    
    elif(computer == -1 and you == 1):
        print("You Lose!")

        
    else:
        print("Something went wrong!")    