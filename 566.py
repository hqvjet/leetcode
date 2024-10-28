class Solution:

    # idea: if area of original shape equals to new shape, then we will 
    # flat original into 1d matrix, then add each of element into new shape one by one
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # check for area of 2 shapes
        if r * c != len(mat) * len(mat[0]):
            return mat

        # flat original matrix
        flat_nums = [num for row in mat for num in row]
        reshaped_matrix = []

        # add each of flatten matrix into empty reshaped matrix
        for i in range(r):
            reshaped_matrix.append(flat_nums[i * c: (i + 1) * c])
        
        return reshaped_matrix
        
