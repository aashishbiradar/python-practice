str_1 = "HELLO"
str_2 = "MADAM"

def is_palindrome(str):
    rstr = str[::-1]
    if rstr == str:
        print("Palindrome!")
    else:
        print("Not Palindrome!")

is_palindrome(str_1)
is_palindrome(str_2)