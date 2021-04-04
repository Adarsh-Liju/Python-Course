#Program 1 a)
f1=0#assigning the values
f2=1
s=0
n=int(input("Enter the number of terms"))#inputing the value
if(n==1):
    print(f1)
elif(n==2):
    print(f1,end="  ")
    print(f2,end="  ")  
elif(n>2):
    print(f1,end="  ")
    print(f2,end="  ")
    for i in range(n-2):#adding the two variables
        s=f1+f2
        print(s,end="  ")
        f1=f2
        f2=s


