'''
Power of Three:
    
https://leetcode.com/problems/power-of-three/description/

'''

import math 
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n >0 and 3**round(math.log(n, 3)) == n