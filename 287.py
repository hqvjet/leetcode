class Solution:

    # idea: use distribute array to count the repeat number
    def findDuplicate(self, nums: List[int]) -> int:
        # create the array of n element initialized equal 0
        counter = [0] * len(nums)

        for i in range(len(nums)):
            # increase count of number i 
            counter[nums[i]] += 1
            # if value > 1 mean that the number i is repeated
            if counter[nums[i]] > 1:
                return nums[i]

        return -1
