class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0, 0]
        
        for i in range(2, len(cost)):
            dp.append(min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])) 
        
        return min(dp[-1] + cost[-1], dp[-2] + cost[-2])