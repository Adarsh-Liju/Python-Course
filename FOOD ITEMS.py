food_lst=['pani puri','dosa','bhel puri','masala dosa','dahi puri','rava dosa','pizza topings','pizza mania']#given list of food items
pizza_s=[]#creating empty lists to store 
puri_e=[]
dosa_e=[]
for i in food_lst:#traversing the list 
    if(i.startswith("pizza")):#checking if the string starts with "pizza"
        pizza_s.append(i)#adding to the empty list 
    if(i.endswith("puri")):#checking if the string ends with "puri"
        puri_e.append(i)#adding to the empty list 
    if(i.endswith("dosa")):#checking if the string ends with "dosa"
        dosa_e.append(i)#adding to the empty list 
print("The list of strings that starts with 'pizza'",pizza_s)#outputing the values
print("The list of strings that ends with 'puri'",puri_e)
print("The list of strings that ends with 'dosa'",dosa_e)