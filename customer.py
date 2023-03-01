import random
import csv
from datetime import datetime
from log import Logger
logger = Logger()

#Define the Customer class
class Customer:
    def __init__(self,full_name, phone_number, password, account_type):
        self.customer_name = full_name
        self.customer_phone = phone_number
        self.account_type = account_type
        self.account_number = ""
        self.customer_pin = password
        self.customer_balance = ""   
        self.account = []
        self.loggedin = False
   
        
    def create_account(self):
            self.customer_name = input("Enter your full name: ").capitalize()
            self.customer_phone = input("Enter your phone number: ")
            self.account_type = input("Enter type of account (enter 1 for Savings/ enter 2 for Current): ")
            self.account_number = random.randint(1000000000, 9999999999)
            self.customer_pin = input("Enter your 4-digit PIN: ")
            self.customer_balance = "0.0"
            account = {'account_number': self.account_number, 'name': self.customer_name, 'phone':self.customer_phone, 'account_type': self.account_type, 'password': self.customer_pin, 'balance': self.customer_balance}
            self.account.append(account)
            self.save_to_file()
            self.update_account_file()
            print("Account created successfully!")
            print(f"Account Number: {self.account_number}")

#LOG IN FOR EXISTING CUSTOMERS
    def login(self):
        account_number = input("Enter account number: ")
        pin = input("Enter PIN: ")
        with open('account.csv', mode='r') as accounts_file:
            reader = csv.DictReader(accounts_file)
            for row in reader:
                if row['account_number'] == account_number and row['password'] == pin:
                    self.loggedin = True
                    self.customer_name = row['name']
                    self.customer_phone = row['phone']
                    self.account_type = row['account_type']
                    self.account_number = row['account_number']
                    self.customer_pin = row['password']
                    self.customer_balance = float(row['balance'])
                    print("Log in successful!")
                    logger.log_activity(f"{self.customer_name} logged  into the account") 
                    return True       
        print("Incorrect account number or PIN!")
        return False

#TO DEPOSIT    
    def deposit(self):
            amount = float(input("Enter amount to deposit: "))
            self.customer_balance += amount
            with open('log.csv', mode='a', newline='') as log_file:
                log_writer = csv.writer(log_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                log_writer.writerow([self.account_number, self.customer_name, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "DEPOSIT", amount])
            self.save_to_file()
            self.update_account_file()
            logger.log_activity(f"{self.customer_name}made a deposit of {amount} into the account")
            print(f"Deposit successful! New balance is {self.customer_balance}")


    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        b = int(self.customer_balance)
        if amount > b:
            print("Insufficient balance!")
            return
        b -= amount
        self.customer_balance = b
        with open('log.csv', mode='a', newline='') as log_file:
            log_writer = csv.writer(log_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            log_writer.writerow([self.account_number, self.customer_name, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "WITHDRAWAL", amount])
        self.save_to_file()
        self.update_account_file()
        logger.log_activity(f"{self.customer_name } made a withdrawal of {amount} from the account")
        print(f"Withdrawal successful! New balance is ${self.customer_balance}")
        
    def save_to_file(self):
        with open('account.csv', mode='a', newline='') as accounts_file:
            fieldnames = ['account_number', 'name', 'phone', 'account_type', 'password', 'balance']
            writer = csv.DictWriter(accounts_file, fieldnames=fieldnames)
            
            for account in self.account:
                writer.writerow(account)    

#FOR UPDATE
    def update_account_file(self):
        with open('account.csv', mode='r') as accounts_file:
            reader = csv.DictReader(accounts_file)
            rows = list(reader)

        with open('account.csv', mode='w', newline='') as accounts_file:
            fieldnames = ['account_number', 'name', 'phone', 'account_type', 'password', 'balance']
            writer = csv.DictWriter(accounts_file, fieldnames=fieldnames)
            writer.writeheader()

            for row in rows:
                if row['account_number'] == str(self.account_number):
                    row['balance'] = str(self.customer_balance)
                writer.writerow(row)

                   
#FOR TRANSFER    
    def transfer(self):
        recipient_account_number = input("Enter account number to transfer to: ")
        amount = float(input("Enter amount to transfer: "))

        if amount > float(self.customer_balance):
            print("Insufficient balance!")
            return

        with open('account.csv', mode='r') as accounts_file:
            reader = csv.DictReader(accounts_file)
            rows = list(reader)

        recipient_account = None
        for row in rows:
            if row['account_number'] == recipient_account_number:
                recipient_account = row
                break

        if not recipient_account:
            print("Recipient account not found!")
            return

        # Update current customer's balance
        self.customer_balance = str(float(self.customer_balance) - amount)
        self.update_account_file()
        self.save_to_file()

        # Update recipient's balance
        recipient_balance = float(recipient_account['balance']) + amount
        recipient_account['balance'] = str(recipient_balance)

        with open('account.csv', mode='w', newline='') as accounts_file:
            fieldnames = ['account_number', 'name', 'phone', 'account_type', 'password', 'balance']
            writer = csv.DictWriter(accounts_file, fieldnames=fieldnames)
            writer.writeheader()
            for row in rows:
                if row['account_number'] == self.account_number:
                    row['balance'] = self.customer_balance
                elif row['account_number'] == recipient_account_number:
                    row['balance'] = recipient_account['balance']
                writer.writerow(row)
        logger.log_activity(f"{self.customer_name} made a transfer of ${amount} into the {recipient_account} account")
        logger.log_activity(f"{recipient_account} received  ${amount} from {self.customer_name}")
        print(f"Transfer successful! New balance is {self.customer_balance}")

 #TO VIEW BALANCE  
    def view_balance(self):
            print (f'your current account balnce is: {self.customer_balance}')
            logger.log_activity(f"{self.customer_name} check his account balance")
            return self.customer_balance


    