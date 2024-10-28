class Solution:

    # idea: create 3 arrays of each keyboard's row, then we will check for if character[i] is in the same row
    def findWords(self, words: List[str]) -> List[str]:
        # Init 3 arrays of keyboard's key
        r1 = "qwertyuiop"
        r2 = "asdfghjkl"
        r3 = "zxcvbnm"

        res = []
        # loop for each words
        for word in words:
            # temp presents for row selected after checking word.lower()[0]
            temp = r1
            temp_word = word.lower()
            if temp_word[0] in r1:
                temp = r1
            elif temp_word[0] in r2:
                temp = r2
            else:
                temp = r3

            lock = False
            # after got temp_word[0]'s row, we check for each character of temp_word are in temp 
            for j in temp_word:
                if j not in temp:
                    lock = True
                    break
                
            if not lock:
                res.append(i)

        return res
            
