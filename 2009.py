class Solution:
    def binary_search(self, nums, start, end, target) -> int:
        start = 0

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
            
        return -1

    
    # ver3
    def minOperations(self, nums) -> int:
        length = len(nums) - 1
        
        nums.sort()
        longest_continue_sequence = 1
        count = 1
        ans = 1000000
        duplicate = 0
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                count += 1
                
            elif nums[i] == nums[i - 1]:
                duplicate += 1
                
            else:
                longest_continue_sequence = max(count, longest_continue_sequence)
                count = 1 
                    
            target_index = self.binary_search(nums,0, i-1, nums[i] - length)
            if target_index != -1:
                ans = min(ans, len(nums) - i - 1 + target_index)
                
        if count != 1:
            longest_continue_sequence = max(count, longest_continue_sequence)
            
        print(nums)
                
        return min(ans, len(nums) - longest_continue_sequence) + duplicate
        
solution = Solution()
print(solution.minOperations([8,10,16,18,10,10,16,13,13,16]))