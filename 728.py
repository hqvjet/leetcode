class Solution:

    # idea: search sequently from left to right, check for divisible for each digit of number
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []

        # search sequently
        for i in range(left, right + 1):
            # number from 1 - 10 is sastified naturally
            if i < 10 and i != 0:
                res.append(i)
            else:
                # multiple by 1 because of avoiding memory location sharing
                temp = i * 1

                # divide number to digit
                while temp != 0:
                    if temp % 10 != 0 and i % (temp % 10) == 0:
                        temp //= 10
                    else:
                        break
                # if number is not = 0, that mean there is a digit that not sastified condition given
                if temp == 0:
                    res.append(i)

        return res
