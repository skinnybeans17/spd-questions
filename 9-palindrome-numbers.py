'''
This question is asking for a palindrome number. It also says ‘Given an integer x, return true if x is a palindrome integer’. For the definition, it says an integer is a palindrome when it reads the same backwards as forward. For example, 123 is not a palindrome, while 121 is a palindrome.
'''

'''
Example:
    Input: x = 121
    Output: true
    Explanation: 121 reads as 121 from left to right and from right to left
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        pali = x
        num = 0
        while x > 0:
            num = num * 10 + x % 10
            x = x //10
        if pali == num:
            return True
        else:
            return False
        
'''
Pseudocode:
Create a list that's empty
Add numbers to it
Reverse the list and check if they are equal
'''
