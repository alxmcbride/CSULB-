import numpy as np
import nSidedDie as nsd
import plotting as plt

#PROBLEM 1: Bernoulli Trials - Experimental

def problem1():
    #The probability vector for the multi - sided dice is:
    p = [0.1, 0.1, 0.1, 0.3, 0.2, 0.2]
    N=10000
    n=1000
    results=np.zeros((N,1))

    for i in range (N): #peforms 10000 experiments
        numOfSucesses=0
        for j in range(n): #performs 1000 trials per experiment
            #roll three dice
             die1=nsd.rollDie(p)
             die2=nsd.rollDie(p)
             die3=nsd.rollDie(p)

            #if succesful, will add to a counter
             if die1==1 and die2==2 and die3==3:
                 numOfSucesses+=1

        results[i]=numOfSucesses #storing number of successes
        print(results[i])

    #plotting results
    plt.plotting(18,results,N)

problem1()