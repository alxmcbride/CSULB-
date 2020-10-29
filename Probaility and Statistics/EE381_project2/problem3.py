import generatorForSAndR as gen

#PROBLEM 3:  #Probability (R=1 | S=1)
def problem3():

    N=100000

    #Generating S,R
    S,R=gen.generatorForSAndR()

    #Keeping track of R=1 and S=1
    numberOfR1=0
    numberOfSuccessesforS=0

    #Comparing S and R
    for k in range(N):
        if (R[k] == 1):
            numberOfR1 += 1
            if (S[k] == 1):
                numberOfSuccessesforS += 1

    #Displaying probabilitiy
    print("Probability of successful transmission when the R bit is 1: ", numberOfSuccessesforS / numberOfR1)

problem3()