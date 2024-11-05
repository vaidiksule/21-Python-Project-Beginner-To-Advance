from cryptography.fernet import Fernet
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''
def load_key():
    with open("key.key", 'rb') as f:
        key = f.read()
    return key

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print('-'*25)
            print("Username: ",user)
            print("Password: ", fer.decrypt(passw.encode()).decode())

def add():
    name = input("Account Name: ")
    password = input("Password: ")

    with open('password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(password.encode()).decode() + '\n')

key = load_key()
fer = Fernet(key)

while True:
    mode = input("Do you wanna view password or add one(view, add) or 'q' to quit : ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")