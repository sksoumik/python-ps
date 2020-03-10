"""
https://leetcode.com/problems/search-insert-position/

Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

"""


class Solution:
    def searchInsert(self, nums, target):
        try:
            return nums.index(target)
        except:
            for index, value in enumerate(nums):
                if value > target:
                    return index
            return len(nums)


if __name__ == "__main__":
    obj = Solution()
    nums = [1, 3, 5, 6]
    target = 7
    res = obj.searchInsert(nums, target)
    print(res)
