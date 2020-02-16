import matplotlib.pyplot as plt
import numpy as np
def draw_scatter(n,s):
        
    data = np.loadtxt('F:/results.txt',encoding='utf-8',delimiter=',')
    x1 = data[:,0]
    y1 = data[:,3]
    x2 = np.random.uniform(0,5,n)
    y2 = np.array([3]*n)
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    ax1.set_title('Result Analysis')
    ax1.set_xlabel('gamma-value')
    ax1.set_ylabel('R-value')
    ax1.scatter(x1,y1,s=s,c='k',marker='.')
    ax1.plot(x2,y2,c='b',ls='--')
    plt.xlim(xmax=5,xmin=0)
    plt.show()


draw_scatter(2000,20)
