import random

import string as str

letter = str.ascii_letters
number = str.digits
punctuation = str.punctuation


def random_password_generator(len: int):
    cahracters = letter+number+punctuation
    random_password = ''.join(random.choice(cahracters) for i in range(len))
    print(random_password)


if __name__ == "__main__":
    pass_length = int(input("Enter password length: "))
    random_password_generator(pass_length)
