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
        self.password = []
        self.name = []
        self.account_id = []
        self.checking_account = []
        self.savings_account = []
        self.balance = []
    
    
        with open('./../bank.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row)
    
    def generate_unique_id(self):
        while True:
            new_id = randint(10006, 11000)
            if new_id not in self.account_id:
                return new_id
                 
    def create_bank_account(self):
        if input('Would you like to create a Bank Account? ').lower() == 'yes':
            name = input('Please enter a name: ')
            password = getpass.getpass('Please enter a password: ')
            account_id = self.generate_unique_id()
            self.name.append(name)
            self.password.append(password)
            self.account_id.append(account_id)
            self.balance.append(0)
            
            print(f"Bank account created successfully. Your Account ID is: {account_id}")
            self.save_to_csv()
        else:
            print('Account Creation Cancelled')
    
    
    def ckecking_saving_account(self):
        if input('Would you like to create a Checking Account? ').lower() == 'yes':
            username = input('Please enter a Username: ').lower()
            if username not in self.checking_account:
                password = getpass.getpass('Please enter a Password: ')
                self.checking_account.append(username)
                self.password.append(password)
                print('Checking Account Created Successfully')
            else:
                print('This name is already in use')
        
       
        if input('Would you like to create a Savings Account? ').lower() == 'yes':
            username = input('Please enter a Username: ').lower()
            if username not in self.savings_account:
                password = getpass.getpass('Please enter a Password: ')
                self.savings_account.append(username)
                self.password.append(password)
                print('Savings Account Created Successfully')
            else:
                print('This name is already in use')
                
        self.save_to_csv()
        return self.checking_account, self.savings_account, self.password
    
    def save_to_csv(self):
        with open('./../bank.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                self.account_id,
                self.name,
                self.password,
                self.checking_account,
                self.savings_account,
                self.balance
            ])
        print("Account information saved to CSV.")
        
 
 
 
       
# class login(User):
#     def __init__(self, account_id, name = [],cheacking_account = [], savings_account = [], balance = 0, check_password = [], save_password = []):
#         super().__init__(account_id, name, cheacking_account, savings_account, balance, check_password, save_password)
        
#     def log_in(self):
#         inp = input('Do you want to log in into your Cheacking Account? ').lower()
#         signed_in = False
#         while(signed_in == False):
#             if inp == 'yes':
#                 try:
#                     inp2 = input('Please enter your Username: ').lower()
#                     inp3 = getpass.getpass('Please enter your Password: ')
#                     if inp2 in self.cheacking_account and inp3 in self.check_password:
#                         signed_in = True
#                         print('You are now logged in')
#                     else:
#                         print('Username or Password is incorrect')
#                 except:
#                     print('Username or Password is incorrect')
#             if inp == 'no':
#                 pass
            
#             inp4 = input('Do you want to log in into your Savings Account? ').lower()
#             if inp4 == 'yes':
#                 try:
#                     inp5 = input('Please enter your Username: ').lower()
#                     inp6 = getpass.getpass('Please enter your Password: ')
#                     if inp5 in self.savings_account and inp6 in self.save_password:
#                         print('You are now logged in')
#                     else:
#                         print('Username or Password is incorrect')
#                 except:
#                     print('Username or Password is incorrect')
#             if inp4 == 'no':
#                 pass
#         return self.cheacking_account, self.savings_account, self.check_password, self.save_password
    
    
#     def account_idinity(self):
#         ins = randint(10006, 11000)
#         idlist = []
#         if ins not in idlist:
#             idlist.append(ins)
#         with open('bank.csv', 'a') as file:
#             file = csv.writer(file)
#             file.writerow([ins])
#         return idlist
    
# # User('name').add_new_customer()
# # User('name').log_in()


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