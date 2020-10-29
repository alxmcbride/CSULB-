import generatorForSAndR as gen

def problem1():
    N=100000

    #Generating S,R
    S,R = gen.generatorForSAndR()
    numOfErrors = 0

    #Comparing S and R values
    for k in range(N):
        if S[k] != R[k]:
            numOfErrors += 1

     #Displaying probability
    print("Probability of failure during transmission: ",numOfErrors/N)

problem1()

