class Solution:

    # Idea: To find out result, we must know the greatest num of candies among those kids
    # and compare the (i_th kid' candies + extraCandy) to greatest num of candies. 
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Find the original greatest num of candy
        greatest = max(candies)

        # Init all of kids = False
        res = len(candies) * [False]
        
        for i in range(len(candies)):
            # if sastified condition below, the i_th kid will be True, else this kid still be False
            if candies[i] + extraCandies >= greatest:
                res[i] = True

        return res
