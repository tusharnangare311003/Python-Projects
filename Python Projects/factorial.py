'''n=int(input("Enter a number"))
fact=1
while(n>0):
    fact=fact*n
    n=n-1
print(fact)  '''

n=int(input("Enter a number"))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)        