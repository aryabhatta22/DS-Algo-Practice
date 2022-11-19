'''
Calculate power of a number using recursion (eg 2^3)
'''

def calcPower(base, exp):
    if exp == 0:
        return 1
    else:
        return base * calcPower(base, exp-1)

# testing    
assert calcPower(2, 3) == 8
assert calcPower(3, 0) == 1
assert calcPower(2, 32) == 4294967296