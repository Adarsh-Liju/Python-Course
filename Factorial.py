fac=1
a=int(input("Enter a number"))#inputing the number
if(a==0 or a==1):#if number is one or two
    print("The factorial for 1 and 0 is : ",fac)
else:
    for i in range(1,a+1):#passing through the range
         fac=fac*i#multiplyin and storing it in a value
print("The Factorial for ",a,"is : ",fac)#outputing the value
