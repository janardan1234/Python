import random

import string


def random_password_generator(length: int):
    char = string.printable
    try:
        random_password = ''.join(random.choice(char)for i in range(length))
        return random_password
    except ValueError:
        print(f"Enter numbers only {length} isn't a number.")


def generate_password(length: int):

    if length <= 8 or length > 16:
        return "Password must be between 8 and 16 letters."
    else:
        return random_password_generator(length)


if __name__ == "__main__":
    pass_length = int(input("Enter password length: "))
    password = generate_password(pass_length)
    print(password)
