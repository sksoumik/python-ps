"""problem
https://leetcode.com/problems/remove-element/

Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place 
with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length

"""


class Solution:
    def removeElement(self, nums, val):
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                del nums[i]
        return len(nums)


if __name__ == "__main__":
    obj = Solution()
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    print(obj.removeElement(nums, val))
