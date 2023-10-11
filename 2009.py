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
        pass
        
solution = Solution()
print(solution.minOperations([8,10,16,18,10,10,16,13,13,16]))