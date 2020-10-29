import numpy as np
def nSidedDie(p):
    #Getting n (number of sides)
    n=len(p)

    #Setting up the cumulative sum
    cumulProbs = np.cumsum(p)  # array of sums
    cumulProbs0 = np.append(0, cumulProbs)

    #random number between 0 and 1
    randNum = np.random.rand()
    for j in range(0, len(p)):
        # checks for the range that the dieRoll is in and get the probability for that range
        if randNum > cumulProbs0[j] and randNum <= cumulProbs0[j + 1]:
            side = j+1
            return side
    return 0;