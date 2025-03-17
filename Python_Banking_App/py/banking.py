import csv
from random import randint
import getpass
import hashlib



############################################################################################
class Csv:
    
    def __init__(self):
        self.accounts = []
        self.load_csv()


    def load_csv(self):
        with open('./../bank.csv', 'r') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                if len(row) >= 7: # ensure all columns are present, was 6 before but changed to 7 to include the 'active' column
                    self.accounts.append({
                        'account_id': row[0],
                        'name': row[1],
                        'password': row[2], 
                        'checking_account': int(row[3]), 
                        'savings_account': int(row[4]), 
                        'overdraft_count': int(row[5]),
                        'active': row[6] == 'True' # convert string to boolean
                    })
              


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
        print("Account information saved to CSV.")


    def generate_unique_id(self):
        existing_ids = {acc['account_id'] for acc in self.accounts} # iterate over the accounts and get the account_id
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
        account_id = self.generate_unique_id()
        
        self.accounts.append({
            'account_id': account_id,
            'name': name,
            'password': password_hash,
            'checking_account': 0,
            'savings_account': 0,
            'overdraft_count': 0,
            'active': True
        })

        # while True:
        #     account_type = input("Would you like to add a Checking or Savings account? (Checking/Savings/Done): ").strip().lower()
        #     if account_type in ('checking', 'savings'):
        #         for acc in accounts:
        #             if acc['account_id'] == account_id:
        #                 if account_type == 'checking' and acc['checking_account'] == 0:
        #                     acc['checking_account'] = 0
        #                 if account_type == 'savings' and acc['savings_account'] == 0:
        #                     acc['savings_account'] = 0
        #                 break
        #     elif account_type == 'done':
        #         break
        #     else:
        #         print("Invalid choice, try again.")
        
        self.save_to_csv()
        print(f"ACEM Bank Account(s) created successfully. Your Account ID is: {account_id}")
##########################################################################################
class Transactions(User):
    
    # def perform_action(self, account):
    #     account = account
    #     while True:
    #         action = input('Would you like to Withdraw, Deposit, Transfer, or Exit? ').strip().lower()
    #         if action == 'withdraw':
    #             self.withdraw_money(account)
    #         elif action == 'deposit':
    #             self.deposit_money(account)
    #         elif action == 'transfer':
    #             self.transfer_money(account)
    #         elif action == 'exit':
    #             break
    #         else:
    #             print('Invalid action. Please try again.')


    def withdraw_money(self, account):
        if not account['active']:
            print("Account is inactive. Please deposit funds to reactivate.")
            return
        
        inp = input('From which account would you like to Withdraw Money? (Checking/Savings) ').strip().lower()
        try:
            amount = int(input('How much would you like to Withdraw? '))
        except ValueError:
            print("Invalid input.")
            return

        if amount <= 0 or amount > 100:
            print("You can only Withdraw up to 100$ at a time.")
            return
            
            
        if inp == 'checking':
            if account['checking_account'] < 0 and amount > 100:
                print("Cannot withdraw more than $100 when balance is negative.")
                return
            
            if account['checking_account'] - amount < -100:
                print("Cannot overdraft beyond -$100.")
                return
            
            account['checking_account'] -= amount
            if account['savings_account'] < 0:
                print("Overdraft detected! Applying 35$ fee...")
                account['checking_account'] -= 35
                account['overdraft_count'] += 1
                if account['overdraft_count'] >= 2:
                    print("Account deactivated due to multiple overdrafts.")
                    account['active'] = False
                    
        elif inp == 'savings':
            if account['savings_account'] >= amount:
                account['savings_account'] -= amount
            else:
                print("Insufficient funds or invalid account type.")
                return
            
        else:
            print("Invalid account type.")
            return

        self.save_to_csv()
        print(f"Withdrawal successful. Updated balances - Checking: {account['checking_account']}, Savings: {account['savings_account']}")


    def deposit_money(self, account):
        inp = input('Which Account would you like to Deposit Into? (Checking/Savings) ').strip().lower()
        try:
            amount = int(input('How much would you like to Deposit? '))
        except ValueError:
            print("Invalid input.")
            return
        
        if amount <= 0:
            print("Amount must be positive.")
            return

        if inp == 'checking':
            account['checking_account'] += amount
        elif inp == 'savings':
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
        inp1 = input('Would like to Tranfer Money between you Accounts or to another Account? (MyAccounts/Account) ').strip().lower()
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
            
            if account['checking_account'] >= amount:
                account['checking_account'] -= amount
                target['checking_account'] += amount
                self.save_to_csv()
                print("Transfer successful.")
            else:
                print("Insufficient funds.")

###########################################################################################
class BankSystem:
    
    def __init__(self):
        self.transactions = Transactions()

    # 1st function to be called
    def log_reg(self):
        while True:
            response = input('''
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
            if response == 'register':
                self.transactions.create_bank_account()
            elif response == 'login':
                account_id = input('Please enter your Account ID: ').strip()
                password = getpass.getpass('Please enter your Password: ')
                account = next((acc for acc in self.transactions.accounts if acc['account_id'] == account_id and acc['password'] == self.transactions.hash_password(password)), None)
                if account:
                    print('Login successful.')
                    while True:
                        task = input('Would like to Withdraw, Deposit, Transfer, or Exit? ').strip().lower()
                        if task == 'withdraw':
                            self.transactions.withdraw_money(account)
                        elif task == 'deposit':
                            self.transactions.deposit_money(account)
                        elif task == 'transfer':
                            self.transactions.transfer_money(account)
                        elif task == 'exit':
                            break
                        else:
                            print('Invalid option.')
                else:
                    print('Login failed.')
            elif response == 'exit':
                break
            else:
                print('Invalid option. Please try again.')
###########################################################################################

if __name__ == '__main__':
    BankSystem().log_reg()