#Given the list motions=[1,1] which means the robot 
#moves right and then right again, compute the posterior 
#distribution if the robot first senses red, then moves 
#right one, then senses green, then moves right again, 
#starting with a uniform prior distribution.

p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
motions = [1,1]
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

"""
Function to compute postierior probability given measurement
"""
def sense(p, Z):
    q = [None] * len(p)
    
    for i in range(len(p)):
        if world[i] == Z :
            q[i] = p[i] * pHit
        else :
            q[i] = p[i] * pMiss
    
    n = sum(q)
    
    for j in range(len(q)):
        q[j] /= n
    
    return q

"""
Function that returns a new distribution q, 
shifted to the right by U units 
"""
def move(p, U):
    q = [None] * len(p)
    for k in range(len(p)):
        q[k] = pExact * p[k-U % len(p)] + pOvershoot * p[k-U+1 % len(p)] + pUndershoot * p[k-U-1 % len(p)]
    return q

for i in range(len(motions)) :
    p = sense(p, measurements[i])
    p = move(p, motions[i])

print p  

