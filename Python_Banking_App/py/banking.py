#   PSEUDOCODE HERE
# - 
# -
# -
# -
# -
# -
# -



import csv
from random import randint
import getpass

class User:
    def __init__(self):
        self.accounts =[]
        self.password = []
        self.name = []
        self.account_id = []
        self.checking_account = []
        self.savings_account = []
        self.balance = []
        self.load_csv()
    
    def load_csv(self):
        with open('./../bank.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row)
                
                
    def save_to_csv(self):
        with open('./../bank.csv', 'a', newline='') as file:
            fieldnames = ['account_id', 'name', 'password', 'checking_account', 'savings_account', 'balance']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for i in self.accounts:
                writer.writerow(i)
        print("Account information saved to CSV.")
    
    def generate_unique_id(self):
        while True:
            new_id = randint(10006, 11000)
            if new_id not in self.account_id:
                return new_id
                 
    def create_bank_account(self):
        if input('*** Welcome To ACME Bank *** \nWould you like to create an ACME Bank Account? ').lower() == 'yes':
            name = input('Please enter a Username: ')
            password = getpass.getpass('Please enter a password: ')
            account_id = self.generate_unique_id()
            
            self.name.append(name)
            self.password.append(password)
            self.account_id.append(account_id)
            self.balance.append(0)
            
            print(f"ACME Bank account created successfully. Your Account ID is: {account_id}")
            # self.save_to_csv()
        
        else:
            print('Account Creation Cancelled')
            pass
    
    
    def ckecking_saving_account(self):
        # Checking Account
        if input('Would you like to create an ACME Checking Account? ').lower() == 'yes':
            username = input('Please enter a Username: ').lower()
            if username not in self.checking_account:
                password = getpass.getpass('Please enter a Password: ')
                self.checking_account.append(username)
                self.password.append(password)
                print('Checking Account Created Successfully')
            else:
                print('This name is already in use')
        
        # Savings Account
        if input('Would you like to create an ACME Savings Account? ').lower() == 'yes':
            username = input('Please enter a Username: ').lower()
            if username not in self.savings_account:
                password = getpass.getpass('Please enter a Password: ')
                self.savings_account.append(username)
                self.password.append(password)
                print('Savings Account Created Successfully')
            else:
                print('This name is already in use')
                
        # self.save_to_csv()
        return self.checking_account, self.savings_account, self.password
    
    
        
 
 

class login(User):
    def __init__(self):
        super().__init__()
        
    
    def authenticate(self, active_type, account_id, password):
        if active_type == 'checking':
            return self.checking_account.get(account_id) ==  password
        elif active_type == 'savings':
            return self.savings_account.get(account_id) == password
        return False
    
    
    def prompt_login(self, account_type):
        response = input(f'Would you like to login to your {account_type.capitalize()} Account? (yes/no)').strip().lower()
        if response == 'yes':
            account_id = input('Please enter your Account ID: ').strip()
            password = getpass.getpass('Please enter your Password: ')
            if self.authenticate(account_type, account_id, password):
                print(f'You are now logged in to your {account_type.capitalize()} Account')
            else:
                print('Invalid Account ID or Password')
    
    def log_in(self):
        self.prompt_login('checking')
        self.prompt_login('savings')
        
        return self.checking_account, self.savings_account
    
User().create_bank_account()
User().ckecking_saving_account()
login().log_in()



# class Withdraw(login):
#     def __init__(self, account_id, name = [],cheacking_account = [], savings_account = [], balance = 0, check_password = [], save_password = []):
#         super().__init__(account_id, name, cheacking_account, savings_account, balance, check_password, save_password)
    
    
#     def withdraw_money(self):
#         inp = input('From which account would you like to withdraw money? ').lower()
#         if inp == 'cheacking account':
#             super().log_in()
#             inp2 = input('How much would you like to withdraw? ')
#             self.balance -= int(inp2)
#         else:
#             super().log_in()
#             inp3 = input('How much would you like to withdraw? ')
#             self.balance -= int(inp3)
#         return self.balance
    
# Withdraw('name').withdraw_money()
# Withdraw('name').log_in()

        
        

#     def deposit_money(self, balance):
#         self.balance = balance
#         inp = input('How much would you like to deposit? ')
#         self.balance += int(inp)
#         with open('bank.csv', 'a') as file:
#             file = csv.writer(file)
#             file.writerow([self.balance])
#         return self.balance



#     def transfer_money(self):
#         inp = input('How much would you like to transfer? ')
#         inp2 = input('What account would you like to transfer to? ')
#         if inp2 == 'cheacking account':
#             self.cheacking_account += int(inp)
#         else:
#             self.savings_account += int(inp)
#         return self.cheacking_account, self.savings_account
    
#     def check_balance(self):
#         inp = input('What account would you like to check the balance of? ')
#         if inp == 'cheacking account':
#             print(self.cheacking_account)
#         else:
#             print(self.savings_account)
        
       

    


#     def overdraft():
#         pass
    

# Bank_System('name').add_new_customer()
# Bank_System('name').withdraw_money(100)
# Bank_System('name').deposit_money(100)