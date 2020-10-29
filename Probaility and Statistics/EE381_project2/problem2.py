import generatorForSAndR as gen

#PROBLEM 2:  #Probability (S=1 | R=1)

def problem2():

    N = 100000

    #Generating S,R
    S, R = gen.generatorForSAndR()

    #Keeping track of S=1 and R=1
    numberOfS1 = 0
    numberOfSuccessesforR = 0

    #Comparing S,R
    for k in range(N):
     if (S[k] == 1):
        numberOfS1 += 1
        if (R[k] == 1):
            numberOfSuccessesforR += 1

     #Displaying Probability
    print("Probability of successful transmission when the S bit is 1: ", numberOfSuccessesforR / numberOfS1)

problem2()