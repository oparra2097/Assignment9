#pick and plant 
from numpy import *

n = 5
a = [['*'] * n for i in range(n)]

bobby = a[0][0]

a[0][0] = 'k'
a[0][3] = '#'

for row in a:
    print(' '.join(row))
    
    
bobby.hop(3)
bobby.pick()


    
    
bobby.turn(RIGHT)
bobby.hop(2)
bobby.plant()

for row in a:
    print(' '.join(row))

bobby.turn(LEFT)
bobby.hop()

for row in a:
    print(' '.join(row))

def hop(x):
    
    return a[0][0+x] 
    a[0][0+x] = 'K'
    for row in a:
        print(' '.join(row))

def pick():
    
    flower = a[2][3+1]
    a[0+2][3] = '#'
    
    for row in a:
        print(' '.join(row))
      
def turn(enum):
    
    if enum == RIGHT:
        return a[0+2][3]
    
    elif enum == LEFT:
        return a[2][3-1]
