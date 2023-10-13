class Solution:
    
    def isNumber(self, s: str) -> bool:
        try:
            float(s)
            if 'INF' in s.upper() or 'NAN' in s.upper():
                return False
            return True

            
        except :
            return False