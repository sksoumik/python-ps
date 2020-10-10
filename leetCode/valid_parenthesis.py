# https://leetcode.com/problems/valid-parentheses/submissions/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        open_p = ["(", "{", "["]
        close_p = [")", "}", "]"]

        pairs = dict(zip(close_p, open_p))

        for c in s:
            if c in open_p:
                stack.append(c)
            elif (len(stack) == 0 or pairs[c] != stack.pop()):
                return False

        return stack == []


if __name__ == "__main__":
    obj = Solution()
    inp = input("Enter some parenthesis")
    print(obj.isValid(inp))
