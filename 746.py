class Solution:

    # idea: We can step 1 or 2 steps, then we will compare which step is more optimal,
    # we save the previous optimal step, then compare (previous_step + cost of 1 step) and (previous_step + cost of 2 steps)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0, 0]

        # compare each step using dp formular below and update 'dp' array
        for i in range(2, len(cost)):
            dp.append(min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])) 

        return min(dp[-1] + cost[-1], dp[-2] + cost[-2])
