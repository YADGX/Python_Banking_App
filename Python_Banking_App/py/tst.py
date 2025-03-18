import csv
import hashlib
import getpass
import random
#################################################################################################################################################
class Csv:
    
    def __init__(self):
        self.accounts = []
        self.load_csv()
    
    
    def load_csv(self):
        try:
            with open('./../bank.csv', 'r') as file:
                reader = csv.reader(file, delimiter=';')
                for row in reader:
                    if len(row) >= 7: # ensure all colunms are present, was 6 before but chenged to 7 to include 'active', and used column 6 for overdraft_count
                        self.accounts.append({
                            'account_id': row[0],
                            'name': row[1],
                            'password': row[2],
                            'checking_account': int(row[3]),
                            'savings_account': int(row[4]),
                            'overdraft_count': int(row[5]),
                            'active': row[6] == 'True' # convert string to boolean
                        })
        except FileNotFoundError:
            pass
    
    
    def save_to_csv(self):
        with open('./../bank.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=';') # used ' ; ' to separate the columns
            for acc in self.accounts:
                writer.writerow([
                    acc['account_id'], 
                    acc['name'], 
                    acc['password'],
                    acc['checking_account'], 
                    acc['savings_account'],
                    acc['overdraft_count'], 
                    acc['active']
                ])


    def generate_unique_id(self):
        existing_ids = {acc['account_id'] for acc in self.accounts}
        while True:
            new_id = str(random.randint(10006, 11000))
            if new_id not in existing_ids:
                return new_id
    
    
    def hash_password(self, password): # used tmo  encode and decode the password, got it from disscus.pyhton.org
        return hashlib.sha256(password.encode()).hexdigest()
#################################################################################################################################################
class User(Csv):
    
    def create_bank_account(self):
        name = input('Enter a username: ').strip()
        password = getpass.getpass('Enter a password: ')
        password_hash = self.hash_password(password)
        account_id = self.generate_unique_id()
        
        self.accounts.append({
            'account_id': account_id,
            'name': name,
            'password': password_hash,
            'checking_account': 0, # set the default value to 0
            'savings_account': 0, # set the default value to 0
            'overdraft_count': 0, # set the default value to 0
            'active': True # set the default value to True
        })
        self.save_to_csv()
        print(f"ACEM Bank Account(s) created successfully. Your Account ID is: {account_id}")
#################################################################################################################################################
class Transactions(User):
    
    def withdraw_money(self, account):
        if not account['active']: # ensure the account is active before any transaction
            print("Account is deactivated due to overdrafts. Please deposit funds to reactivate.")
            return
        
        account_type = input('From which Account would you like to Withdraw from? (Checking/Savings) ').strip().lower()
        try:
            amount = int(input('Enter amount: '))
        except ValueError:
            print("Invalid input.")
            return
        
        if amount <= 0 or amount > 100: # ensure the use can't withdraw more than $100
            print("You can only withdraw up to $100 at a time.")
            return
        
        if account_type == 'checking': # ensure the user can't withdraw more than $100 when balance is negative
            if account['checking_account'] < 0 and amount > 100:
                print("Cannot withdraw more than $100 when balance is negative.")
                return
            
            if account['checking_account'] - amount < -100: # ensure the user can't overdraft beyond -$100
                print("Cannot overdraft beyond -$100.")
                return
            
            account['checking_account'] -= amount
            if account['checking_account'] < 0:
                print("Overdraft! Charging $35 fee.")
                account['checking_account'] -= 35
                account['overdraft_count'] += 1
                if account['overdraft_count'] >= 2:
                    print("Account deactivated due to multiple overdrafts.")
                    account['active'] = False
        
        elif account_type == 'savings':
            if account['savings_account'] >= amount:
                account['savings_account'] -= amount
            else:
                print("Insufficient funds.")
                return
        
        else:
            print("Invalid account type.")
            return
        
        self.save_to_csv()
        print(f"Withdrawal successful. Updated balances - Checking: {account['checking_account']}, Savings: {account['savings_account']}")


    def deposit_money(self, account):
        account_type = input('Which Account would you like to Deposit Into? (Checking/Savings) ').strip().lower()
        try:
            amount = int(input('How much would you like to Deposit? '))
        except ValueError:
            print("Invalid input.")
            return
        
        if amount <= 0:
            print("Amount must be positive.")
            return
        
        if account_type == 'checking':
            account['checking_account'] += amount
        elif account_type == 'savings':
            account['savings_account'] += amount
        else:
            print("Invalid account type.")
            return
        
        if account['checking_account'] >= 0:
            account['overdraft_count'] = 0
            account['active'] = True
            print("Account reactivated.")
        
        self.save_to_csv()
        print(f"Deposit successful. Updated balances - Checking: {account['checking_account']}, Savings: {account['savings_account']}")


    def transfer_money(self, account):
        inp1 = input('Would like to Tranfer Money between your Accounts or to another Account? (MyAccounts/Account) ').strip().lower()
        if inp1 == 'myaccounts':
            inp = input('From which account would you like to transfer? (Checking/Savings) ').strip().lower()
            if inp == 'checking' or inp == 'savings':
                try:
                    amount = int(input('How much would you like to Transfer? '))
                except ValueError:
                    print("Invalid input.")
                    return
                
                if amount <= 0:
                    print("Amount must be positive.")
                    return
                
                if inp == 'checking' and account['savings_account'] >= amount:
                    account['savings_account'] -= amount
                    account['checking_account'] += amount
                    self.save_to_csv()
                    print("Transfer successful.")
                elif inp == 'savings' and account['checking_account'] >= amount:
                    account['checking_account'] -= amount
                    account['savings_account'] += amount
                    self.save_to_csv()
                    print("Transfer successful.")
                else:
                    print("Insufficient funds or invalid account type.")
                    return

        if inp1 == 'account':
            target_id = input("Enter recipient's account ID: ").strip()
            target = next((acc for acc in self.accounts if acc['account_id'] == target_id), None)
            if not target:
                print("Account not found.")
                return
            try:
                amount = int(input('Enter amount to transfer: '))
            except ValueError:
                print("Invalid input.")
                return
            
            if amount <= 0:
                print("Amount must be positive.")
                return
            
            inp3 = input('From which account would like to Transfer from? (Checking/Savings)')
            if inp3 == 'savings' and account['savings_account'] >= amount:
                account['savings_account'] -= amount
                target['savings_account'] += amount
                self.save_to_csv()
                print("Transfer successful.")
            elif inp3 == 'checking' and account['checking_account'] >= amount:
                account['checking_account'] -= amount
                target['checking_account'] += amount
                self.save_to_csv()
                print("Transfer successful.")
            else:
                print("Insufficient funds or wrong input.")
#################################################################################################################################################
class BankSystem:
    
    def __init__(self):
        self.transactions = Transactions()
    
    # 1st function to be called
    def start(self):
        while True:
            action = input('''
██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝
████████╗ ██████╗      █████╗  ██████╗███╗   ███╗███████╗
╚══██╔══╝██╔═══██╗    ██╔══██╗██╔════╝████╗ ████║██╔════╝
   ██║   ██║   ██║    ███████║██║     ██╔████╔██║█████╗
   ██║   ██║   ██║    ██╔══██║██║     ██║╚██╔╝██║██╔══╝
   ██║   ╚██████╔╝    ██║  ██║╚██████╗██║ ╚═╝ ██║███████╗
   ╚═╝    ╚═════╝     ╚═╝  ╚═╝ ╚═════╝╚═╝     ╚═╝╚══════╝
██████╗  █████╗ ███╗   ██╗██╗  ██╗
██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝
██████╔╝███████║██╔██╗ ██║█████╔╝
██╔══██╗██╔══██║██║╚██╗██║██╔═██╗
██████╔╝██║  ██║██║ ╚████║██║  ██╗
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝


Would you like to Login, Register, or Exit? 
''').strip().lower()
            if action == 'register':
                self.transactions.create_bank_account()
            elif action == 'login':
                account_id = input("Enter Account ID: ").strip()
                password = getpass.getpass("Enter Password: ")
                account = next((acc for acc in self.transactions.accounts if acc['account_id'] == account_id and acc['password'] == self.transactions.hash_password(password)), None)
                if account:
                    print("Login successful.")
                    while True:
                        task = input("Would you like to Withdraw, Deposit, Transfer, Logout? ").strip().lower()
                        if task == 'withdraw':
                            self.transactions.withdraw_money(account)
                        elif task == 'deposit':
                            self.transactions.deposit_money(account)
                        elif task == 'transfer':
                            self.transactions.transfer_money(account)
                        elif task == 'logout':
                            break
                        else:
                            print("Invalid option.")
                else:
                    print("Login failed.")
            elif action == 'exit':
                break
            else:
                print("Invalid input.")

if __name__ == "__main__":
    BankSystem().start()
