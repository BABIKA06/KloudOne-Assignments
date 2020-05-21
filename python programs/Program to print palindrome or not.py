'''To find palindrome or not'''

n=int(input("enter number:"))
reverse=0
temp=n
while(temp>0):
    r=temp%10
    reverse=(reverse*10)+r
    temp=temp//10
print("reverse of given number:",reverse)
if(n==reverse):
        print("palindrome")

else:
            print("is not palindrome")
