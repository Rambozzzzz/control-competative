import math

def perfect_square_root(a):
    root = int(math.sqrt(a))
    if root * root == a:
        return root
    else:
        return -1

print(perfect_square_root(25))  
print(perfect_square_root(26))  
