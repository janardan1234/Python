import random

import string as str

letter = str.ascii_letters
number = str.digits
punctuation = str.punctuation


def random_password_generator(len: int):
    cahracters = letter+number+punctuation
    try:
        random_password = ''.join(random.choice(cahracters)for i in range(len))
        return random_password
    except ValueError:
        print(f"Enter numbers only {len} isn't a number.")


if __name__ == "__main__":
    pass_length = int(input("Enter password length: "))
    password = random_password_generator(pass_length)
    print(password)
