import numpy as np
#### PROBLEM 3 #####

#Number of tosses where number of heads is exactly 50
numOfSuccesses=0

#Setting N
N=100000

for i in range (0,N):
  coinToss= np.random.randint(0,2,100) #tosses 100 coins (0= tails, 1=heads)
  total= sum(coinToss) #sum of numbers
  if total==50:  #if total is 50, add one to numOfSuccesses
      numOfSuccesses+=1

#Calculate the probability
prob= numOfSuccesses / N
print("Probability of 50 heads:", prob)






