import inspect
import sys
import numpy as np
import matplotlib.pyplot as plt

def kalmanFilter(data):
    estimated = []
    xk = [0,0]
    R = [[10**-2, 5*(10**-3)], [5*(10**-3), 10**-2]]
    Q = [[10**-4, 2*(10**-5)], [2*(10**-5), 10**-4]]
    l = 1
    #l=.0001
    P = np.identity(2)*l
    for i in range(len(data)):
        uk = (data[i][0:2])
        zk = (data[i][2:4])

        xkp1 = np.sum([xk,uk],axis=0)
        P = P + Q

        K = np.divide(P,np.sum([P,R]))
        xkp1 = np.sum([xkp1, np.matmul(K, (np.subtract(zk,xkp1)))], axis=0)
        P = np.multiply(np.subtract(np.identity(2), K),P)

        xk = xkp1
        print (xk)
        estimated.append(xk.tolist())

    return estimated

def plot(data, output):
    z_prev = [0,0]
    x_prev = [0,0]
    for i in range(len(data)):
        z = data[i][2:4]
        x = output[i]
        plt.plot([z_prev[0], z[0]], [z_prev[1], z[1]], 'b-o', markersize=3)
        plt.plot([x_prev[0], x[0]], [x_prev[1], x[1]], 'r-o', markersize=3)
        z_prev = z
        x_prev = x
    plt.grid()
    plt.title('Observed vs. Estimated')
    plt.xlabel('$x_1$')
    plt.ylabel('$x_2$')
    plt.legend(['Observed State', 'Estimated State'])
    plt.show()
    return
