'''To calculate using various operations'''

def add(x,y):return x+y
def sub(x,y):return x-y
def mul(x,y):return x*y
def div(x,y):return x/y
print("select operation")
print("1.addition:")
print("2.subtract:")
print("3.multiplication:")
print("4,division:")
choice=input("enter choice(1/2/3/4):")
n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
if choice== '1':print(n1,"+",n2,"=",add(n1,n2))
elif choice== '2':print(n1,"-",n2,"=",sub(n1,n2))
elif choice=='3':print(n1,"*",n2,"=",mul(n1,n2))
elif choice=='4':print(n1,"/",n2,"=",div(n1,n2))
else :print("invalid selection")
                      
