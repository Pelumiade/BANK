from customer import Customer
from admin import Admin
from staff import Staff
import csv
customers = []

def main():

    while True:
        print("\n*******************************")
        print("Welcome to the ATS Banking System")
        print("*******************************")

        print("1. Admin Login")
        print("2. Staff Login")
        print("3. Customer\n")

        choice = input("Select an option: ")

        if choice == "1":

            username = input("Enter admin username: ")
            password = input("Enter admin password: ")
            admin = Admin()
            login = admin.login(username, password)
            if not login:
                    print("Invalid Password or Username.")
                    break
            print("\nWelcome, Admin!")
            while True:
                print("\nPlease choose an option:")
                print("\n1. Create Staff Account")
                print("2. Suspend Staff Account")
                print("3. Reactivate Suspended Account")
                print("4. Check customers Activities")
                print("5. Check staffs Activities")
                print("6. logout")
                
                choice = input("Enter your choice (1-6): ")
                
                if choice == "1":
                    admin.create_staff()
                elif choice == "2":
                    admin.suspend_staff()
                    #staff_username = input("which customer do you want to suspend:")
                elif choice == "3":
                    admin.reactivate_staff()
                elif choice == "4":
                    admin.view_customer_activities()
                elif choice == "5":
                    admin.view_staff_activities()   
                elif choice == "6":
                    admin.logout()

                    break

                else:
                    print("Invalid choice, please try again.")

        
        elif choice == "2":
            staff = Staff()
            staff.display_menu()
       

        if choice == "3":
            customer = Customer('full_name', 'phone_number', 'password', 'account_type')
            
            with open('account.csv', mode='r') as accounts_file:
                reader = csv.DictReader(accounts_file)
                for row in reader:
                    customers.append(row)
            customer=Customer('full_name', 'phone_number', 'password', 'account_type')

            print("1. Create account")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                customer.create_account()
            elif choice == "2":
                    #customer = Customer.find_customer("fullname", "pasword")
                    #customer.login()
                if customer.login():
                    print(f"Welcome {customer.customer_name}!")
                    
                    while True:

                        print("1. Deposit")
                        print("2. Withdraw")
                        print("3. Transfer")
                        print("4. Check balance")
                        print("5. Logout")
                        sub_choice = input("Enter your choice: ")
                        if sub_choice == "1":
                            customer.deposit()
                        elif sub_choice == "2":

                            customer.withdraw()
                        elif sub_choice == "3":
                            customer.transfer()
            
                        elif sub_choice == "4":
                            customer.view_balance()
                        elif sub_choice == "5":
                            print("Logout successful.")
                            break
                        else:
                            print("Invalid choice. Please try again.")
                            break
            elif choice == "3":
                print("THANK YOU FOR TRUSTING US!!!")
                print("If you have any issues, call our customer care: +101")
                break
            else:
                print("Invalid choice. Please try again.")
                    




if __name__ == "__main__":
    main()
