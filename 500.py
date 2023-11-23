class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1 = "qwertyuiop"
        r2 = "asdfghjkl"
        r3 = "zxcvbnm"

        res = []
        for i in words:
            temp = ""
            temp_i = i.lower()
            if temp_i[0] in r1:
                temp = r1
            elif temp_i[0] in r2:
                temp = r2
            else:
                temp = r3

            lock = False
            for j in temp_i:
                if j not in temp:
                    lock = True
                    break
                
            if not lock:
                res.append(i)

        return res
            