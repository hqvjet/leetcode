class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)
        res = len(candies) * [False]
        for i in range(len(candies)):
            if candies[i] + extraCandies >= greatest:
                res[i] = True

        return res