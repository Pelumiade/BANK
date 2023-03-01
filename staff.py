import csv

from datetime import datetime
from customer import Customer
from log import Log, Logger
from admin import Admin

admin = Admin()
log = Log()
logger = Logger()

customer = Customer('full_name', 'phone_number', 'password', 'account_type')
class Staff:
    def __init__(self):
        self.staff_username = ''
        self.staff_password = ''
        self.status = ''

    def new_staff_login(self):
        username = input("Enter username: ").capitalize()
        with open('staffs.csv', mode='r') as staff_file:
            staff_reader = csv.reader(staff_file)
            rows = list(staff_reader)
            for row in rows:
                if row[0] == username:
                    print(f"Your password is: {row[1]}")
                    password = input("Enter password: ")
                    if row[1] == password:
                        print("Login Successful!")
                        log.log_activity(f"{username} logged in successfully")

                        # Offer to change password
                        change_password = input("Do you want to change your password? (y/n)").lower()
                        if change_password == "y":
                            new_password = input("Enter new password: ")
                            row[1] = new_password
                            # Save the new password to the CSV file
                            with open('staffs.csv', mode='w', newline='') as staff_file:
                                staff_writer = csv.writer(staff_file)
                                staff_writer.writerows(rows)
                            print("Password changed successfully!")
                            log.log_activity(f"{username} changed password successfully")
                        return True
        print("Incorrect username or password!")
        return False

    def exixting_staff_login(self):
        username = input("Enter username: ").capitalize()
        password = input("input your password:")                
        with open('staffs.csv', mode='r') as staff_file:
            staff_reader = csv.reader(staff_file)
            for row in staff_reader:
                if row[0] == username and row[1] == password and row[3] == "Suspended":
                    print("Your account is inactive. Contact admin to activate it!")    
                    return False
                elif row[0] == username and row[1] == password and row[3] == "Active":
                    print("Login Successful!")
                    log.log_activity(f"{username} logged in successfully")
                    return True
            else:
                print("Incorrect username or password!")
                return False
    
    def deposit(self):
        account_number = input("Enter account number: ")
        amount = float(input("Enter amount to deposit: "))
        #Implement deposit functionality
        with open('account.csv', mode='r') as accounts_file:
            reader = csv.DictReader(accounts_file)
            for row in reader:
                if row['account_number'] == account_number:
                    
                    customer.customer_name = row['name']
                    customer.customer_phone = row['phone']
                    customer.account_type = row['account_type']
                    customer.account_number = row['account_number']
                    customer.customer_pin = row['password']
                    customer.customer_balance = float(row['balance']) + amount
                    row['balance'] = str(customer.customer_balance)
        
        with open('log.csv', mode='a', newline='') as log_file:
            log_writer = csv.writer(log_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            log_writer.writerow([customer.account_number, customer.customer_name, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "DEPOSIT", amount])

        customer.save_to_file()
        customer.update_account_file()
        logger.log_activity(f"{customer.customer_name}made a deposit of {amount} into the account by{self.staff_username} ")
        #log.log_activity(f"{username}made a deposit of {amount} into the {customer.customer_name},{customer.account_number}")
        print(f"Deposit successful! New balance is of {customer.customer_name} is {customer.customer_balance}")
 
    
    def check_balance(self):
        account_number = input("Enter account number: ")
        with open('account.csv', mode='r') as accounts_file:
            reader = csv.DictReader(accounts_file)
            for row in reader:
                if row['account_number'] == account_number:
                    customer.customer_name = row['name']
                    customer.customer_phone = row['phone']
                    customer.account_type = row['account_type']
                    customer.account_number = row['account_number']
                    customer.customer_pin = row['password']
                    customer.customer_balance = float(row['balance'])
                    print(f"Account Name: {customer.customer_name}\nAccount Number: {customer.account_number}\nBalance: {customer.customer_balance}")
                    #log.log_activity(f"staff {username} checked the account balance of {customer.customer_name}\nAccount Number: {customer.account_number} ")
                    return
        print("Account not found.")


    def logout(self):
        self.staff_username = ""
        self.staff_password = ""
        print("Logged out successfully!")
        
    def view_log(self):
        with open('staff.log', mode='r') as log_file:
            log_reader = log_file.readlines()
            for line in log_reader:
                print(line)

        with open('staff.log', mode='a') as log_file:
            log_file.write(f"{datetime.now()}: {self.username} viewed staff log.\n")



    def display_menu(self):
        while True:
            print("\n====== Main Menu ======")
            print("1. New Staff")
            print("2. Existing Staff")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.new_staff_login()
            elif choice == "2":
                if self.exixting_staff_login():
                    print(f"Welcome {self.staff_username}!")
                    while True:
                        print("\n1. Deposit for a customer")
                        print("2. Check customer's Balance")
                        print("3. Logout")
                        sub_choice = input("Enter your choice: ")
                        if sub_choice == "1":
                            self.deposit()
                        elif sub_choice == "2":
                            self.check_balance()
                        elif sub_choice == "3":
                            print("Logout successful.")
                            break
                        else:
                            print("Invalid choice. Please try again.")
                            break
            elif choice == "3":
                print("GOODBYE!!!") 
                break   
            else:
                print("Invalid choice. Please try again.")    

            
