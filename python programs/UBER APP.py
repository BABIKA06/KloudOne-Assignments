print("Sign-in form")
n=str(input(print("name:")))
m=str(input(print("mailid:")))
c=int(input(print("contact:")))
print("Thank you for downloding the UBER app…")
print("Successfully completed")
print("*****************")
print("searching for a cab or auto")
print("******************")
s=str(input("i am here:"))
d1=str(input("drop:"))
d=float(input("distance:"))
t=int(input("time:"))
print("available auto/cab....")
print("1.UBER AUTO(per km=1.00INR)")
print(("2.UBER MINI(per km=2.50INR"))
print("3.UBER PRIME(per km=4.50INR)")
start1=1.00
start2=2.50
start3=4.50
speed=d/t
if d<=10:
 amount1=(d*0.7)+start1
 amount2=(d*0.7)+start2
 amount3 = (d * 0.7) + start3
 print("distance:",d)
 print("your amount for UBER AUTO:",amount1,"INR")
 print("your amount for UBER MINI:", amount2,"INR")
 print("your amount for UBER PRIME:", amount3,"INR")
 print("speed:",speed,"inches/minute")
elif d>10:
  amount1=((d-10)*30)+8.20
  amount2=((d-10)*30)+10.00
  amount3= ((d - 10) * 30) + 12.00
  print("distance:",d)
  print("your amount for UBER AUTO:",amount1,"INR")
  print("your amount for OLA MINI:", amount2,"INR")
  print("your amount for OLA PRIME:", amount3,"INR")
  print("speed",speed,"inches/minute")
else:
    exit(0)

enter=str(input("if the amount is stastify enter(yes/no)"))
if(enter=="yes"):
    print("welcome")
    print("you OTP:3456")
    print("car number:TN2345")
    print("Contact number:9865345678")
else: exit(0)
