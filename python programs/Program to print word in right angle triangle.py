'''to print word in right triangle'''

word=input("enter the sentence:")
print(word)
print()
for i in range( 1,len(word)+1):
    print(word[:i])
