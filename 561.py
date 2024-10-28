class Solution:

    # idea: we have to pair the two closest numbers to get the optimal answer
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        s = 0
        
        # sum all of the first pair, jump 2 steps to skip the max(pair) 
        for i in range(0, len(nums), 2):
            s += nums[i]

        return s
