#Modify your code so that it normalizes the output for 
#the function sense. This means that the entries in q 
#should sum to one.

p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red','green']
pHit = 0.6
pMiss = 0.2

def sense(p, measurements):
    q=[]
    for i in range(len(p)):
        hit = (measurements == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    norm = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / norm
    return q

print(sense(p,measurements))


