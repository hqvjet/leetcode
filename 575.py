class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType) // 2
        a = set(candyType)
        return min(len(a), n)

