"""
Program a function that returns a new distribution q, 
shifted to the right by U units. 
If U=0, q should be the same as p.
"""

p=[0, 1, 0, 0, 0]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2

def move(p, U):
    q = [None] * len(p)
    for i in range(len(p)):
        q[i] = p[i-U % len(p)]
    q[0] = p[-1]
            
    return q

print(move(p, 1))