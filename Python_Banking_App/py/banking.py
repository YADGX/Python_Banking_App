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
    def __init__(self, name, cheacking_account = [], savings_account = [], active_account = [], balance = 0):
        self.name = name
        self.cheacking_account = cheacking_account
        self.savings_account = savings_account
        self.balance = balance
        with open('bank.csv', 'r') as file:
            file = csv.reader(file)
            for row in file:
                print(row)

    def add_new_customer(self):
        self.name = input('Enter your name: ')
        inp = input('Do you have a cheacking account? ')
        inp2 = input('Do you have a savings account? ')
        if inp == 'yes':
            self.cheacking_account.append(self.name)
        if inp2 == 'yes':
            self.savings_account.append(self.name)
        if inp == 'yes' and inp2 == 'yes':
            self.cheacking_account.append(self.name)
            self.savings_account.append(self.name)
        with open('bank.csv', 'a') as file:
            file = csv.writer(file)
            file.writerow([self.name, self.cheacking_account, self.savings_account])
        return self.name, self.cheacking_account, self.savings_account
        
        
        
        
    def withdraw_money(self, balance):
        self.balance = balance
        with open('bank.csv', 'a') as file:
            file = csv.writer(file)
            file.writerow([self.balance])
        return self.balance
        

    def deposit_money():
        pass


    def transfer_money():
        pass


    def overdraft():
        pass