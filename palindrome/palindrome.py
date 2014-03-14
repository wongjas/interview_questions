#/usr/bin/python

# How to figure out if a string is a palindrome

import string

# str -> str
def remove_punc(str):
    transTable = string.maketrans("", "")
    return str.translate(transTable, string.punctuation)

# str -> str
def remove_spaces(str):
    return str.replace(" ", "")

# str -> boolean
def palindrome_with_punc(str):
    # remove all spaces
    strNoSpaces = remove_spaces(str)
    # remove all punctuation
    rawString = remove_punc(strNoSpaces.replace)
    # lowercase
    return palindrome(rawString.lower())


# str -> boolean
def palindrome(str):
    strLength = str.__len__()
    for i in range(0, strLength - 1):
        if str[i] == str[strLength -1 - i]:
            return True
        else:
            return False

if __name__ == "__main__":
    palindrome()
