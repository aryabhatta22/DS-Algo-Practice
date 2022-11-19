'''
Convert a decimal number to binary using recusrion
'''

def D2B(n):
    if n in [0,1]:
        return n
    else:
        return (n%2) + D2B(int(n/2)) * 10

# testing    
assert D2B(32) == 100000
assert D2B(27) == 11011