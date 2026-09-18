#here i will store the password securely, it will not be accessed
#this password will get imported to the security check
#without revealing its own characters

filename = "secret_password.txt"
def mypassword():
    try:
        with open(filename, "x") as file:
            file.write("waqas2004")
    except FileExistsError:
        pass

mypassword()
