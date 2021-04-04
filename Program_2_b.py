s ="bad python bad teacher bad lecture"#give string 
A_1=s.replace("bad","good")#replacing the string using replace()
B_2=s.replace("bad","good",1)#replacing the string using replace()
C_3=s.find("bad")#finding the position of 'bad' using find()
print("Replacing all occurrences of bad to good :\n",A_1)#outputing the values
print("Replacing first occurrence of bad to good :\n",B_2)
print("The position of the leftmost bad :\n",C_3)
X_1=s.index("bad")#finding the index no of 'bad'
Y_1=s.index("bad",X_1+len("bad"))#adding it with previous indexes
Z_1=s.index("bad",Y_1+len("bad"))
print("The position of the secondmost left bad :\n",Z_1)#outputing the values
print("Replacing the second bad to worst and display from that point of string and also display the whole string :")
print(s[Z_1:].replace('bad','worst',1))
print(s[:Z_1]+s[Z_1:].replace('bad','worst',1))

