import random

computer = random.choice([1,-1,0])

you = input("Enter your choice: ")

youDict = {"s":1, "p":-1, "c":0}

younum = youDict[you]

print("The computer choose: ",computer)

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

    print("Please choose only \n Stone : s \n Paper : p \n Scissor : s")