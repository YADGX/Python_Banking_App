#   PSEUDOCODE HERE
# -
# -
# -
# -
# -
# -
# -



import csv

class Bank_System():
    def __init__(self, name, cheacking_account = [], savings_account = [], balance = 0):
        with open('./../bank.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row)
        self.name = name
        self.cheacking_account = cheacking_account
        self.savings_account = savings_account
        self.balance = balance
         

    def add_new_customer(self):
        self.name = input('Enter your name: ').lower()
        inp = input('Do you have a cheacking account? ').lower()
        inp2 = input('Do you have a savings account? ').lower()
        if inp == 'yes':
            self.cheacking_account.append(self.name)
        else:
            print('You do not have a cheacking account')
        if inp2 == 'yes':
            self.savings_account.append(self.name)
        else:
            print('You do not have a savings account')
        
        with open('./../bank.csv', 'a', newline='') as file:
            feidnames = ['Name', 'Cheacking Account', 'Savings Account']
            writer = csv.DictWriter(file, fieldnames=feidnames)
            headers = writer.fieldnames()
            if not headers:
                writer.writeheader()
        return self.name, self.cheacking_account, self.savings_account
        
        
        
        
    def withdraw_money(self, balance):
        self.balance = balance
        inp = input('How much would you like to withdraw? ')
        self.balance -= int(inp)
        with open('bank.csv', 'a') as file:
            file = csv.writer(file)
            file.writerow([self.balance])
        return self.balance
        

    def deposit_money(self, balance):
        self.balance = balance
        inp = input('How much would you like to deposit? ')
        self.balance += int(inp)
        with open('bank.csv', 'a') as file:
            file = csv.writer(file)
            file.writerow([self.balance])
        return self.balance



    def transfer_money(self):
        inp = input('How much would you like to transfer? ')
        inp2 = input('What account would you like to transfer to? ')
        if inp2 == 'cheacking account':
            self.cheacking_account += int(inp)
        else:
            self.savings_account += int(inp)
        return self.cheacking_account, self.savings_account
    
    def check_balance(self):
        inp = input('What account would you like to check the balance of? ')
        if inp == 'cheacking account':
            print(self.cheacking_account)
        else:
            print(self.savings_account)
        
       

    


    def overdraft():
        pass
    

Bank_System('name').add_new_customer()
Bank_System('name').withdraw_money(100)
Bank_System('name').deposit_money(100)