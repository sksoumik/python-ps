"""
https://leetcode.com/problems/two-sum/
"""


class Solution:
    def twoSum(self, nums, target):
        hash_table = {}  # lookup table.
        for count, num in enumerate(nums):
            if target - num in hash_table:
                return ([hash_table[target - num], count])
            hash_table[num] = count
        return ([])


if __name__ == '__main__':
    nums = [2, 7, 11, 15, 30]
    target = 45
    obj = Solution()
    print(obj.twoSum(nums, target))
    
