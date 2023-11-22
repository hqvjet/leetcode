class Solution:
    def dup(self, flag):
        res = ""

        for i in range(flag):
            res += 'a'

        return res

    def toGoatLatin(self, sentence: str) -> str:
        vob = [i for i in sentence.split()]

        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        flag = 1
        for i in range(len(vob)):
            if vob[i][0] in vowel:
                vob[i] += 'ma'
            else:
                vob[i] = vob[i][1:] + vob[i][0] + 'ma'
        res = ""
        for i in vob:
            res += i + self.dup(flag) + ' '
            flag += 1
        res = res[0: -1]

        return res 