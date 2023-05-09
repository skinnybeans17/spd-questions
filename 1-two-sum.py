'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

'''
Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index1, num1 in enumerate(nums):
            for index2, num2 in enumerate(nums):
                if index1 is not index2 and num1 + num2 == target:
                    return [index1, index2]
                
'''
Pseudocode:
Create a dict that's empty
Loop through all the list's numbers
Get the target and number's difference
Return the index and value if it already exists there
Add them to directory if otherwise
'''
