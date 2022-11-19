'''
Find GCD (Greatest common Divisior) of two nubers using recursion 
'''

def gcd(num1, num2):
    if num2 == 0:
        return num1
    elif num1 < num2:
        return gcd(num1, num2%num1)
    else:
        return gcd(num2, num1%num2)
        

# testing    
assert gcd(8,12) == 4
assert gcd(96, 128) == 32
assert gcd(128, 96) == 32