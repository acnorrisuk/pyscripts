# passwords
# logical operators

username = ""
while not username:
    username = input("Username: ")

password = ""
while not password:
    password = input("Password: ")
    
if username == "Adam" and password == "Jeremy":
    print("Hi Adam")

elif username == "guest" or password == "guest":
    print("Welcome Guest")

else:
    print("Login Failed\n")

input("\n\nexit")
