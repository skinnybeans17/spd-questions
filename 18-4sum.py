'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
'''

'''
Example:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
'''

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
	
        def oneSum(nums: List[int], target: int, output: int) -> List[List[int]]:
            result = []
            
            if not nums:
                return result

            average_value = target // output

            if average_value < nums[0] or nums[-1] < average_value:
                return result
            
            if output == 2:
                return twoSum(nums, target)
    
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for subset in oneSum(nums[i + 1:], target - nums[i], output - 1):
                        result.append([nums[i]] + subset)
    
            return result

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            result = []
            low, high = 0, len(nums) - 1
    
            while (low < high):
                current_sum = nums[low] + nums[high]
                if current_sum < target or (low > 0 and nums[low] == nums[low - 1]):
                    low += 1
                elif current_sum > target or (high < len(nums) - 1 and nums[high] == nums[high + 1]):
                    high -= 1
                else:
                    result.append([nums[low], nums[high]])
                    low += 1
                    high -= 1
                                                         
            return result

        nums.sort()
        return oneSum(nums, target, 4)