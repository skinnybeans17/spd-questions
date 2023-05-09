class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #First, create an array that makes an integer from digits.
        integer = int(''.join(map(str,digits)))
        #Then, add up one to the array of numbers.
        integer +=1
        #Finally, adjust back to digits array.
        return [int(y) for y in str(integer)]
