import csv
from random import randint
import getpass
import hashlib


accounts = []
account = None
############################################################################################
class Csv:
    
    def __init__(self):
        accounts = []
        self.load_csv()


    def load_csv(self):
        try:
            with open('./../bank.csv', 'r') as file:
                reader = csv.reader(file, delimiter=';')
                for row in reader:
                    if len(row) >= 6: # ensure all columns are present
                        try:
                            accounts.append({
                                'account_id': row[0],
                                'name': row[1],
                                'password': row[3], # used 3 becuase 2 didn't work for some reason  :}
                                'checking_account': int(row[4]) if row[4] else 0, # if row[4] is empty, set to 0
                                'savings_account': int(row[5]) if row[5] else 0 # if row[5] is empty, set to 0
                            })
                        except ValueError:
                            print(f"Skipping invalid row: {row}")
        except FileNotFoundError:
            pass  


    def save_to_csv(self):
        with open('./../bank.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=';') # used ' ; ' to separate the columns
            for acc in accounts:
                writer.writerow([
                    acc['account_id'],
                    acc['name'],
                    '',  # Placeholder for missing column
                    acc['password'],
                    acc['checking_account'],
                    acc['savings_account']
                ])
        print("Account information saved to CSV.")


    def generate_unique_id(self):
        existing_ids = {acc['account_id'] for acc in accounts} # iterate over the accounts and get the account_id
        while True:
            new_id = str(randint(10006, 11000))
            if new_id not in existing_ids:
                return new_id


    def hash_password(self, password): # encode and decode the password, got it from discuss.python.org
        return hashlib.sha256(password.encode()).hexdigest()
############################################################################################
class User(Csv):
    
    def create_bank_account(self):
        name = input('Please enter a Username: ').strip()
        password = getpass.getpass('Please enter a Password: ')
        password_hash = self.hash_password(password)
        
        existing_account = None
        for acc in accounts:
            if acc['name'] == name:
                existing_account = acc
                break  

        if existing_account:
            print("An account with this name already exists.")
            account_id = existing_account['account_id']
        else:
            account_id = self.generate_unique_id()
            accounts.append({
                'account_id': account_id,
                'name': name,
                'password': password_hash,
                'checking_account': 0,
                'savings_account': 0
            })

        while True:
            account_type = input("Would you like to add a Checking or Savings account? (Checking/Savings/Done): ").strip().lower()
            if account_type in ('checking', 'savings'):
                for acc in accounts:
                    if acc['account_id'] == account_id:
                        if account_type == 'checking' and acc['checking_account'] == 0:
                            acc['checking_account'] = 0
                        if account_type == 'savings' and acc['savings_account'] == 0:
                            acc['savings_account'] = 0
                        break
            elif account_type == 'done':
                break
            else:
                print("Invalid choice, try again.")
        
        self.save_to_csv()
        print(f"ACEM Bank Account(s) created successfully. Your Account ID is: {account_id}")
##########################################################################################
class Login(User):
    
    def authenticate(self, account_id, password):
        password_hash = self.hash_password(password)
        for account in accounts:
            if account['account_id'] == account_id and account['password'] == password_hash:
                return account
        return None


    def log_in(self):
        account_id = input('Please enter your Account ID: ').strip()
        password = getpass.getpass('Please enter your Password: ')
        return self.authenticate(account_id, password)
###########################################################################################
class Transactions(Login):
    
    def perform_action(self, account):
        account = account
        while True:
            action = input('Would you like to Withdraw, Deposit, Transfer, or Exit? ').strip().lower()
            if action == 'withdraw':
                self.withdraw_money(account)
            elif action == 'deposit':
                self.deposit_money(account)
            elif action == 'transfer':
                self.transfer_money(account)
            elif action == 'exit':
                break
            else:
                print('Invalid action. Please try again.')


    def withdraw_money(self, account):
        inp = input('From which account would you like to withdraw money? (checking/savings) ').strip().lower()
        try:
            amount = int(input('How much would you like to withdraw? '))
            if amount <= 0:
                print("Amount must be positive.")
                return
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            return

        if inp == 'checking' and account['checking_account'] >= amount:
            account['checking_account'] -= amount
        elif inp == 'savings' and account['savings_account'] >= amount:
            account['savings_account'] -= amount
        else:
            print("Insufficient funds or invalid account type.")
            return

        self.save_to_csv()
        print(f"Withdrawal successful. Updated balances - Checking: {account['checking_account']}, Savings: {account['savings_account']}")


    def deposit_money(self, account):
        inp = input('Which account would you like to deposit into? (checking/savings) ').strip().lower()
        try:
            amount = int(input('How much would you like to deposit? '))
            if amount <= 0:
                print("Amount must be positive.")
                return
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            return

        if inp == 'checking':
            account['checking_account'] += amount
        elif inp == 'savings':
            account['savings_account'] += amount
        else:
            print("Invalid account type.")
            return

        self.save_to_csv()
        print(f"Deposit successful. Updated balances - Checking: {account['checking_account']}, Savings: {account['savings_account']}")


    def transfer_money(self, account):
        inp = input('What account would you like to transfer to? (checking/savings) ').strip().lower()
        try:
            amount = int(input('How much would you like to transfer? '))
            if amount <= 0:
                print("Amount must be positive.")
                return
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            return

        if inp == 'checking' and account['savings_account'] >= amount:
            account['savings_account'] -= amount
            account['checking_account'] += amount
        elif inp == 'savings' and account['checking_account'] >= amount:
            account['checking_account'] -= amount
            account['savings_account'] += amount
        else:
            print("Insufficient funds or invalid account type.")
            return


        self.save_to_csv()
        print(f"Transfer successful. Updated balances - Checking: {account['checking_account']}, Savings: {account['savings_account']}")
###########################################################################################
class BankSystem:
    
    def __init__(self):
        self.user = User()
        self.transactions = Transactions()

    # 1st function to be called
    def log_reg(self):
        while True:
            response = input('Would you like to Login, Register, or Exit? ').strip().lower()
            if response == 'login':
                account = Login().log_in()
                if account:
                    Transactions().perform_action(account) # called the perform_action function from the Transactions class
                else:
                    print("Authentication failed.")
            elif response == 'register':
                User().create_bank_account()
            elif response == 'exit':
                print('Goodbye!')
                break
            else:
                print('Invalid response. Please try again.')


    # def overdraft(self, accounts):
    #     accounts = self.account
    #     while True:
    #         if self.transactions['checking_account'] + self.transactions['savings_account'] < 0:
    #             self.transactions['checking_account'] - 35 or self.transactions['savings_account'] - 35
    #         if self.transactions['checking_account'] + self.transactions['savings_account'] < 0:
    #             accounts['withdraw_money'] > 100 = False
    #             print("You have an overdraft on your account.")
                
    #         pass

if __name__ == '__main__':
    BankSystem().log_reg()