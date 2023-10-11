class Bank_Account:
  def_init_(self):
    self.balance =0
    print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
  def deposit(self):
    amount = float(input("Enter amount to be Deposited:"))
    self.balance+=amount
    print("\n Amount Deposited:",amount)
    def withdraw(self):
      amount = float(input("Enter amount to be Withdrawn:"))
        if self.balance>=amount:
          self.balance-=amount
          print("\n You Withdrew:",amount)
        else:
          print("\n Insufficient Balance")
          def display(self):
            print("\n Net Avilable Balance=",self.balance)
            #Driver code
            # creating an object of class
            s=Bank_Account()
            #Calling functions with that calling object
            s.deposit()
              s.withdraw()
              s.display()
              
             