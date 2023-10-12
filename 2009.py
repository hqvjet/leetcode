class Solution:
    def binary_search(self, nums, start, end, target) -> int:
        start = 0
        index = 0

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] <= target:
                index = mid
                start = mid + 1
            else:
                end = mid - 1

        return index
    
    def backtracking_to_first_duplication_number(self, nums, index) -> int:
        position = index
        target = nums[index]
        
        for i in range(index - 1, 0, -1):
            if target != nums[i]:
                i = -1
            else:
                position = i
        
        return position

    def prefix_sum(self, nums) -> list[int]:
        ps = [0]
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                ps.append(ps[-1] + 1)
            else:
                ps.append(ps[-1])
                
        return ps
    
    # ver3
    def minOperations(self, nums) -> int:
        if len(nums) == 1:
            return 0
        
        nums.sort()
        l = len(nums) - 1
        ans = 1000000
        i = 0
        j = self.backtracking_to_first_duplication_number(nums, self.binary_search(nums, 0, l, nums[0] + l))
        duplication = self.prefix_sum(nums)
        
        while j <= l and i <= l:
            while j + 1 <= l and nums[i] + l >= nums[j + 1]:
                # print('reached')
                j += 1
                
            if j <= l:
                ans = min(ans, l + 1 - (j - i + 1) + duplication[j] - duplication[i])
                # print(i, j, l + 1 - (j - i + 1) + duplication[j] - duplication[i])
                i += 1
        # print(nums)
        return ans
        
solution = Solution()
print(solution.minOperations([41,33,29,33,35,26,47,24,18,28]))
