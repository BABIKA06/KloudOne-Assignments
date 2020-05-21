''' To find armstrong number or not'''

num=int(input("enter a number:"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if num==sum:
        print("armstrong number")
else: print("not armstrong number")
