#Program 2
#Part A(Assigning it  to thier datatypes)
lst=[1,2,3,{'a','b','c','d'},'python','a','y','z',('p',1,'t',2),["COMP","PUTER"],3.4,7.9,2.1]#creating a hetrogenous elements
int1=[]#creating empty lists for new datatypes
ch1=[]
lst1=[]
tup1=[]
fl1=[]
for i in lst:#going through the elements
    if(type(i)==int):
        int1.append(i)#appending the integer datatype list
    elif(type(i)==str):
        ch1.append(i)#appending the string datatype list
    elif(type(i)==list):
        lst1.append(i)#appending the list datatype list
    elif(type(i)==tuple):
        tup1.append(i)#appending the tuple datatype list
    elif(type(i)==float):
        fl1.append(i)#appending the float datatype list
print("THE INTEGER DATA TYPE IS : ",int1)#outputing the results
print("THE LIST DATA TYPE IS : ",lst1)
print("THE TUPLE DATA TYPE IS : ",tup1)
print("THE STRING DATA TYPE IS : ",ch1)
print("THE FLOAT DATA TYPE IS : ",fl1)
#Part B(Ascending and Descending)
ch1.sort()#for sorting the string list
print("The STRING List in Ascending order : ",ch1)#outputing the results
ch1.sort(reverse=True)
print("The STRING List in Descending order : ",ch1)#outputing the results
int1.sort()#for sorting the integer list
print("The INTEGER List in Ascending order : ",int1)#outputing the results
int1.sort(reverse=True)
print("The INTEGER List in Descending order : ",int1)#outputing the results

