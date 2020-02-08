# https://leetcode.com/problems/reverse-integer/


class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(x)
        is_minus = False
        if str_x[0] == '-':
            str_x = str_x[1:]
            is_minus = True

        rev = str_x[::-1]

        if is_minus:
            rev = '-' + rev
        rev = int(rev)
        if rev > 2**31 - 1 or rev < -2**31:
            return 0
        return rev


rev = Solution()
sample = input()
print(rev.reverse(sample))
