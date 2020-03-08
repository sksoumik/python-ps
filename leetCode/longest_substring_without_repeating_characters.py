"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

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
