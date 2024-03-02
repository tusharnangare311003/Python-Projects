# To check input is integer and b/w 1 to 100
def digit(a):
    indi=True
    while indi:
         if a.isdigit():
             a=int(a)
             if a<=100 and a>0:
                 print() 
                 indi=False   
             else:
                 a=input("Please Enter Number Only Between 1 to 100 : ")    
         else:
            a=input("\nInvalid Input !  \n\nTry again ! :")            
    return a

def check(a,ran1) :# To check input number is equal , greater or lower
    if (ran1 ==a) :
        print ("Congratulation You Are The Winner")
    elif(ran1<a) :
         print(f"Your Guess Is High\nYour Guess is : {a}\nActual Number is : {ran1}")
    else:
         print(f"Your Guess Is Low\nYour Guess is : {a}\nActual Number is : {ran1}")                                                            
import random  
con = True
while con : 
    rand = random.randint(1,100)

    num = input("\nEnter a number b/w 1 to 100 : ")

    num = digit(num)
    check(num,rand)
    con1 = input("\nDo You Want to Play again(Y/N) :")
    con1 = con1.upper()
    if con1 == "N":
        break      