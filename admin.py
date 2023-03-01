import csv
from datetime import datetime
import random
import string

def random_password():
        return "".join((random.choice(string.ascii_letters) for x in range(7)))
        
class Admin:
    def __init__(self):
        self.admin_username = "admin"
        self.admin_password = "adminpassword"
        self.logged_in = False

    
    def login(self, username, password):
        if username == self.admin_username and password== self.admin_password:
            self.logged_in = True
            print("Successfully logged in")
            return True
        else:
            return False

    def create_staff(self):
        staff_username = input("Enter a username for the staff member: ").capitalize()
        temp_password = random_password()
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open('staffs.csv', mode='a', newline='') as staff_file:
            staff_writer = csv.writer(staff_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            staff_writer.writerow([staff_username, temp_password, created_at, "Active"])

        print("Staff member created successfully!") 
        print(f"Username: {staff_username}\nTemporary Password: {temp_password}")

    
    # def view_staff_log(self):
    #     with open('staff.log', mode='r') as log_file:
    #         log_reader = csv.reader(log_file)
    #         for row in log_reader:
    #             print(row) 
            
    def view_staff_activity(self, filename="staff_log.txt"):
        with open(filename, "r") as file:
            log = file.read()
            print(log)
          

    def view_customer_activities(self, filename="log.txt"):
        #if self.logged_in:
        with open(filename, "r") as file:
            log = file.read()
            print(log)
          

    # def check_staff_activities(self):
    #     log_file = "activity_log.csv"
    #     with open(log_file, "r") as file:
    #         reader = csv.reader(file)
    #         self.format_activities(reader)  
    #  def new_staff_login(self):
        # username = input("Enter username: ").capitalize()
        # with open('staffs.csv', mode='r') as staff_file:
        #     staff_reader = csv.reader(staff_file)
        #     rows = list(staff_reader)
        #     for row in rows:
        #         if row[0] == username:
        #             print(f"Your password is: {row[1]}")
        #             password = input("Enter password: ")
        #             if row[1] == password:
        #                 print("Login Successful!")     

    def suspend_staff(self):
        staff_username=input("Enter username: ").capitalize()
        with open('staffs.csv', mode='r') as staff_file:
            staff_reader = csv.reader(staff_file)
            staff_data = list(staff_reader)


        for row in staff_data:
            if row[0] == staff_username:
                row[3] = "Suspended"
                with open('staffs.csv', mode='w', newline='') as staff_file:
                    staff_writer = csv.writer(staff_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    staff_writer.writerows(staff_data)
                print(f"{staff_username} has been suspended successfully.")
                return

        print(f"Could not find a staff member with username {staff_username}.")


   

    def reactivate_staff(self):
        staff_username=input("Enter username: ").capitalize()
        with open('staffs.csv', mode='r') as staff_file:
            staff_reader = csv.reader(staff_file)
            staff_data = list(staff_reader)


        for row in staff_data:
            if row[0] == staff_username:
                if row[3] == "Suspended":
                    row[3] = "Active"
                    with open('staffs.csv', mode='w', newline='') as staff_file:
                        staff_writer = csv.writer(staff_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        staff_writer.writerows(staff_data)
                    print(f"{staff_username} has been reactivated successfully.")
                    return
                elif row[3] == "Active":
                    print(f"{staff_username} is already active.")
                    return

        print(f"Could not find a staff member with username {staff_username}.")

        

    def logout(self):
        self.logged_in = False
        print("Logged out successfully!")    

    