import random
# ------- Introduction -------
print("Welcome to Xavier's Ultimate Banking ChatBot")
name = input("What is your name? ")
age = int(input(f"Hello {name}, how old are you? "))
print('How can I assist you?')
# ------- Defining functions -------
usedAccounts = []
accounts = [{"accountNumber": "1024", "accountType": "savings", "balance": 10000},
            {"accountNumber": "1435", "accountType": "savings", "balance": 0}]
def addAccount():
    while True:
        accountChoice = str.lower(input("What type of account would you like to open?(savings or checking): "))
        if accountChoice == "savings" or accountChoice == "checking":
            break
        else:
            print("Please choose either 'savings' or 'checking'")
    while True:
        accountNum = str(random.randint(1000, 9999))
        if accountNum not in usedAccounts:
            break
    usedAccounts.append(accountNum)
    accounts.append({"accountNumber": accountNum, "accountType": accountChoice, "balance": 0})
    print(f"your new account number is {accountNum}, don't forget it!")

def viewAccount():
    account = input("Enter account number: ")
    for i, acct in enumerate(accounts):
        if acct["accountNumber"] == account:
            print(acct)
        elif i >= len(accounts)-1:
            print("account with that number not found\n")

def depositMoney():
    account = input("Enter account number: ")
    for i, acct in enumerate(accounts):
        if acct["accountNumber"] == account:
            deposit = int(input("how much money would you like to deposit? "))
            accounts[i]["balance"] += deposit
            print(f"Your new balance is {accounts[i]["balance"]}")
            print(accounts[i]["balance"])
        elif i >= len(accounts)-1:
            print("account with that number not found\n")

def withdrawMoney():
    account = input("Enter account number: ")
    for i, acct in enumerate(accounts):
        if acct["accountNumber"] == account:
            while True:
                withdraw = int(input("how much money would you like to withdraw? "))
                if accounts[i]["balance"] >= withdraw:
                    break
                elif accounts[i]["balance"] < withdraw:
                    print("You're not that rich!")
            accounts[i]["balance"] -= withdraw
            print(f"Your new balance is {accounts[i]["balance"]}")
        elif i >= len(accounts)-1:
            print("account with that number not found\n")


        

# ------- Bank function -------
while True:
    print("1. Open an account\n2. Display account details\n3. Deposit Money\n4. Withdraw money\n5. Exit")
    selection = int(input("Please select a number: "))
    if selection == 1:
        addAccount()
    if selection == 2:
        viewAccount()
    if selection == 3:
        depositMoney()
    if selection == 4:
        withdrawMoney()
    if selection == 5:
        print("Farewell!")
        break