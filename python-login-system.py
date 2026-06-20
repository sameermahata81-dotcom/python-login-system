print("python-login-system")
print("Facebook style Log in System")

username = input("Username: ")
password = input("Password: ")

attempts = 0

while (username != "Samir Mahata" or password != "xyz1234") and attempts < 3:
    attempts += 1
    print("Please try Again")
    print("Attempts Left:", 3 - attempts)
    
    username = input("Username: ")
    password = input("Password: ")

if username == "Samir Mahata" and password  == "xyz1234":
    print("Login Successfully")
else:
    print("Account Locked")
