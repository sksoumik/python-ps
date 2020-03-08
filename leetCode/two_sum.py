"""
https://leetcode.com/problems/two-sum/

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""


class Solution:
    def twoSum_bf(self, nums, target):
        """
        TC: O(n^2)

        Arguments:
            nums {[List[int]]} -- [description]
            target {[List[int]]} -- [description]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum_hash_table(self, nums, target):
        """[O(n log n)]
        
        Arguments:
            nums {[List[int]]}
            target {[int]} 
        
        Returns:
            [List[int]] -- [list of indices]
        """
        hash_table = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_table:
                return [hash_table[complement], i]
            hash_table[nums[i]] = i


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    obj = Solution()
    print(obj.twoSum_hash_table(nums, target))
