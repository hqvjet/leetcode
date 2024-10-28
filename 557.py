class Solution:

    # idea: for each word of sentence, reverse these words and printout
    def reverseWords(self, s: str) -> str:
        res = ""

        # split sentence by " "
        for i in s.split():
            # reverse word and save to 'res' array
            res += i[::-1] + ' '

        # remove the last ' '
        res = res[:-1]

        return res
