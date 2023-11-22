class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []

        for i in range(left, right + 1):
            if i < 10 and i != 0:
                res.append(i)
            else:
                temp = i * 1

                while temp != 0:
                    if temp % 10 != 0 and i % (temp % 10) == 0:
                        temp //= 10
                    else:
                        break

                if temp == 0:
                    res.append(i)

        return res
