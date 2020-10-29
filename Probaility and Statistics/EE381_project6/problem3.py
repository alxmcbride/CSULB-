#Absorbing States           Transition Probabilities:   a=2/3;  b=3/5;  c=3/10;
import numpy as np
import matplotlib.pyplot as plt
import nSidedDie as nsd

n=15
P=np.array([[1.0,0.0,0.0,0.0,0.0],
            [0.67, 0.0, 0.33, 0.0, 0.0],
            [0.0, 0.6, 0.0, 0.4, 0.0],
            [0.0, 0.0, 0.3, 0.0, 0.7],
            [0.0, 0.0, 0.0, 0.0, 1.0]])

w=[0.0,0.33,0.33,0.33,0.0]

steps=np.linspace(0,n,n+1)
states=np.linspace(0,4,5)
run=np.zeros((n+1,1))
initial=nsd.rollDie(w)
run[0]=initial
print(initial)
next=initial
print(next)

#Plotting a run of the chain
for j in range(1,n+1):
    if  next== 0:
        next= nsd.rollDie(P[0])
    elif next == 1:
        next = nsd.rollDie(P[1])
    elif next== 2:
        next = nsd.rollDie(P[2])
    elif next== 3:
        next = nsd.rollDie(P[3])
    elif next == 4:
          next = nsd.rollDie(P[4])
    print(next)
    run[j]=next
plt.plot(steps,run,'b',linestyle='dotted', marker='o', markerfacecolor='r')
plt.xticks(steps)
plt.yticks(states)
plt.title("A sample simulation of Drunkard's Walk")
plt.xlabel("Step")
plt.ylabel("State")
plt.savefig("Simulation_P3.png")
plt.close('all')

#Problem 4
N=10000
v1=[0.0,0.0,1.0,0.0,0.0]

state_0_ends=0
state_4_ends=0


for i in range(N):
    state= nsd.rollDie(v1)
    for j in range(1,n):
        if state == 0:
            state=nsd.rollDie(P[0])
        elif state == 1:
            state = nsd.rollDie(P[1])
        elif state== 2:
            state= nsd.rollDie(P[2])
        elif state == 3:
            state = nsd.rollDie(P[3])
        elif state == 4:
            state = nsd.rollDie(P[4])
    if state == 0:
      state_0_ends += 1
    elif state == 4:
      state_4_ends += 1

print(state_0_ends/N)
print(state_4_ends/N)

