#input all the 4 character 
ch1=input("Enter the first character : ")
ch2=input("Enter the second character : ")
ch3=input("Enter the third character : ")
ch4=input("Enter the fourth character : ")
ch1_new=chr(ord(ch1)+1)#converting its value to ascii and adding one to it 
ch2_new=chr(ord(ch2)+1)#converting the new value to character
ch3_new=chr(ord(ch3)+1)
ch4_new=chr(ord(ch4)+1)
print("The first character after incresing by 1 : ",ch1_new)#printing all the new values
print("The second character after incresing by 1 : ",ch2_new)
print("The third character after incresing by 1 : ",ch3_new)
print("The fourth character after incresing by 1 : ",ch4_new)
