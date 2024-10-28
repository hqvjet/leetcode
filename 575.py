class Solution:

    # idea: We will just simply pay attention on num of type and num of candies / 2 
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType) // 2
        a = set(candyType)
        return min(len(a), n)

