#this function carries the actual key for authentication means
#only the authorized members can add items to the mall
#shadow script used for security measures
import getpass


#lets extract password from secret password
#it will be used to compare it with the one taken from the user
def load_password():
    with open("secret_password.txt", "r") as file:
        return file.read().strip()

#passing load_password to the security check
password = load_password()
def security_check():
    
    pw = getpass.getpass("Enter password: ")
    while pw != password:
        print("Try again")
        pw = getpass.getpass("Enter password: ")
    print("Access granted")

#test purpose
def show_verif():
    print("Verify yourself to enter product...")

def show_p_check():
    print("     Verify yourself to show All of the products...")          
    
    
        