"""
https://leetcode.com/problems/palindrome-number/
Determine whether an integer is a palindrome. An integer is a palindrome when it 
reads the same backward as forward.

"""

class Solution:
    def isPalindrome(self, x):
        int_to_str = str(x)
        rev = int_to_str[::-1]
        if int_to_str == rev:
            return True
        else:
            return False


if __name__ == "__main__":
    obj = Solution()
    res = obj.isPalindrome(121)
    print(res) 
