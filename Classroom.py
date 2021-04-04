a,b,c=input("Enter the number of students in each class").split()#accepting values
a=int(a)#converting string to integer
b=int(b)
c=int(c)
cl_a=a//2#computing number of desks for each grp
a=a%2
cl_a+=a
cl_b=b//2
b=b%2
cl_b+=b
cl_c=c//2
c=c%2
cl_c+=c
desks=cl_a+cl_b+cl_c#sum of desks
print("Desks in Group A",cl_a)#printing desks of class a
print("Desks in Group B",cl_b)#printing desks of class b
print("Desks in Group C",cl_c)#printing desks of class c
print("Sum of Desks is : ",desks)#printing sum of desks
