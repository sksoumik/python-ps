"""Problem:
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given a sorted array nums, remove the duplicates in-place such that each element appear only 
once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array 
in-place with O(1) extra memory.

"""


class Solution:
    def removeDuplicates(self, nums):
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] == nums[i - 1]:
                del nums[i]
        return len(nums)


if __name__ == "__main__":
    obj = Solution()
    sorted_list = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(obj.removeDuplicates(sorted_list))
