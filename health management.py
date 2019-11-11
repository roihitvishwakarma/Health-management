print("****Welcome to helth management program****           ")
print("     our best is rohit,rohan and harry")
def getdate():
    import datetime
    return datetime.datetime.now()
client_name=input("Enter the name of client\n")
if(client_name=="rohit"):
    print("What do you want to choose for diet press 1 or for exercise press 2\n")
    inp=input("Enter the input\n")
    if (inp=="1"):
        print("what do you want to choose press 1 for see or press 2 for update")
        inp2=input("Enter input\n")
        if(inp2=="1"):
            f=open("rohit_diet.txt")
            print(f.read())
        elif(inp2=="2"):
            print("Enter update about diet\n")
            with open("rohit_diet.txt","a") as f:
                a=f.write(input([str(getdate())])+":::"+inp2+"\n")
                print("successfully written")
        else:
            (inp2!="1") and (inp2!="2")
            print("You entered wrong argument")
    elif(inp=="2"):
        print("What do you want to choose press 1 to see or press 2 for update")
        inp3=input("enter input\n")
        if(inp3=="1"):
            f=open("rohit_exercise.txt")
            print(f.read())
        elif(inp3=="2"):
            print("Enter update about exercise\n")
            with open("rohit_exercise.txt","a") as s:
                c=s.write(input([str(getdate())])+":::"+inp3+"\n")
                print("successfully written")
    else:
        (inp!="1") and (inp!="2")
        print("you entered wrong argument")

#below code for harry  

elif(client_name=="harry"):
    print("What do you want to choose for diet press 1 or for exercise press 2\n")
    inp=input("Enter the input\n")
    if (inp=="1"):
        print("what do you want to choose press 1 for see or press 2 for update")
        inp2=input("Enter input\n")
        if(inp2=="1"):
            f=open("harry_diet.txt")
            print(f.read())
        elif(inp2=="2"):
            print("Enter update about diet\n")
            with open("harry_diet.txt","a") as f:
                a=f.write(input([str(getdate())])+":::"+inp2+"\n")
                print("successfully written")
        else:
            (inp2!="1") and (inp2!="2")
            print("You entered wrong argument")
    elif(inp=="2"):
        print("What do you want to choose press 1 to see or press 2 for update")
        inp3=input("enter input\n")
        if(inp3=="1"):
            f=open("harry_exercise.txt")
            print(f.read())
        elif(inp3=="2"):
            print("Enter update about exercise\n")
            with open("harry_exercise.txt","a") as s:
                c=s.write(input([str(getdate())])+":::"+inp3+"\n")
                print("successfully written")
    else:
        (inp!="1") and (inp!="2")
        print("you entered wrong argument")            
            
            
#below code for rohan        
    

if(client_name=="rohan"):
    print("What do you want to choose for diet press 1 or for exercise press 2\n")
    inp=input("Enter the input\n")
    if (inp=="1"):
        print("what do you want to choose press 1 for see or press 2 for update")
        inp2=input("Enter input\n")
        if(inp2=="1"):
            f=open("rohan_diet.txt")
            print(f.read())
        elif(inp2=="2"):
            print("Enter update about diet\n")
            with open("rohan_diet.txt","a") as f:
                a=f.write(input([str(getdate())])+":::"+inp2+"\n")
                print("successfully written")
        else:
            (inp2!="1") and (inp2!="2")
            print("You entered wrong argument")
    elif(inp=="2"):
        print("What do you want to choose press 1 to see or press 2 for update")
        inp3=input("enter input\n")
        if(inp3=="1"):
            f=open("rohan_exercise.txt")
            print(f.read())
        elif(inp3=="2"):
            print("Enter update about exercise\n")
            with open("rohan_exercise.txt","a") as s:
                c=s.write(input([str(getdate())])+":::"+inp3+"\n")
                print("successfully written")
    else:
        (inp!="1") and (inp!="2")
        print("you entered wrong argument")    
    
    
    
