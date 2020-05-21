'''To find factorial of given number'''

n=int(input("enter number:"))
result=1
for i in range(n,0,-1):
    result=result*i
print("factorial of given number:",result)
