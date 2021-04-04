'''Program_2'''
'''#FORMAL LETTER
s=" Respected sir,\n I am here By enlisting all the programming languages we teach.\n Problem solving using python.\n object oriented programming with C++\n java and jee. \n R programming. \n Thanking You \n Team Programming Languages"# given string
s_new=s.split('\n')#removing \n 
for i in s_new:#passing through the string
    i=i[1:]#removing blank spaces
    print(i.capitalize())#outputing the individual strings and capitalizing it 
#MAC ADDRESS
mac_address=['00','11','23','45','67','70']#given list
print("The MAC address is : ",":".join(mac_address))# joining the strings using join() 
#FESTIVAL GREETINGS
friends_list=[' Ram',' Sita',' Raj',' Joy',' Joe',' ']#given list
print("Festival Greetings :"," Happy Festival!".join(friends_list))# joining the strings using join()'''
srn_no="PE01 PE02 PE03 PE04 PE05 PE06 PE07 PE08 PE09 PE10"
srn_no_new=srn_no.replace('PE','PESU',3)
print(srn_no_new)
search_srn=input("Enter SRN to be searched")
found_srn=srn_no.find(search_srn.upper())
if(found_srn>=0):
    print(search_srn,"is present at ",found_srn)
else:
    print("Not Found")
