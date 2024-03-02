no = int(input('Enter How Many Number you want to add in List'))
list1 = []
oddlist = []
evenlist = []
for i in range (1,no+1):
    a=int(input("Enter "+str(i)+" Number"))
    list1.append(a)
    if (a%2==0):
        evenlist.append(a)
    else :
         oddlist.append(a) 
print(list1)
print(evenlist)
print(oddlist)         