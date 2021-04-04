n=int(input("Enter the Four Digit Number"))#inputing four digit number 
dig1=n%10#removing individual digit
rem1=n//10#the number after digit is removed
print("The digit is :",dig1,"The remaining number after removal",rem1)#display digit 1
sum=dig1
dig2=rem1%10#removing individual digit
rem2=rem1//10#the number after digit is removed
print("The digit is :",dig2,"The remaining number after removal",rem2)#display digit 2
sum=dig1+dig2
dig3=rem2%10#removing individual digit
rem3=rem2//10#the number after digit is removed
print("The digit is :",dig3,"The remaining number after removal",rem3)#display digit 3
sum=dig1+dig2+dig3
dig4=rem3%10#removing individual digit
rem4=rem3//10#the number after digit is removed
print("The digit is :",dig4,"The remaining number after removal",rem4)#display digit 4
sum=dig1+dig2+dig3+dig4#sum of digits
print("The sum of the digits",sum)#printing sum
