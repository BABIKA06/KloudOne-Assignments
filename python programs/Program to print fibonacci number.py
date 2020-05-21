''' to print fibonacci number'''

n=int(input("enter number:"))
print("fibonacci of given numbers are:")
first=0
second=1
for i in range(n):
      print(first)
      temp=first
      first=second
      second=temp+second
