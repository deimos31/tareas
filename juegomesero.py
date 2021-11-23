import os
import secrets
os.system("clear")
print(" __________________________________________")
print("|                                          |")
print("|           ¿WHOS GONNA PAY?               |")
print("|__________________________________________|")
print("                                            ")
print("                                            ")
print("                                            ")
names_list= input("Write the names of the players (separated by ','): ").lower()
names = names_list.split(",")
print(names)
list_complete = False 
ask=input("Is the list complete? (Yes/No):  ").lower()

if ask == "yes":
    list_complete = True
    os.system("clear")
    print("The name selected is: ",secrets.choice(names))
elif not list_complete:
    new_list= input ("Write the names you forgot: ").lower()
    new_names= new_list.split(",")
    the_list= names + new_names
    print(the_list)
    print("The name selected is: ", secrets.choice(the_list))




