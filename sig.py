import time 
import sys
def main():#sets the definition of the menu
    print("- menu -")
    print("1. add nation")
    print("2. view all information")
    print("3. sort nations")
    print("4. view interesting facts")
    print("5. Quit")
    
loop=True
choice=""
nationlist=['']
statelist=[]
languagelist=[]
factslist=[]

def option1():
        print("option 1 was selected")
        time.sleep(1)
        print("create new record")
        time.sleep(1)
        
        if choice==1:
            new= input("Please enter the name of the Nation:\n")
            time.sleep(1)
            nationlist.append(new)
        
            new1= input("please enter State or Territory:\n")
            time.sleep(1)
            statelist.append(new1)
        
            new2= input("please enter the name of language:\n") 
            time.sleep(1)
            languagelist.append(new2)
            
            new3= input("please enet interesting fact about nation:\n")
            time.sleep(1)
            factslist.append(new3)
        
            print("the record that you have entered is",new,new1,new2,new3)
            
            
def option2():
    print("option 2 was selected")
    time.sleep(1)
    print("sort the list A-Z")
    time.sleep(1)
    Nations=[]
    Nations.sort()
    print(Nations)
    
def option3():
    print("option 3 was selected")
    time.sleep(1)
    print("printing the list..")
    time.sleep(1)
    print(nationlist,statelist,languagelist,factslist)
    
    
def option4():
    print("option 4 was selected")
    time.sleep(1)
    print("thank you for participating. The program will exit...")
    time.sleep(1)
    

while True:
    main()
    option=''
    try:
        option=int(input("enter your choice 1-4\n"))
    except:
        print("wrong input.Please enter a number...")
        
    if option==1:
        option1()
    
    elif option==2:
        option2()
        
    elif option==3:
        option3()
        
    elif option==4:
        option4()
        
    else:
        print("invalid option. please enter a number between 1-4")