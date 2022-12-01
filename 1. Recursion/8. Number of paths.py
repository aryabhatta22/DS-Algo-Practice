'''
Number of paths:
    
https://practice.geeksforgeeks.org/problems/number-of-paths0926/1

'''

class Solution:
    def numberOfPaths (self, n, m):
        if n== 1 or m == 1:
            return 1
        return self.numberOfPaths(n-1, m) + self.numberOfPaths(n, m-1)
