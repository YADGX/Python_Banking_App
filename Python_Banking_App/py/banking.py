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
import hashlib


#############################################################################################################################################################
class Csv:
    def __init__(self):
        self.accounts =[]
        self.account_id = []
        self.load_csv()
    
    def load_csv(self):
        with open('./../bank.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
                
                
    def save_to_csv(self):
        with open('./../bank.csv', 'a', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            for account in self.accounts:
                writer.writerow([
                account['account_id'],
                account['name'],
                account.get('password'),
                account.get('checking_account', ''),
                account.get('savings_account', ''),
                account.get('balance', '0')
            ])
        print("Account information saved to CSV.")
    
    def generate_unique_id(self):
        while True:
            new_id = randint(10006, 11000)
            if new_id not in self.account_id:
                self.account_id.append(new_id)
                return new_id
            
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
#############################################################################################################################################################    
class User(Csv):
    def __init__(self):
        super().__init__()
                 
    def create_bank_account(self, account_type):
        if input(f'''
                ----------------------------
                *** Welcome To ACME Bank ***
                ----------------------------
                Would you like to create an ACME {account_type.capitalize()} Account? (yes/no) 
                ''').lower() == 'yes':
            name = input(f'Please enter a Username for your {account_type} account: ').strip()
            password = getpass.getpass('Please enter a password: ')
            password_hash = self.hash_password(password)
            account_id = self.generate_unique_id()
            
            self.accounts.append({
                'account_id': str(account_id),
                'name': name,
                'password': password_hash,
                'account_type': account_type,
                'balance': '0'
            })
            
            print(f"{account_type} ACME Bank account created successfully. Your Account ID is: {account_id}")
            self.save_to_csv()
        
        else:
            print('Account Creation Cancelled')
            pass
############################################################################################################################################################# 
class Login(User):
    def __init__(self):
        super().__init__()
        
    
    def authenticate(self, account_id, password):
        password_hash = self.hash_password(password)
        for account in self.accounts:
            if account['account_id'] == account_id and account['password'] == password_hash:
                return account
        return None
    
    
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
#############################################################################################################################################################
class BankSystem:
    def __init__(self):
        self.user = User()
        self.login = Login()
    
    def log_reg(self):
        while True:
            response = input('*** Welcome To ACME Bank *** \nWould you like to Login or Register? ').strip().lower()
            if response == 'login':
                self.login.log_in()
            elif response == 'register':
                self.user.create_bank_account('checking')
                self.user.create_bank_account('savings')
            elif response == 'exit':
                print('Goodbye!')
                break
            else:
                print('Invalid response. Please try again.')

BankSystem().log_reg()
#############################################################################################################################################################
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