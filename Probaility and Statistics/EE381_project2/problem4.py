import numpy as np
import nSidedDie as nsd


#PROBLEM 4:  #Probability (R=1 | S=1)
def problem4():
    # Setting N, p0, p1
    N = 100000
    p0 = 0.35
    p1 = 1 - p0

    # Creating S - Sent bits
    S = np.zeros((N, 1))

    # Creating list of probablities of bit being 0 or 1 and cumulative sums list
    probs01 = [p0, p1]

    # Generating 100,000 bits for S
    for i in range(N):
        sBit = (nsd.nSidedDie(probs01)) - 1
        S[i] = sBit

    #Creating R
    R = np.zeros((N, 1))

    # Setting e0, e1
    e0 = 0.04
    e1 = 0.07


    #Generating S and 3 bits for R
    numIncorrect=0
    for j in range(N):

        if S[j] == 0:
            rBit1 = nsd.nSidedDie([1 - e0,e0])-1
            rBit2 = nsd.nSidedDie([1 - e0,e0])-1
            rBit3 = nsd.nSidedDie([1 - e0,e0])-1
            threeBits=[rBit1,rBit2,rBit3]
            if sum(threeBits)>=2:
                R[j]=1
            else:
                R[j]=0
        elif S[j] == 1:
            rBit1 = nsd.nSidedDie([e1, 1 - e1])-1
            rBit2 = nsd.nSidedDie([e1, 1 - e1])-1
            rBit3 = nsd.nSidedDie([e1, 1 - e1])-1
            threeBits = [rBit1, rBit2, rBit3]
            if sum(threeBits) >= 2:
                R[j] = 1
            else:
                R[j] = 0

        #Comparing S and R values
        if S[j]!=R[j]:
            numIncorrect+=1

     #Displaying probability
    print("Probability of a message being incorrectly received " ,numIncorrect/N)

problem4()