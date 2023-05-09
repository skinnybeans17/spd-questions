class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0 
        b = 1
        while a<= b and b < len(nums):
            if nums[a] != nums[b]:
                nums[a+1] = nums[b]
                a += 1
            b += 1
        return a + 1
