'''Experiment No 3:

To accept from the user the number of Fibonacci numbers to be generated and print the Fibonacci series.'''

a=int(input("Enter how many terms of Fibonacci Series you want:"))
n1=0
n2=1
print(n1)
print(n2)
for i in range(1,a-1):
    n3=n1+n2
    print(n3)
    n1,n2=n2,n3
    
print()    
print (a,"terms of Fibonacci Series")    