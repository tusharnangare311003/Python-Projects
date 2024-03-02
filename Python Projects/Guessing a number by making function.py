#Guessing a number by making function
import random
def Guess():
    num=int(input("Enter a number"))
    if(num==rando):
        print("Congratulations !! , Your Guess Is absolutely right !")
    elif(num>rando):
        print("Your Guess Is Wrong")
        print("You are away from  number by ",num-rando,".")
    else:
            print("Your Guess Is Wrong/n")
            print("You are away from  number by ",rando-num)
            return num;
            
rando=random.randint(100,999)
num=Guess()
attempts=1
if(num!=rando):
        for i in range(attempts):
            print("Try Again !!")
            Guess()
            attempt+=1

    