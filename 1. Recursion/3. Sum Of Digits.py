'''
 Find the sum of digits of a positive number using recursion
'''


def sumDigits(n):
    if n <= 0:
        return 0
    else:
        return n%10 + sumDigits(int(n/10))

# testing    
assert sumDigits(327) == 12
assert sumDigits(0) == 0
assert sumDigits(11110110) == 6