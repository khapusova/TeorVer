
import math
d = [0,1,2]
k = [0.16,0.48,0.36]

def mode(d,k):
    kmax = k[0]
    max = 0
    for i in range(len(k)):
        if k[i]>kmax:
            kmax = k[i]
            max = i
    return d[max]

def ME(d,k):
    Me = 0
    for i in range(len(d)):
        Me += d[i]*k[i]
    return Me
def ME2(d,k):
    Me = 0
    for i in range(len(d)):
        Me += k[i]*(d[i])**2
    return Me

print("ME:", ME(d, k ),"    ME^2: ", ME2(d, k))
print("DE", ME2(d,k) - ((ME(d,k))**2))
print("root", math.sqrt(ME2(d,k) - (ME(d,k))**2))
print("mode" ,  mode(d,k))

