# Program 3 
#Heart Rate
#Part 1)
import random as r
i=1
brady=0
tachy=0
heart_rate=[]#creating a list for collection of heart rate
heart_con=[]
for i in range(8):
    heart_rate.append(r.randrange(50,120))#generating random values and adding it to the list
print("THE HEART RATE IS : ",heart_rate)
for i in heart_rate:
    if(50<i & i>65):#checking if heart condition is bradycardia
        heart_con.append("BRADYCARDIA")
        brady+=1#counting no of times of  bradycardia
    elif(i>100):
        heart_con.append("TACHYCARDIA")#checking if heart condition is tachycardia
        tachy+=1#counting no of times of  tachycardia
    else:
        heart_con.append("NORMAL")#checking if heart condition is normal
print(heart_con)
if(brady>=3 or tachy>=3):#checking if bradycardia or tachycardia is there three times
    print("YOU ARE AT RISK")#output if patient is at risk
else:
    print("YOU ARE NORMAL")#output if patient is normal
max_heart_rate=max(heart_rate)#using max function to get maximum value
min_heart_rate=min(heart_rate)#using min function to get minimum value
print("THE MAXIMUM HEART RATE IS : ",max_heart_rate)#outputing the values
print("THE MINIMUM HEART RATE IS : ",min_heart_rate)