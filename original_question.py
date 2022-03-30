class Solution(object):
    def fiveSum(self, nums, target):
        for index1, num1 in enumerate(nums):
            for index2, num2 in enumerate(nums):
                for index3, num3 in enumerate(nums):
                    for index4, num4 in enumerate(nums):
                        for index5, num5 in enumerate(nums):
                            if index1 is not index2 and index2 is not index3 and index3 is not index4 and index4 is not index5 and num1 + num2 + num3 + num4 + num5 == target:
                                return [index1, index2, index3, index4, index5]

if __name__ == '__main__':
    test = Solution()
    method = test.fiveSum([2, 6, 4, 8, 10], 30)
    print(method)