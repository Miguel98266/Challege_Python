import hashlib


def hash_password(string):
    # adding 5gz as password
    salt = "5gz"
    # Adding salt at the last of the password
    dataBase_password = string+salt
    # Encoding the password
    password_hashed = hashlib.md5(dataBase_password.encode())
    # Printing the Hash
    print(password_hashed.hexdigest())
    return password_hashed.hexdigest()
