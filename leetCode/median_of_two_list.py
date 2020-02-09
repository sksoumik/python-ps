"""
https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/
"""
import statistics


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        s = sorted(nums1 + nums2)
        m = statistics.median(s)
        return m


if __name__ == '__main__':
    list_1 = [2, 3]
    list_2 = [5, 7, 6, 10]
    obj = Solution()
    median = obj.findMedianSortedArrays(list_1, list_2)
    print(median)
