print("Part 1:using a temporary variable")
a=int(input("Enter the first variable"))#input first variable
b=int(input("Enter the second variable"))#input second variable
c=a#swapping using a temp variable
a=b
b=c
print("The value of first variable is :",a,"The value of second variable :",b)#displaying output after swapping
print("Part 2:without using a temporary variable")
a=int(input("Enter the first variable"))#input first variable
b=int(input("Enter the second variable"))#input second variable
b=a+b#swapping without using a temp variable
a=b-a
b=b-a
print("The value of first variable is :",a,"The value of second variable :",b)#displaying output after swapping
