from tkinter import *
import random
def roll():
    No=random.randint(1,6)
    if No==1:
        dice.configure(text="⚀")
    elif No==2 :
        dice.configure(text="⚁")
    elif No==3:
        dice.configure(text="⚂")
    elif No==4:
        dice.configure(text="⚃")
    elif No==5:
        dice.configure(text="⚄")
    elif No==6:
        dice.configure(text="⚅")
         
    
a_root= Tk()

# Width x Height
a_root.title('Roll the Dice')
a_root.geometry("400x550")
L1 = Label(text="\nWelcome to",font ="comicsansms 20 bold")
L1.pack()
L2 = Label(text="Rolling Dice !",font ="comicsansms 30 bold")
L2.pack()

#Dice image
dice=Label(text="🎲",font ="comicsansms 220 bold",fg="blue")
dice.pack()

#Button
button=Button(text="Roll the Dice",bg= "red",fg='white',font ="comicsansms 20 bold",command=roll)
button.pack()

#Made by
pe1= Label(text='\n\nMade by Tushar Nangare J2',font="comicsansms 10 underline bold")
pe1.pack()
a_root.mainloop()
