class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mourse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        mourse_encryption = []
        for i in words:
            str = ""
            for j in i:
                str += mourse_code[ord(j) - 97]
                
            if str not in mourse_encryption:
                mourse_encryption.append(str)
        
        return len(mourse_encryption)