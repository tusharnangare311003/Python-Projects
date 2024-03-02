import random
def roll():
    L1=["⚀","⚁","⚂","⚃","⚄","⚅"]
    print(random.choice(L1))
a = True

b = input("Do You Want To Roll The Dice(Yes/No) :")
while b.lower()=="Yes".lower():
    roll()
    b = input("Roll Again?(Yes/No)")
    
    
