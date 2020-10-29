import numpy as np
import matplotlib.pyplot as plt
import nSidedDie as nsd

#State Transition Matrix  P=[1/3  1/3  1/3;  1/3   1/6   1/2 ;  2/5    1/5    2/5]
p1= [0.33, 0.33, 0.33]
p2= [0.33, 0.17, 0.5]
p3= [0.4, 0.2, 0.4]

#Initial probability distribution vector:  [1/4    0    3/4]
V = [0.25,0.0, 0.75]

#Plotting a run of the chain

N=10000; n=15
states=np.linspace(0,15,16)
run=np.zeros((n+1,1))
initial=nsd.rollDie(V)
run[0]=initial
print(initial)
next=0

#Plotting a run of the chain
for j in range(1,n+1):
    if initial == 1:
        next = nsd.rollDie(p1)
    elif initial== 2:
        next = nsd.rollDie(p2)
    elif initial== 3:
        next = nsd.rollDie(p3)
    run[j]=next
plt.plot(states,run,'b',linestyle='dotted', marker='o', markerfacecolor='r')
plt.xticks(states)
plt.yticks(run)
plt.title("A sample simulation of a 3-state Markov Chain")
plt.xlabel("Step")
plt.ylabel("State")
plt.savefig("Simulation.png")
plt.close('all')

#Plotting based off 10,000 runs
state_1_probs= np.zeros((n+1,1))
state_2_probs= np.zeros((n+1,1))
state_3_probs= np.zeros((n+1,1))

for i in range(N):
    state= nsd.rollDie(V)
    if state== 1: state_1_probs[0]+=1
    elif state == 2: state_2_probs[0]+=1
    elif state == 3: state_3_probs[0]+=1
    for j in range(1,n+1):
        if state ==1:
            state=nsd.rollDie(p1)
        elif state == 2:
            state = nsd.rollDie(p2)
        elif state == 3:
            state = nsd.rollDie(p3)
        if state == 1:
            state_1_probs[j] += 1
        elif state == 2:
            state_2_probs[j] += 1
        elif state == 3:
            state_3_probs[j] += 1


plt.plot(states,(state_1_probs/N),'C0',linestyle='dotted', marker='o', markerfacecolor='C0', label= 'State 1')
plt.plot(states,(state_2_probs/N),'C1',linestyle='dotted', marker='o', markerfacecolor='C1', label= 'State 2')
plt.plot(states,(state_3_probs/N),'C2',linestyle='dotted', marker='o', markerfacecolor='C2', label= 'State 3')
plt.legend(loc = "upper right")
plt.xticks(states)
plt.title("Simulated 3-state Markov Chain")
plt.xlabel("Step")
plt.ylabel("State")
plt.savefig("SimulatedResult.png")
plt.close("all")

#Plotting based off calculated probabilities
state_1_probs= np.zeros((n+1,1))
state_2_probs= np.zeros((n+1,1))
state_3_probs= np.zeros((n+1,1))
st=np.array([p1,p2,p3])
w=V
state_1_probs[0]=w[0]
state_2_probs[0]=w[1]
state_3_probs[0]=w[2]

for i in range(1,n+1):
    w=np.dot(w,st)
    print(w)
    state_1_probs[i] = w[0]
    state_2_probs[i] = w[1]
    state_3_probs[i] = w[2]

plt.plot(states,state_1_probs,'C0',linestyle='dotted', marker='o', markerfacecolor='C0', label= 'State 1')
plt.plot(states,state_2_probs,'C1',linestyle='dotted', marker='o', markerfacecolor='C1', label= 'State 2')
plt.plot(states,state_3_probs,'C2',linestyle='dotted', marker='o', markerfacecolor='C2', label= 'State 3')
plt.legend(loc = "upper right")
plt.xticks(states)
plt.title("Calculated 3-state Markov Chain")
plt.xlabel("Step")
plt.ylabel("State")
plt.savefig("CalculatedResult.png")
plt.close("all")























 

