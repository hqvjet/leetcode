class Solution:

    # idea: for picking stone optimaly, we will sort the array ascen, 
    # then for each turn of each players pick the largest (last) stone in sorted array
    def stoneGame(self, piles: List[int]) -> bool:

        # sort array ascen
        piles.sort()
        # True: Alice, False: Bob
        turn = True
        alice = 0
        bob = 0
        n = len(piles)
        for i in range(n):
            # take the last element of array
            if turn:
                alice += piles[n - i - 1]
            else:
                bob += piles[n - i - 1]
            turn = not turn
          
        return alice > bob
