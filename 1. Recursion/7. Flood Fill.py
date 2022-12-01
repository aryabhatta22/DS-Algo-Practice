'''
Flood Fill:
    
https://leetcode.com/problems/flood-fill/submissions/846812694/
'''

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols, orig_color = len(image), len(image[0]), image[sr][sc]
        if(orig_color == color):
            return image
        def traverseAndFill(r, c):
            if(not(0<= r < rows and 0<= c < cols) or image[r][c] != orig_color):
                return
            if(image[r][c] == orig_color):
                image[r][c] = color
            traverseAndFill(r-1, c)
            traverseAndFill(r+1, c)
            traverseAndFill(r, c-1)
            traverseAndFill(r, c+1)
        traverseAndFill(sr, sc)
        return image