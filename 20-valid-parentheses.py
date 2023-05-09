class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        twos = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        pack = []
        for parentheses in s:
            if parentheses in twos:
                pack.append(parentheses)
            elif len(pack) == 0 or parentheses != twos[pack.pop()]:
                return False

        return len(pack) == 0
