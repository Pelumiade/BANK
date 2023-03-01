A BANKING APP (CONSOLE APPLICATION)


This is a banking app (a console application) using python Class and methods.
This app contains three menu: 
1.	The Admin
2.	The Staff
3.	The customers



THE ADMIN


This is a Python code for a basic staff management system that allows an admin to perform several tasks such as creating staff, viewing staff and customer activities, suspending or reactivating staff, and logging out.

The code imports the necessary modules including csv for working with CSV files, datetime for handling dates and times, and random and string for generating random passwords.

The code defines a function random_password() that generates a random password consisting of seven letters, which will be used to create temporary passwords for newly created staff members.

The Admin class is then defined, which has several methods:

__init__: The constructor method that initializes the admin's username, password, and login status.
login: A method that accepts a username and password and checks if they match the admin's username and password. If the login is successful, the method sets the logged_in attribute to True.
create_staff: A method that prompts the admin to enter a username for a new staff member, generates a temporary password using random_password(), records the new staff member's details including the username, temporary password, creation date, and status in a CSV file, and prints the staff member's details.
view_staff_activity: A method that reads the content of a log file containing the activities of staff members and prints them to the console.
view_customer_activities: A method that reads the content of a log file containing the activities of customers and prints them to the console.
suspend_staff: A method that prompts the admin to enter the username of a staff member to be suspended, searches for the staff member's details in the CSV file, sets their status to "Suspended", updates the CSV file, and prints a success message.
reactivate_staff: A method that prompts the admin to enter the username of a staff member to be reactivated, searches for the staff member's details in the CSV file, sets their status to "Active" if they were previously suspended, updates the CSV file, and prints a success message.
logout: A method that sets the logged_in attribute to False and prints a success message.



THE STAFF


This Python code defines a class Staff which provides functionalities for staff of a bank. The class has methods for logging in, depositing money into a customer's account, checking a customer's account balance, and viewing the staff log.

The Staff class imports csv, datetime, customer, log, and admin modules from respective files. It then instantiates an Admin object admin, a Log object log, and a Logger object logger. A Customer object is also instantiated, but its attributes are initialized with placeholder values.

The Staff class has an __init__ method that initializes the staff_username, staff_password, and status attributes of the object to empty strings. The status attribute is not used in the code.

The new_staff_login method allows new staff to log in to the system. The method prompts the user to enter a username, which is checked against a CSV file containing staff usernames and passwords. If the username is found, the corresponding password is displayed, and the user is prompted to enter their password. If the entered password matches the stored password, the user is logged in and prompted to change their password. The new password is written to the CSV file, and the method returns True. Otherwise, the method returns False.

The existing_staff_login method allows existing staff to log in to the system. The method prompts the user to enter their username and password, which are checked against the CSV file containing staff usernames and passwords. If the username and password match an active staff account, the user is logged in and the method returns True. If the account is suspended, the user is informed that their account is inactive and the method returns False. If the username or password is incorrect, the user is informed that their login details are incorrect, and the method returns False.

The deposit method allows staff to deposit money into a customer's account. The method prompts the user to enter the account number and amount to deposit. It then reads the CSV file containing account details and updates the account balance for the specified account. The method also writes the deposit transaction to a CSV file containing all bank transactions. Finally, the updated customer account details are saved to a file, and a log entry is made indicating the name of the staff member who made the deposit, the amount deposited, and the name and account number of the customer.

The check_balance method allows staff to check the balance of a customer's account. The user is prompted to enter the account number, which is used to search the CSV file containing account details. If the account is found, the customer's name, account number, and balance are displayed. Otherwise, the user is informed that the account was not found.

The logout method logs out the staff member by resetting their username and password to empty strings.

The view_log method allows staff to view the log of all staff activities. The method reads a text file containing all staff activities and prints them to the console. The name of the staff member who viewed the log is added to the log file.

The display_menu method displays the main menu for staff members. The method prompts the user to select an option, which determines which method is called. The user can choose to create a new staff account, log in to an existing staff account, exit the system, or perform other actions (deposit, check balance, view log) if they are logged in. If the user is not logged in, they are prompted to log in first. The method uses a while loop to repeatedly display the menu until the user chooses to exit the system.



THE CUSTOMER

The code defines a Customer class that contains various methods to create and manage a customer's account. The Customer class has methods to create an account, log in to an existing account, deposit and withdraw funds, transfer funds to another account, and update the account details in a CSV file.

The code uses the built-in csv module to read and write CSV files, the random module to generate random account numbers, and the datetime module to record transaction dates and times.

The Logger class is imported from the log.py file and is used to log various activities like customer login, deposit, withdrawal, and transfer.

In the Customer class, the __init__ method initializes various attributes of a customer's account like account type, account number, customer PIN, and balance. The create_account method is used to create a new account, where the customer is prompted to enter their personal details like full name, phone number, and account type. A random 10-digit account number is generated and the customer's PIN and balance are set to default values.

The login method is used to log in to an existing account. The customer is prompted to enter their account number and PIN. The account details are read from a CSV file, and if the account number and PIN match, the customer is logged in, and their account details are retrieved from the CSV file.

The deposit method is used to deposit funds into a customer's account. The customer is prompted to enter the amount to deposit, and the account balance is updated. A new transaction is logged in the log.csv file with the transaction type, amount, and date and time of the transaction.

The withdraw method is used to withdraw funds from a customer's account. The customer is prompted to enter the amount to withdraw, and if the amount is greater than the current balance, the transaction fails. Otherwise, the account balance is updated, and a new transaction is logged in the log.csv file.

The transfer method is used to transfer funds from one account to another. The customer is prompted to enter the recipient's account number and the amount to transfer. If the amount to transfer is greater than the current balance, the transaction fails. Otherwise, the recipient's account is located in the CSV file, and the transfer amount is added to their account balance. The sender's account balance is updated, and the transaction is logged in the log.csv file.

The save_to_file and update_account_file methods are used to save the account details to a CSV file and update the account balance in the file, respectively.


