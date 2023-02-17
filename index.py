from hashing import hash_password
from createpassword import createpass


def main():
    print("Choose an option ")
    while (True):
        print("""
        1) Hash your password
        2) Create a password
        3) Exit
        """)
        option = input()
        match option:
            case("1"):
                hash_pass()
            case("2"):
                create_password()
            case("3"):
                print("Good Bye")
                break
            case _:
                print("Option not valid")


def hash_pass():
    string = input("What is your password? ")
    password_hashed = hash_password(string)
    print("Here you go 👌", password_hashed)


def create_password():
    number = int(input("How long you want your password?"))
    password_created = createpass(number)
    print("Here you go 👌", password_created)


if __name__ == "__main__":
    main()
