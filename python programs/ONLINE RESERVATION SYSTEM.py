print("welcome to Online Reservation System")
print("only for area chennai,arakkonam")
s=str(input("your Source:"))
d=str(input("your Destination:"))
print(s,"-",d)
if(s=="chennai" and d=="arakkonam"):
    print("Available Train is express")
    print("No Intermediate stop")
    print("Timing from 5.30pm -7.00pm")
elif(s== "arakkonam" and d=="chennai"):
    print("Available Train is express")
    print("No Intermediate stop")
    print("Timing from 4.00pm-5.30pm")
else:
    print("No Available Trains")
    exit(0)
print("************")
print("1.PNR status")
print("2.Ticket Reservation")
choice=int(input("\n Enter your choice :"))
if choice==1:
    print("waiting......")
    exit(0)
elif choice==2:
    n1=int(input("\n Enter number of ticket you want: "))
    n=n1
    amount=30
    print("******Enter your details*****")
    while(n1>=1):
     name=str(input("Name:"))
     age=int(input("Age(Greater than five):"))
     sex=str(input("Sex(male/female):"))
     n1=n1-1
     print(name,age,sex)
    print("**********************************************************")
    print("HAPPY JOURNEY")
    print("Train Number:11049")
    print("Ticket Number:7366")
    print("Boarding From:",s)
    print("To Station:",d)
    print("Amount:",amount*n)

else:
    x=0
    print("Name:",x)
    print("Age:",x)
    print("Sex:",x)
    exit(0)



