p=[0.2, 0.2, 0.2, 0.2, 0.2]                         # probability
world=['green', 'red', 'red', 'green', 'green']     # world
measurements = ['red', 'green']                     # measurement
pHit = 0.6                                          # probability if hit
pMiss = 0.2                                         # probability if miss

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

# finding postierior distribution for multiple measurement
for k in range(len(measurements)):
    p = sense(p, measurements[k])

print(p)