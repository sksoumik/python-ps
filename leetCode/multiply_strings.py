"""
problem: https://leetcode.com/problems/multiply-strings/
"""

class Solution:
    def multiply(self, num1, num2):
        num1, num2 = str(num1), str(num2)
        result = num1 * num2
        return result



if __name__ == "__main__":
    obj = Solution()
    num1 = "123"
    num2 = "324"
    result = obj.multiply(num1, num2)
    print(result)

