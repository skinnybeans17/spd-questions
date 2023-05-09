class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        #First, let up the lists, including the outcomes and lists.
        holder = 0
        outcome = ''

        a = list(a)
        b = list(b)

        #Then, see the while loop.
        while a or b or holder:
            if a:
                holder += int(a.pop())
            if b:
                holder += int(b.pop())

            outcome += str(holder %2)
            holder //= 2

        #Finally, return the answer!
        return outcome[::-1]
