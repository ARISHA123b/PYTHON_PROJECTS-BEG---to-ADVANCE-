from cryptography.fernet import Fernet


def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

key = load_key() 
fer = Fernet(key)
'''
def write_key():
    key = Fernet.generate_key ()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
write_key()'''



def view():
    with open("passwords.txt", "r") as f :
        for line in f.readlines():
            data = line.rstrip()
            user , passw = data.split("|") 
            print("User:",user,"| Password",str(fer.decrypt(passw.encode()).decode()))


def add():
    name = input("Account name :  ")
    pwd = input("password:  ")
    with open("passwords.txt","a") as f :
        f.write(name +"|"+fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input("Would you like to add a new password or view exsisting ones (view , add) or press Q to quit:  ").lower()


    if mode == "q":
        break
    if mode == "view":
        view()
    
    elif mode == "add":
        add()

    else :
        print("Invalid")
        continue
    # encode string to bytes 
    # encrypt = Bytes = bytes encrypted data lock it 
    # decrypt  = encrypted -- > bytes unlock it 