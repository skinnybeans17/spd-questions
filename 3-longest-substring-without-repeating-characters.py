class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        first, maximumSub, seen = 0, 0, set()
        for second in range(len(s)):
            while s[second] in seen:
                seen.remove(s[first])
                first += 1
            seen.add(s[second])
            maximumSub = max(maximumSub, (second - first) + 1)
        return maximumSub
