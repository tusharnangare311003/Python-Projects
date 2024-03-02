import random
indi=True
num = input("Enter a number b/w 1 to 100 :")
while indi:
    if num.isdigit():
        print("\nLets play")
        indi=False
    else:
        num=input("\nInvalid Input !  \n\nTry again ! :")
num=int(num)    
rando=random.randint(1,100)
if(num==rando):
    print("Congratulations !! , Your Guess Is absolutely right !")
elif(num>rando):
    print("Your Guess is Wrong")
    print("You are away from  number by :",num-rando,".")
else:
     print("Your Guess is Wrong")
     print("You are away from  number by :",rando-num)

if(num!=rando):
    count=1
    for i in range(20):
        print("Try Again !!")
        num=int(input("Enter a number"))
        count+=1
        if(num==rando):
            print("Congratulations !! , Your Guess Is absolutely right !")
            break
        elif(num>rando):
            print("You are away from  number by ",num-rando,".")
        else:
            print("You are away from  number by ",rando-num)
        



