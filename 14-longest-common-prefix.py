class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        short_sent = min(strs, key=len)
        for letter in strs:
            while len(short_sent) > 0:
                if letter.startswith(short_sent):
                    break
                else:
                    short_sent = short_sent[:-1]
        return short_sent
