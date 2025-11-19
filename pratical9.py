class Bank:
    def __init__(self, name):
        self.name = name
        print(f"Bank '{self.name}' created")
    
    def __del__(self):
        print(f"Bank '{self.name}' closed")

class Account(Bank):
    def __init__(self, name, acc_number):
        super().__init__(name)
        self.acc_number = acc_number
        print(f"Account {self.acc_number} created in bank '{self.name}'")
    
    def __del__(self):
        print(f"Account {self.acc_number} closed")
        super().__del__()

class Loan:
    def __init__(self, loan_amount):
        self.loan_amount = loan_amount
        print(f"Loan of {self.loan_amount} issued")
    
    def __del__(self):
        print(f"Loan of {self.loan_amount} settled")

class Customer(Account, Loan):
    def __init__(self, name, acc_number, loan_amount, customer_name):
        Account.__init__(self, name, acc_number)
        Loan.__init__(self, loan_amount)
        self.customer_name = customer_name
        print(f"Customer '{self.customer_name}' associated with Account {self.acc_number} and Loan {self.loan_amount}")
    
    def __del__(self):
        print(f"Customer '{self.customer_name}' relationship ended")
        super().__del__()
        Loan.__del__(self)

customer = Customer("ABC Bank", 12345, 50000, "John Doe")
del customer
