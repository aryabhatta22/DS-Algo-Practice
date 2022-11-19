'''
 Calculate factorial of a number using recursion where n >=1
'''

def fact(n):
    if n in [0,1]:
        return 1
    else:
        return n * fact(n-1)

# testing
assert fact(10) == 3628800
assert fact(6) == 720
assert fact(1) == 1