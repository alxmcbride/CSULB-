import numpy as np

#Setting the constant values
N=1000  #number of experiments
m=70000
k=9
n=26**4  #number of possible 4 letter words

#Part 1- Hacker generates m passwords
# numOfSuccessP1=0
# for i in range(N):
#     password = np.random.randint(0,n)
#
#     hackerList=np.random.randint(0,n,m)
#
#     if password in hackerList:
#              numOfSuccessP1+=1
#
# print("Probability of successful attempt with m passwords:", numOfSuccessP1/N)
#
# #Part 2- Hacker generates k*m passwords
# numOfSuccessP2=0
# for i in range(N):
#     password = np.random.randint(0,n)
#
#     hackerList=np.random.randint(0,n,k*m)
#
#     if password in hackerList:
#              numOfSuccessP2+=1
#
# print("Probability of successful attempt with k*m passwords:", numOfSuccessP2/N)

#Part 3 - Find m where the probability of success is 0.5
numOfSuccessP3=0
m2=350000
for i in range(N):
    password = np.random.randint(0,n)

    hackerList=np.random.randint(0,n,m2)

    if password in hackerList:
             numOfSuccessP3+=1

print("Probability of successful attempt:", numOfSuccessP3/N)




















