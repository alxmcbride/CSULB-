import numpy as np
import plottingP1 as plt1
######PROBLEM 2#########

#rolls a fair die
def diceRoll():
    dice=np.random.randint(1,7) #dice 1
    return dice


#method to perform the experiment
def exp():
    #Setting N
    N=100000

    outcomes=np.zeros((N,1))

    for i in range (0,N):
        numOfRolls=0 #keep track of the number of rolls before successful experiment
        while True:
          dice1= diceRoll() #dice 1
          dice2= diceRoll() #dice 2
          sumOfDice= dice1+dice2        #sum of the two dice
          if sumOfDice==7:
             numOfRolls+=1
             outcomes[i]=numOfRolls     #assigns results into outcomes
             break
          else:
             numOfRolls+=1

#Plotting
    plt1.plotting(30,outcomes,100000)

exp()



