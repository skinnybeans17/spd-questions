'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
'''

'''
Example:
Input: nums = [1,3,5,6], target = 5
Output: 2
'''

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if nums[i] > target:
                return i
            if i == len(nums) - 1:
                return i + 1
'''
Pseudocode:
Loop through the entire length of the list
Constantly check if the current list's value is the target
Return index if yes
Return target if current value is greater than target
Return index + 1 if the current value is less than target when the end of the list is reached
'''
