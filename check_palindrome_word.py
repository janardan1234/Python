def is_palindrome(word: str):
    word = word.replace(' ', '')
    if word == word[::-1]:
        print(word, "is a palindrome.")
    else:
        print(word, "is not a palindrome.")


word = input("Enter a word: ")

is_palindrome(word)
