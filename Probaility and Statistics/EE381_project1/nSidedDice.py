import numpy as np
import plottingP1 as plt1

#######PROBLEM 1########

# rolls the n sided die
def nSidedDie(p):

    #Getting n (number of sides)
    n=len(p)

    # random number between 0 and 1
    randNum = np.random.rand()
    return randNum




# method to perform the experiment
def exp():
    #Setting list for test case
    pList=[0.10,  0.15,  0.20,  0.35, 0.20]

    # Setting N (number of rolls of n-sided dice)
    N = 100000
    outcomes = np.zeros((N, 1))  # N zero arrays with 1 zero element

    cumulProbs = np.cumsum(pList)  # array of sums
    cumulProbs0 = np.append(0, cumulProbs)  # array with 0 added

    for i in range(0, N):
        dieRoll = nSidedDie(pList)
        for j in range(0, len(pList)):
            #checks for the range that the dieRoll is in and get the probability for that range
            if dieRoll > cumulProbs0[j] and dieRoll<= cumulProbs0[j + 1]:
                side = j + 1
                outcomes[i] = side # stores the outcome

    plt1.plotting(len(pList),outcomes,100000) #plotting the PMF

exp()