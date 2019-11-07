p=[0, 1, 0, 0, 0]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def move(p, U):
    q = [None] * len(p)
    for k in range(len(p)):
        q[k] = pExact * p[k-U % len(p)] + pOvershoot * p[k-U+1 % len(p)] + pUndershoot * p[k-U-1 % len(p)]
    return q
    

# move 1000 times
for i in range(1000):
    p = move(p, 1)

print(p)


# output for given distribution will be uniform distribution over the time
# which is also called limit distribution