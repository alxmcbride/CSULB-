import matplotlib.pyplot as plt
import numpy as np
import math
# #Setting the values
N=1200000; mu=45; sigma=3; n=180 #ranges from 1 to 180

# #Creating N X variables
B=np.random.normal(mu,sigma,N)
#
#Creating graph for confidence interval
pos_interval_95=np.zeros((n,1))
neg_interval_95=np.zeros((n,1))
pos_interval_99=np.zeros((n,1))
neg_interval_99=np.zeros((n,1))



sample_sizes = list(range(1,n+1))
for i in sample_sizes:
    X=np.random.choice(B,i)
    X_bar=np.mean(X)
    S_hat=sigma/np.sqrt(i)
    print(S_hat)
    plt.figure(0)
    plt.plot(i, X_bar, 'b', marker="x")
    plt.figure(1)
    plt.plot(i, X_bar, 'b', marker="x")
    neg_interval_95[i-1] = mu - 1.96*S_hat
    pos_interval_95[i-1]= mu + 1.96*S_hat
    neg_interval_99[i - 1] = mu - 2.58* S_hat
    pos_interval_99[i - 1] = mu + 2.58 * S_hat

plt.figure(0)
plt.title("Sample means and 95% confidence intervals")
plt.xlabel("Sample Size")
plt.ylabel("X_bar")
plt.plot(sample_sizes, neg_interval_95,'r',linestyle='--')
plt.plot(sample_sizes, pos_interval_95,'r',linestyle='--')
plt.axhline(mu,color='k')

plt.savefig("95%.png")

plt.figure(1)
plt.title("Sample means and 99% confidence intervals")
plt.xlabel("Sample Size")
plt.ylabel("X_bar")
plt.plot(sample_sizes, neg_interval_99,'g',linestyle='--')
plt.plot(sample_sizes, pos_interval_99,'g',linestyle='--')
plt.axhline(mu,color='k')

plt.savefig("99%.png")
plt.close("all")

#Problem 2
# size 5
n=120; M=10000; z=1.96 ;t=1.98  #change t when n changes
numOfSuccess__normal_95=0
numOfSuccess__t_95=0
for i in range(M):
 X = np.random.choice(B, n)
 X_bar=sum(X)/n
 total=0
 for x in X:
    total+=((x-X_bar)**2)
 S_hat=np.sqrt(total/(n-1))

 pos_interval_normal_95=X_bar+z*(S_hat/np.sqrt(n))
 neg_interval_normal_95=X_bar-z*(S_hat/np.sqrt(n))

 if mu <= pos_interval_normal_95 and mu >= neg_interval_normal_95:
     numOfSuccess__normal_95+=1

 pos_interval_t_95=X_bar+t*(S_hat/np.sqrt(n))
 neg_interval_t_95=X_bar-t*(S_hat/np.sqrt(n))

 if mu <= pos_interval_t_95 and mu >= neg_interval_t_95:
     numOfSuccess__t_95+=1

normal_percent_95 = numOfSuccess__normal_95/M
print(normal_percent_95)
t_percent_95 = numOfSuccess__t_95/M
print(t_percent_95)

z = 2.58;
t = 2.62  # change z and t when n changes
numOfSuccess__normal_99=0
numOfSuccess__t_99=0
for i in range(M):
 X = np.random.choice(B, n)
 X_bar=sum(X)/n
 total=0
 for x in X:
    total+=((x-X_bar)**2)
 S_hat=np.sqrt(total/(n-1))

 pos_interval_normal_99=X_bar+z*(S_hat/np.sqrt(n))
 neg_interval_normal_99=X_bar-z*(S_hat/np.sqrt(n))

 if mu <= pos_interval_normal_99 and mu >= neg_interval_normal_99:
     numOfSuccess__normal_99+=1

 pos_interval_t_99=X_bar+t*(S_hat/np.sqrt(n))
 neg_interval_t_99=X_bar-t*(S_hat/np.sqrt(n))

 if mu <= pos_interval_t_99 and mu >= neg_interval_t_99:
     numOfSuccess__t_99+=1

normal_percent_99 = numOfSuccess__normal_99/M
print(normal_percent_99)
t_percent_99 = numOfSuccess__t_99/M
print(t_percent_99)



