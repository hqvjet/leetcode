class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        tree = (2 * 1e5) * []
        
        for i in adjacentPairs:
            tree[i[0] if i[0] >= 0 else 1e5 - i[0]].append(i[1])
            tree[i[1] if i[0] >= 0 else 1e5 - i[0]].append(i[0])
            
        for i in 
        