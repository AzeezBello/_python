# Python program to create Bankaccount class 
# with deposit, withdraw function 

import ast
# import connect

class User():

    def __init__(self, username = 'general'):
 
        self.username = username.lower()
        self.accounts = Storage(self).read()
        

    def create_account(self):

        firstname = input('Please enter Firstname : ')
        lastname = input('Please enter Lastname :')
        gender = input('Please enter Gender :-----> [M/F]')
        phone_number = input('Please enter Phone number :')
        account_type = input('Please enter Account Type :')
        customer_email = input('Please enter your Email :')
        customer_password = input('Please enter a default password :')
        new_account = Bankaccount(firstname, lastname, gender, phone_number, account_type, customer_email, customer_password)
        storage_object = Storage(self)
        storage_object.save(new_account)

    def login(self):
        # username = input('Please enter your username :')
        # customer_password = input('Please enter your password :')
        accounts = Storage(self).read()
        print(accounts)
       
        # try:
        #     print(accounts[username])
        #     if accounts[username][customer_password] == customer_password:
        #         print("logged in")

        # except:
        #     print("incorect authentication data")

        # return

  

class Bankaccount(): 
    def __init__(self, firstname = 'empty', lastname = 'empty', gender = 'empty', phone_number = 'empty', account_type = 'empty', customer_email = 'empty', customer_password = 'empty'): 
        self.balance=0
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.phone_number = phone_number
        self.account_type = account_type
        self.customer_email = customer_email
        self.customer_password = customer_password
        
        print("Hello!!!Welcome to Deposit&Withdrawl Machine") 
  
    def deposit(self): 
        amount=float(input("Enter amount to be Deposited: ")) 
        self.balance += amount 
        print("\n Amount Deposited:",amount) 
  
    def withdraw(self): 
        amount = float(input("Enter amount to be Withdrawed: ")) 
        if self.balance>=amount: 
            self.balance-=amount 
            print("\n You Withdrawed:", amount) 
        else: 
            print("\n Insufficient balance  ") 

    def transfer(self):

        pass

    def view_profile(self):

        pass

    def close_account(self):

        pass
  
    def display(self): 
        print("\n Net Available Balance=",self.balance) 



class Storage():
    
    def __init__(self, user):
        self.user = user

    def save(self, new_account):
        account = {}
        data = self.__read_all()
        reg_users = list(data.keys())
        # account = [new_account.firstname, new_account.lastname, new_account.gender, new_account.phone_number, new_account.account_type, new_account.customer_email, new_account.customer_password]
        account [new_account.username] = {'firstname':new_account.firstname, 'lastname': new_account.lastname, 'gender':new_account.gender, 'phone_number':new_account.phone_number, 'account_type': new_account.account_type, 'customer_email': new_account.customer_email,'customer_password': new_account.customer_password }
        print(account)

        if self.user.username in reg_users: #check if user exists
            data[self.user.username].append(account)

        else:

            data[self.user.username] = []
            data[self.user.username].append(account)

        with open('bank.txt', 'w') as file:
            file.writelines(str(data)) 
            file.close()

    
    def __read_all(self):
        with open('bank.txt', 'r') as file:
            data = file.read() 

            file.close()

            return {} if len(data)<1 else ast.literal_eval(data) 
    
    def read(self):
        with open('bank.txt', 'r') as file:
            data = file.read() 

            file.close()
            try: 
                return {} if len(data)<1 else ast.literal_eval(data)[self.user.username]
            except: 
                return [['NONE','NO BANK DATA YET']]
  
# Driver code 

# creating an object of class 
s = User()

# Calling functions with that class object 
s.login()
# s.create_account()

# k = Bankaccount(s)
# k.deposit() 
# k.withdraw() 
# k.display() 