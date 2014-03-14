#/usr/bin/python

# How to figure out if a string is a palindrome

def palindrome(str):
    strLength = str.__len__()
    for i in range(0, strLength - 1):
        if str[i] == str[strLength -1 - i]:
            return True
        else:
            return False

if __name__ == "__main__":
    palindrome()
