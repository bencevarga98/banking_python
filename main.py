#create dictionary to store accounts 
acc_dict = dict()

#create class for accounts
class Account:
    def __init__(self, name, account_number):
        self.full_name = name
        self.acc_no = account_number
        self.balance = 0
    
    def get_data(self):
        print( self.full_name, self.acc_no, self.balance)
    
    def add(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough funds")
        else:
            self.balance -= amount
    
    def inquire(self):
        return f'Your balance is {self.balance}'
    
    def __del__(self):
        print("Object deleted")

#While loop to run the program       
while True:
    #Get user input every time to select a task to do
    task = int(input("Please enter a number (1 create, 2 add, 3 withdraw, 4 inquire, 5 delete, 6 quit"))
    
    #Quit the app by entering 6
    if task == 6:
        break

    #Creating a new account object
    elif task == 1:
        name_input = input("Please enter your name:")
        an_input = int(input("Please enter your account number:"))
        acc_dict[an_input] = Account(name_input, an_input)

    #Adding money to the account    
    elif task == 2:
        an_input = int(input("Please enter your account number:"))
        amount_input = int(input("Please enter the amount you want to add:"))
        try:
            acc_dict[an_input].add(amount_input)
        except KeyError:
            print("Make sure that the account number exists!")

    #Withdraw money from the account        
    elif task == 3:
        an_input = int(input("Please enter your account number:"))
        amount_input = int(input("Please enter the amount you want to withdraw:"))
        try:
            acc_dict[an_input].withdraw(amount_input)
        except KeyError:
            print("Make sure that the account number exists!")

    #Inquire the balance of the account    
    elif task == 4:
        an_input = int(input("Please enter your account number:"))
        try:
            print(acc_dict[an_input].inquire())
        except KeyError:
            print("Make sure that the account number exists!")

    #Delete the account object    
    elif task == 5:
        an_input = int(input("Please enter your account number:"))
        try:
            del acc_dict[an_input]
        except KeyError:
            print("Make sure that the account number exists!")
