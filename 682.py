class Solution:

    # idea: implementation problem, just follow description
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for i in operations:
            if i == 'D':
                res.append(res[-1] * 2)
            elif i == 'C':
                res = res[:-1]
            elif i == '+':
                res.append(res[-1] + res[-2])
            else:
                res.append(int(i))

        return sum(res)
