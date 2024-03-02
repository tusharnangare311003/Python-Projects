a=int(input("Enter How Many Number You Want To Enter : "))
mylist=[]
for i in range (0,a):
    b=int(input("Enter Number "+str(i+1)+" : "))
    mylist.append(b)
print("\n1.Maximum Number In list")
print("2.Minmum Number In list")
print("3.Length Of List")
print("4.Sum Of Numbers")
print("5.Average Of Numbers")
ch=int(input("\nWhat You Want To Find :"))
if(ch==1):
    print("\nMaximum Number In list :",max(mylist))
elif(ch==2):
   print("\nMinmum Number In list :",min(mylist))
elif(ch==3):
    print("\nLength Of List :",len(mylist))   
elif(ch==4):
     print("\nSum Of Numbers :",sum(mylist))    
elif ch==5 :
     print("\nAverage Of Numbers :",sum(mylist)/a)     
else:
       print("\nInvalid Index")     
       
           