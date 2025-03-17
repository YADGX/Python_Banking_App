
# ACME Banking App

## Project Description
**ACME**  Banking App allows the user to either Create or to Login to his/her Bank Account with either a Checking or a Savings Account or both.
This app is fully functional and provides a simple Bank Account System. which allows the user to manage their Bank Account, Users can perform transactions such as deposits, withdrawals, and transfers between checking and savings accounts.

## Used Technologies
- Python
- CSV
- 'getpass' to hide the password input
- 'hashlib' to encode and decode the password
- 'random' to generate a random Account ID

## APP Functionality
| Feature                | Description |
|------------------------|-------------|
| **Registration**  | Users can create an account with a username and password. |
| **Secure Password** | User passwords are hashed and verified upon login. |
| **Checking & Savings Accounts** | Users can maintain both checking and savings accounts. |
| **Deposits & Withdrawals** | Users can deposit into or withdraw from their accounts. |
| **Transfers** | Users can transfer money between their checking and savings accounts. |

## System Procces
### If the user chooses to Register
- He/She will be asked to enter a unique Username with a password. <br/><br/>
- Once he/she enters the Username and Password it will be automatically stored in the CVS file. <br/><br/>
- Then he/she will be asked if he/she wants to open a Checking Account, a Savings Account, or both. <br/><br/>
- Once they are finished the system will output ***Account information saved to CSV.*** and ***Bank account(s) created successfully. Your Account ID is: ID***  which they will need when they Login. <br/><be/>

### If the user chooses to Login
- The app will ask him to enter his Account ID and his/her Password (The password will be hidden due to the use of **getpass** function) <br/><br/>
- Once he logs in he will have the choice of either withdrawing, Deposit, Transfer or Exit. <br/><br/>
  
### If the user chooses to  Withdraw
- He will be asked from which account he would like to Withdraw his money. (Either Checking or Savings Account)<br/><br/>
- Then he will be asked to enter the amount of money he would like to withdraw and it must be available in his balance.<br/><br/>

### If he chooses Deposit
- He will be asked from which account he would like to Deposit his money (Either Checking or Savings account).<br/><br/>
- Then he will be asked to input the amount of money he would like to Deposit.<br/<br/>

### If he chooses to Transfer
- He would ask to which account he would like to Transfer his money to. (Either Checking or Savings Account)<br/><br/>
- Then he will be asked to input the amount of money he would like to Transfer.<br/><br/>

### If the user chooses Exit
- The App will end and he will be kicked out.<br/><br/>

## Challenges & Sulotions

### Challenges
- Make the CSV auto-update after a user input.
- Matching the user with his/her password.
- how to create the Overdraft function. (I gave up ;p)
- how to generate a unique ID.
- how to ensure account names are unique

### Solutions
- Created a ***save_to_csv** function.
- Created a ***authenticate** function to ensure they are matching.
- Created a ***unique_id*** to generate a unique ID between 10006 and 11000.
- Created a ***for loop*** to iterate through the acc['name'] and if there is it will break the loop.

## Icebox Features (Future Enhancements)
- Add overdraft function
- allows to transfer to other user accounts
- add transaction history logging

