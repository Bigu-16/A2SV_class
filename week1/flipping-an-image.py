class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        # flipped = [[0]*n]
        for row in image:
            row.reverse()

        for row in range(n):
            for col in range(n):
                if image[row][col] == 0:
                    image[row][col] = 1
                else:
                    image[row][col] = 0
        
        return image
