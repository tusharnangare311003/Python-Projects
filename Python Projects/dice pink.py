from tkinter import *
import random

def roll():
    L1=["⚀","⚁","⚂","⚃","⚄","⚅"]
    dice.configure(text=random.choice(L1))


a_root= Tk()

# Width x Height
a_root.title('Roll the Dice')
a_root.geometry("400x500")
a_root.configure(bg="skyblue")
L = Label(text="\nWelcome to",font ="comicsansms 20 bold",bg="skyblue")
L.pack()
L = Label(text="Rolling Dice !",font ="comicsansms 30 bold",bg="skyblue")
L.pack()

#Dice image
dice=Label(text="⚅",font ="comicsansms 180 bold",fg='blue',bg="skyblue")
dice.pack()

#Button
button=Button(text="Roll the Dice",bg= "red",fg='white',font ="comicsansms 20 bold",command=roll)
button.pack()

#Made by
'''L= Label(text='\n\nMade by Mr Profz',font="comicsansms 10 underline bold",bg='skyblue')
L.pack()'''
a_root.mainloop()