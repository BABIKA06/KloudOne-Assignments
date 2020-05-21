class c1:
     def __init__(self):
        print("details")
        self.name=input("name:")
        self.contact=input("contact:")
        self.address=input("address:")
     def display(self):
            print("\nname:",self.name)
            print("contact:",self.contact)
            print("address:",self.address)
class c2:
     def __init__(self):
         print("AVAILABLE STOCKS")
         self.fruits=str(input("fruits(apple/orange/grapes)"))
         self.vegetables=str(input("vegetables(onion/tomato/carrot)"))
         self.chips=str(input("chips(potato/pagoda)"))
     def result(self):
         fruits=self.fruits
         vegetables=self.vegetables
         chips=self.chips
         n1=int(input(("enter number of items you want:")))
         while(n1>=1):
          n=str(input("enter item:"))
          if(n=="fruits"):
           amount=100
           print(amount)
          elif(n=="vegetables"):
             amount=50
             print(amount)
          elif(n=="chips"):
             amount=120
             print(amount)
          else:
             exit(0)

          totalamount-0
          amount=amount+totalamount
          print("your bill")
          cgst=(amount/100)*9
          sgst=(amount/100)*9
          totalamount=(amount+cgst+sgst)
          print("\ncgst=",cgst,"\nsgst=",sgst,"\ntotalamount=",totalamount)
          n1=n1-1

class c3(c1,c2):
     def __init__(self):
        c1.__init__(self)
        c2.__init__(self)
     def printresult(self):
        c1.display(self)
        c2.result(self)


resultpro=c3()
resultpro.printresult()

