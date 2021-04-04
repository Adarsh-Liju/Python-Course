a=int(input("Enter a Number"))#inputing value
if((a&1)==1): #checcking whether the number has LSB
    print("LSB is present")#displayed if LSB is there
    new_a=a&(a-1)#removing the LSB 
    print("The number after clearing LSB :",new_a)#printing the new value of number after clearing LSB
else:
    print("LSB is already removed")#this will be printed if lsb is already removed
