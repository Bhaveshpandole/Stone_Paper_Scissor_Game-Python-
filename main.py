#random is a Builtin module
import random

#random.choice is a method to choose random number any of this list[  ,  ,  ]
computer = random.choice([1,-1,0])

#you take input from user
you = input("Please choose only \n Stone(-1) : s \n Paper(1) : p \n Scissor(0) : c \n Enter your choice here: ")

#youDict is a Dictionary to store keypairs
youDict = {"s":1, "p":-1, "c":0}

younum = youDict[you]

#Statement print to user understanding
print("You choose: ",you)
print("The computer choose: ",computer)

#Conditional expression
if(computer == younum):
    print("Its draw")

elif(computer == 1 and younum == -1):
    print("You Win")

elif(computer == 1 and younum == 0):
    print("You lose")

elif(computer == -1 and younum == 1):
    print("You lose")

elif(computer == -1 and younum == 0):
    print("You Win")

elif(computer == 0 and younum == 1):
    print("You Win")

elif(computer == 0 and younum == -1):
    print("You lose")

else:
    print("Something went wrong!")
