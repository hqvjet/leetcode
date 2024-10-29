class Solution:

    # idea: using dp to handle the maximum value the robber can get
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        # init dp array
        dp = [nums[0], nums[1], nums[0] + nums[2]]

        # find max of dp[i - 3] and dp[i - 2] for optimalize and addition of the max number and value of house[[i]
        for i in range(3, len(nums)):
            dp.append(max(dp[i - 2], dp[i - 3]) + nums[i])

        return max(dp)
