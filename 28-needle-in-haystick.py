class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        last=len(needle)
        for first in range(len(haystack)):
            if haystack[first:last]==needle:
                return first
            last+=1
        return -1 
