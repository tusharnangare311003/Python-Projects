no=int(input("Enter a number, which you want to check for Armstrong no :"))
sum=0
order=len(str(no))
copy_no=no

while(no>0):
    digit=no%10
    sum+=digit**order
    no=no//10
if(sum==copy_no):   
    print(copy_no,"is an Armstrong number")
else: 
    print(copy_no,"is not an Armstrong number")