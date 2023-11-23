class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat
    
        flat_nums = [num for row in mat for num in row]
        reshaped_matrix = []
        
        for i in range(r):
            reshaped_matrix.append(flat_nums[i * c: (i + 1) * c])
        
        return reshaped_matrix
        