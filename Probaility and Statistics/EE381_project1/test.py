import numpy as np
import matplotlib.pyplot as plt

def main():
    sum2dice(2)


def sum2dice(N):
 d1= np.random.randint(1,7,N)
 d2= np.random.randint(1,7,N)
 s=d1+d2
 b=range(1,15) ; sb=np.size(b)
 #
 h1, bin_edges = np.histogram(s,bins=b)
 b1=bin_edges[0:sb-1]
#
 plt.close('all')
 fig1=plt.figure(1)
 plt.stem(b1,h1,use_line_collection=True)
 plt.title('Stem plot - Sum of two dice')
 plt.xlabel('Sum of two dice')
 plt.ylabel('Number of occurrences')
 fig1.savefig(fname="fig1.pdf")
 #
 fig2=plt.figure(2)
 p1=h1/N
 plt.stem(b1,p1,use_line_collection=True)
 plt.title('Stem plot - Sum of two dice: Probability mass function',
 fontsize=14, fontweight='bold')
 plt.xlabel('Sum of two dice', fontsize=14)
 plt.ylabel('Probability', fontsize=14)
 plt.xticks(b1)
 #fig2.savefig()


main()