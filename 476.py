class Solution:
    def findComplement(self, num: int) -> int:
        s = bin(num)[2:]
        complement = ''

        for i in range(len(s)):
            if s[i] == '1':
                complement += '0'
            else:
                complement += '1'
        
        return int(complement, 2)
