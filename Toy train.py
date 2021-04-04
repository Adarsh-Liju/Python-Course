print("Enter Your Choice")
cho=int(input(" 1: Entry Ticket \n 2: Entry Ticket and Toy Train\n"))
age=int(input("Enter Your Age"))
if(cho==1):
    if(age>12):
        ent_tic=80
    if(12>=age or age<=5):
        ent_tic=40
if(cho==2):
    if(age>12):
        ent_tic=100
    if(12>=age or age<=5):
        ent_tic=50
print("Entered Choice is : ",cho)
print("Your Entry Ticket is",ent_tic)

