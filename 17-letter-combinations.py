class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        L=[]
        mapping = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

        def com(combo,digit):
            if not digit:
                return L.append(combo)
                
            digit_str=mapping[digit[0]]
            for letter in digit_str:
                com(combo+letter,digit[1:])
            return L
        return com("",digits)
