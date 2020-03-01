"""
https://leetcode.com/problems/longest-common-prefix/
Write a function to find the longest common prefix string 
amongst an array of strings.

"""


class Solution:
     
    # find the common string between two strings 
    def common_prefix_utils(self, str1, str2):
        result = ""
        i = j = 0
        while (i <= len(str1) - 1) and (j <= len(str2) - 1):
            if (str1[i] != str2[j]):
                break
            result += str1[i]
            i += 1
            j += 1
        return result 


    def longestCommonPrefix(self, strs):
        prefix = strs[0]
        for i in range(1, len(strs)):
            prefix = self.common_prefix_utils(prefix, strs[i])
        return prefix


obj = Solution()
inputa_arry = ["dog","racecar","car"]
print(obj.longestCommonPrefix(inputa_arry))

