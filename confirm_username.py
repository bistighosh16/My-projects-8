class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def authenticate(self):
        attempts = 3
        while attempts > 0:
            username_input = input("Enter username: ")
            password_input = input("Enter password: ")
            if username_input == self.username and password_input == self.password:
                print("You've successfully logged in!")
                return
            else:
                attempts -= 1
                print(f"Incorrect username or password. Attempts left: {attempts}")
        print("Your account has been locked.")
username = input("Set your username: ")
password = input("Set your password: ")
user = User(username, password)
user.authenticate()
