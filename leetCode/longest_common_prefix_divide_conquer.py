"""
leetcode: 
https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
"""


class Solution:
    def longestCommonPrefix(self, strs):
        low = 0
        high = len(strs) - 1
        res = self.longest_common_prefix(strs, low, high)
        if (len(strs) == 0):
            return ""
        return res

    def common_prefix_between_two_strings(self, string1, string2):
        l1, l2 = len(string1) - 1, len(string2) - 1
        i, j = 0, 0
        result = ""
        while i <= l1 and j <= l2:
            if string1[i] != string2[j]:
                break
            result = result + string1[i]
            i = i + 1
            j = j + 1
        return result

    def longest_common_prefix(self, arr, low, high):
        if low == high:
            return arr[low]
        if low < high:
            mid = low + (high - low) // 2
            s1 = self.longest_common_prefix(arr, low, mid)
            s2 = self.longest_common_prefix(arr, mid + 1, high)
            return self.common_prefix_between_two_strings(s1, s2)


if __name__ == "__main__":
    obj = Solution()
    l = []
    res = obj.longestCommonPrefix(l)
    print(res)
