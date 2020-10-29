import numpy as np
import nSidedDie as nsd

def generatorForSAndR():
    # Setting N, p0, p1
    N = 100000
    p0 = 0.35
    p1 = 1 - p0

    # Creating S - Sent bits
    S = np.zeros((N, 1))

    # Creating list of probablities of bit being 0 or 1 and cumulative sums list
    probs01 = [p0, p1]


    # Creating R - Received bits
    R = np.zeros((N, 1))

    # Setting e0, e1
    e0 = 0.04
    e1 = 0.07

    # Generating 100,000 bits for S and R
    for i in range(N):
        sBit = (nsd.nSidedDie(probs01)) - 1
        S[i] = sBit
        if S[i] == 0:
            rBit = nsd.nSidedDie([1 - e0,e0])-1
            R[i]=rBit
        elif S[i] == 1:
            rBit = nsd.nSidedDie([e1, 1 - e1])-1
            R[i] = rBit
        #print(R[i])
    return S,R