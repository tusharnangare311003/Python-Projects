'''n=int(input(""))
sum=0
if(n%2==0):
    for i in range(2,n+1,2):
        sum=sum+i
else:
    for i in range(2,n,2):
        sum=sum+i
print(sum) '''
    
n=int(input("Enter a number"))
sum=0
for i in range(1,n+1):
    if(i%2==0):
        sum+=i
print("Sum of n even terms",sum)        
        
    