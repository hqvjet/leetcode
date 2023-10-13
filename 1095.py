# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:


class Solution:
    
    def search_top(self, mountain_arr: list[int]) -> int:
        l, r = 0, mountain_arr.length() - 1
        length = mountain_arr.length()
        
        while l <= r:
            mid = (l + r) // 2
            if mid + 1 < length and mid - 1 > -1:
                p_mid = mountain_arr.get(mid - 1)
            if mid + 1 < length:
                n_mid = mountain_arr.get(mid + 1)
            if(mid - 1) > -1:
                c_mid = mountain_arr.get(mid)
            if (mid + 1 < length and mid - 1 > -1 and c_mid and c_mid > p_mid) and (c_mid > n_mid):
                return mid
            elif (mid + 1 < length and c_mid < n_mid) or (mid - 1 > -1 and c_mid > p_mid):
                l = mid + 1
            elif (mid + 1 < length and c_mid > n_mid) or (mid - 1 > -1 and c_mid < p_mid):
                r = mid - 1
                
        return -1
    
    def binary_search(self, target: int, mountain_arr: list[int], start: int, stop: int, reverse: bool) -> int:
        #arr.get 13 times
        while start <= stop:
            mid = (start + stop) // 2
            c_mid = mountain_arr.get(mid)
            if c_mid == target:
                return mid
            elif c_mid < target:
                if not reverse:
                    start = mid + 1
                else:
                    stop = mid - 1
            else:
                if not reverse:
                    stop = mid - 1
                else:
                    start = mid + 1
                
        return -1
        
    def findInMountainArray(self, target: int, mountain_arr: list[int]) -> int:
        mountain_top = self.search_top(mountain_arr)
        
        index = self.binary_search(target, mountain_arr, 0, mountain_top, False)
        if index != -1:
            return index
        index_reverse = self.binary_search(target, mountain_arr, mountain_top + 1, mountain_arr.length() - 1, True)
        if index_reverse != -1:
            return index_reverse
            
        return -1
            
    
solution = Solution()
print(solution.findInMountainArray(1, [1,5,2]))