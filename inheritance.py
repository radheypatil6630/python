class RBI :
    
    

    def __init__(self,amount,name,rate=5):

        self.amount=amount
        self.name=name
        self.rate=rate
        print("parent class ",name," ",amount," ",rate)
        

    def deposit(self):
        deposit_amount=int(input("enter deposit amount :"))
        amount=self.amount+deposit_amount

    def interestRate(self):
        amount=amount+(amount//rate)
        print("interest rate added to amount")

    def totalAmount(self):
        print("current balance is  :",self.amount)

    def __del__(self):
        print("destructor called ")
        
        
        

class BOI(RBI):
    
    def __init__(self,amount,name,rate,acc_no):
        
        super().__init__(amount,name,rate)
        self.acc_no=acc_no
        print(name," ",amount," ",rate)
        

    def deposit(self,acc_no,amount):
        deposit_amount=int(input("enter deposit amount in BOB :"))
        amount=amount+deposit_amount

  
    def totalAmount(self,amount):
        print("current balance is in BOB :",self.amount)

        

class BOB(RBI):

    def __init__(self,amount,name,rate):
        super().__init__(amount,name,rate)
    

   
        
        
            
  


name=input("Enter name :")
amount=int(input("Enter amount :"))
rate=int(input("Enter interest between 1 to 10 :"))


bob_obj=BOB(amount,name,rate)
#bob_obj.deposit()
#bob_obj.totalAmount(amount)

bob_obj.deposit()
bob_obj.totalAmount()

obj=BOI(amount,name,rate,"23131")
obj.deposit("23131",amount)
obj.totalAmount(amount)
