#Google PageRank Problem
import numpy as np
import matplotlib.pyplot as plt

n=20 #number of steps
steps=np.linspace(0,n,n+1)
#State Transition Matrix
P=np.array([[0.0,1.0,0.0,0.0,0.0],
            [0.5, 0.0, 0.5, 0.0, 0.0],
            [0.33, 0.33, 0.0, 0.0, 0.33],
            [1.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.33, 0.33, 0.33, 0.0]])

#Initial Probability vector v1

v1=[0.2,0.2,0.2,0.2,0.2]

A_probs=np.zeros((n+1,1))
B_probs=np.zeros((n+1,1))
C_probs=np.zeros((n+1,1))
D_probs=np.zeros((n+1,1))
E_probs=np.zeros((n+1,1))
A_probs[0]=v1[0]
B_probs[0]=v1[1]
C_probs[0]=v1[2]
D_probs[0]=v1[3]
E_probs[0]=v1[4]

for i in range(1,n+1):
    v1 = np.dot(v1, P)
    print(v1)
    A_probs[i]=v1[0]
    B_probs[i]=v1[1]
    C_probs[i]=v1[2]
    D_probs[i]=v1[3]
    E_probs[i]=v1[4]


plt.plot(steps,A_probs,'C0',linestyle='dotted', marker='o', markerfacecolor='C0', label= 'Page A')
plt.plot(steps,B_probs,'C1',linestyle='dotted', marker='o', markerfacecolor='C1', label= 'Page B')
plt.plot(steps,C_probs,'C2',linestyle='dotted', marker='o', markerfacecolor='C2', label= 'Page C')
plt.plot(steps,D_probs,'C3',linestyle='dotted', marker='o', markerfacecolor='C3', label= 'Page D')
plt.plot(steps,E_probs,'C4',linestyle='dotted', marker='o', markerfacecolor='C4', label= 'Page E')
plt.legend(loc = "upper right")
plt.xticks(steps)
plt.title("Calculated probabilities of Pages A-E for v1")
plt.xlabel("Step")
plt.ylabel("State")
plt.savefig("PageRankResult_v1.png")
plt.close("all")

#Initial Probability vector v1
print()

v2=[0.0,0.0,0.0,0.0,1.0]

A_probs=np.zeros((n+1,1))
B_probs=np.zeros((n+1,1))
C_probs=np.zeros((n+1,1))
D_probs=np.zeros((n+1,1))
E_probs=np.zeros((n+1,1))
A_probs[0]=v2[0]
B_probs[0]=v2[1]
C_probs[0]=v2[2]
D_probs[0]=v2[3]
E_probs[0]=v2[4]

for i in range(1,n+1):
    v2 = np.dot(v2, P)
    print(v2)
    A_probs[i]=v2[0]
    B_probs[i]=v2[1]
    C_probs[i]=v2[2]
    D_probs[i]=v2[3]
    E_probs[i]=v2[4]

plt.plot(steps,A_probs,'C0',linestyle='dotted', marker='o', markerfacecolor='C0', label= 'Page A')
plt.plot(steps,B_probs,'C1',linestyle='dotted', marker='o', markerfacecolor='C1', label= 'Page B')
plt.plot(steps,C_probs,'C2',linestyle='dotted', marker='o', markerfacecolor='C2', label= 'Page C')
plt.plot(steps,D_probs,'C3',linestyle='dotted', marker='o', markerfacecolor='C3', label= 'Page D')
plt.plot(steps,E_probs,'C4',linestyle='dotted', marker='o', markerfacecolor='C4', label= 'Page E')
plt.legend(loc = "upper right")
plt.xticks(steps)
plt.title("Calculated probabilities of Pages A-E for v2")
plt.xlabel("Step")
plt.ylabel("State")
plt.savefig("PageRankResult_v2.png")
plt.close("all")