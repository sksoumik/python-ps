"""
Checking if a string is palindrome ot not.
"""


# Process 01
def isPalindrome(string):
    flag = 0

    length = len(string)
    for i in range(length):
        if (string[i] != string[length - i - 1]):
            flag = 1
            break

    if (flag == 0):
        print("Palindrome")
    else:
        print("Not a Palindrome")


# driver code
sample = input("Please enter your own String : ")
isPalindrome(sample)

"""
Procedure 02

string = input()
if string != string[::-1]:
    print("Not palindrome")
else:
    print("Palindrome")

"""
