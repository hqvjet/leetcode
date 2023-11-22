class Solution:
    
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        
        xor_bn = bin(xor)
        xor_bn = xor_bn[2:]
        
        count = 0
        for i in xor_bn:
            if i == '1':
                count += 1
        
        return count