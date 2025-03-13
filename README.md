
# Python Banking App 
**This** app allows the user to either Create or to Login to his/her Bank Account with either a Checking or a Savings Account or both.
This app is fully functional and provides a simple Bank Account System.

Once the user opens the app he will be asked to either Login, Register or Exit

## If the user chooses to Register
- He/She will be asked to enter a unique Username with a password. <br/><br/>
- Once he/she enters the Username and Password it will be automatically stored in the CVS file. <br/><br/>
- Then he/she will be asked if he/she wants to open a Checking Account, a Savings Account, or both. <br/><br/>
- Once they are finished the system will output ***Account information saved to CSV.*** and ***Bank account(s) created successfully. Your Account ID is: ID***  which they will need when they Login. <br/><be/>

## If the user chooses to Login
1- The app will ask him to enter his Account ID and his/her Password (The password will be hidden due to the use of 'getpass' function)
2- Once he logs in he will have the choice of either withdrawing, Deposit, Transfer or Exit.
#If the user chooses to  Withdraw#
1- He will be asked from which account he would like to Withdraw his money. (Either Chacking or Savings Account)
2- Then he will be asked to enter the amount of money he would like to withdraw and it must be available in his balance.

## If he chooses Deposit
1- He will be asked from which account he would like to Deposit his money (Either Chacking or Savings Accoount).
2- Then he will be asked to input the amount of money he would like to Deposit in.
#If he chooses Transfer#
1- He woould asked to which account he would like to Transfer his money too. (Either Chacking or Savings Accoount)
2- Then he will be asked to input the amount of money he would like to Transfer to.

##If the user chooses Exit##
The App will end and he will be kicked out.
