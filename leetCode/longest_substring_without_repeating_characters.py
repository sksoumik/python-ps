"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        current_length = max_length = 0
        for i, num in enumerate(s):
            current_length -= s[i - current_length:i].find(num)
            max_length = max(max_length, current_length)
        return max_length


if __name__ == "__main__":
    obj = Solution()
    s = "abccsdr"
    res = obj.lengthOfLongestSubstring(s)
    print(res)
