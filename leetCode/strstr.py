"""problem statement
https://leetcode.com/problems/implement-strstr/
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

"""

class Solution:
    def strStr(self, haystack, needle):
        # return haystack.find(needle)
        for i in range(len(haystack)):
            if haystack[i] == needle:
                return i
            else:
                i = i+1
            return -1    
        


if __name__ == "__main__":
    obj = Solution()
    haystack = "hello"
    needle = "ll"
    print(obj.strStr(haystack, needle))
