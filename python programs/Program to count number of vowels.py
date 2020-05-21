'''count number vowels in sentence'''

n=input("enter the sentence you want:")
count=0
for i in n:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        count=count + 1
print("vowels in sentence:",count)  
