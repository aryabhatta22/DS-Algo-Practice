'''
 Calculate nth number in a fibonacci series where n>=1
'''

def fib(n):
    if n in [0,1]:
        return n
    else:
        return fib(n-1) + fib(n-2)
    
# testing
assert fib(1) == 1
assert fib(2) == 1
assert fib(11) == 89