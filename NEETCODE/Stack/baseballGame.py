class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res =[]

        for o in operations:
            if o == '+':
                res.append(res[-1] + res[-2])
            elif o == 'D':
                res.append(res[-1] * 2)
            elif o == 'C':
                res.pop()
            else: # A string representing a number
                res.append(int(o))

        return sum(res)