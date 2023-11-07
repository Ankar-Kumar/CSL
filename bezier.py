import matplotlib.pyplot as plt
import numpy as np
import math

def fact(num):
    t=1
    for i in range(1,num+1):
        t*=i
    return t
def Bezier(x, y,n):
    nfact = fact(n - 1)
    x_curve=[]
    y_curve=[]
    for t in range(0, 1001):
        t /= 1000.0
        xt, yt = 0, 0
        for i in range(n):
            b = (nfact * math.pow(t, i) * math.pow(1 - t, n - 1 - i)) / (fact(n - 1 - i) * fact(i))
            xt += b * x[i]
            yt += b * y[i]
        # print(xt,yt)
        x_curve.append(xt)
        y_curve.append(yt)
        plt.plot(x_curve,y_curve,color='red')
        plt.xlim([0,500])
        plt.ylim([0,500])
        # plt.pause(0.01)
    for i in range(4):
         plt.scatter(x[i],y[i], marker='o',color='green')


n = int(input("Number of control points: "))
x = []
y = []

# Input control points
print("Enter the control points (x, y):")
for _ in range(n):
    point = input().split()
    x.append(int(point[0]))
    y.append(int(point[1]))
# print(x,y)

Bezier(x,y,n)

plt.show()