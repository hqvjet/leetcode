class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res = []
        for row in image:
            flipped = list(reversed(row))
            inverted = [1 - pixel for pixel in flipped]
            res.append(inverted)

        return res