def HasUppercase(password):
    for i in password:
        if i.isupper():
            return True


def isShort(password):
    return len(password) >= 8

def passwordChecker(password):
    if not HasUppercase(password):
        print("Password must contain at least one uppercase letter.")
    if not isShort(password):
        print("Password is too short.")
    else:
        print("Password is strong.")


password = input("Enter a password:")
passwordChecker(password)