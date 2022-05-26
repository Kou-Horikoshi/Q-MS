import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
from matplotlib import animation
import mpl_toolkits.mplot3d.axes3d as p3
import os
from mpl_toolkits.mplot3d import Axes3D
import math



plt.rcParams['font.family'] = 'Helvetica'
plt.rcParams['font.size'] = 16
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['xtick.major.width'] = 1.0
plt.rcParams['ytick.major.width'] = 1.0
plt.rcParams['lines.linewidth'] = 2



#イオンの電荷
z = 1*1.60217662*(10**(-19))
#交流電圧
u = 83
#イオンの質量
m = 202*1.660540*(10**(-27))
#筒の半径
r = 0.0026
#周波数
w = 14.2 * (10**6)
#直流電圧
ev = 497


def f(x, v, t):
    return -w*w/2/2*(2*q*np.cos(w*t) + a)*x

q = 4*z*ev/m/r/r/w/w
a = 8*z*u/m/r/r/w/w

t0 = 0.0
t1 = 25  /(10**6)
N = 10000

del_t = (t1-t0)/N # time grid

tpoints = np.arange(t0, t1, del_t)
xpoints = []
vpoints = []
ypoints = []
zpoints = []
vz = np.sqrt((2*z*20)/m)
# initial condition
x0 = 0.0001
v0 = 0 # m/s/s

x, v = x0, v0


for t in tpoints:
    xpoints.append(x)
    vpoints.append(v)
    k1v =f(x, v, t)*del_t
    k1x = v * del_t

    k2v =  f(x+k1x/2, v+k1v/2, t+del_t/2 )*del_t
    k2x =(v+k1v/2)*del_t

    k3v =f (x+k2x/2, v+k2v/2, t+del_t/2 )*del_t
    k3x =(v+k2v/2 ) *del_t

    k4v = f(x+k3x, v+k3v, t+del_t/2 )*del_t
    k4x = (v+k3v )*del_t

    v += (k1v + 2 * k2v + 2* k3v + k4v)/6
    x += (k1x + 2 * k2x + 2* k3x + k4x)/6


for item in tpoints:
    zpoints.append(item*vz)

xpoints_2 =[]
for item in xpoints:
    a = item*1000
    xpoints_2.append(a)
tpoints_2 = []
for item in tpoints:
    c = item*10**6
    tpoints_2.append(c)


def f(y, v, t):
    return w*w/2/2*(2*q*np.cos(w*t) + a)*y

q = 4*z*ev/m/r/r/w/w
a = 8*z*u/m/r/r/w/w

tpoints = np.arange(t0, t1, del_t)
vpoints = []
ypoints = []


# initial condition
y0 = 0.0001
v0 = 0 # m/s/s
y, v = y0, v0

for t in tpoints:
    ypoints.append(y)
    vpoints.append(v)
    k1v =f(y, v, t)*del_t
    k1y = v * del_t

    k2v =  f(y+k1y/2, v+k1v/2, t+del_t/2 )*del_t
    k2y =(v+k1v/2)*del_t

    k3v =f(y+k2y/2, v+k2v/2, t+del_t/2 )*del_t
    k3y =(v+k2v/2 ) *del_t

    k4v = f(y+k3y, v+k3v, t+del_t/2 )*del_t
    k4y = (v+k3v )*del_t

    v += (k1v + 2 * k2v + 2* k3v + k4v)/6
    y += (k1y + 2 * k2y + 2* k3y + k4y)/6

ypoints_2 = []
for item in ypoints:
    b = item*1000
    ypoints_2.append(b)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

def kakunin():
    ax.scatter(tpoints_2, xpoints_2, ypoints_2, c = "black")# label='ion path')
    ax.set_xlabel("Z")
    ax.set_ylabel("X")
    ax.set_zlabel("Y")
    ax.set_xlim3d(0,10)
    ax.set_ylim3d(-2.5, 2.5)
    ax.set_zlim3d(-2.5, 2.5)
    plt.show()
#kakunin()
#ax = Axes3D(fig)
def gif(mass):
    path = os.path.expanduser('~/Desktop')
    x,y,z = [],[],[]
    def animate(i):
        ax.set_xlabel("Z")
        ax.set_ylabel("X")
        ax.set_zlabel("Y")
        ax.set_xlim3d(0,25)
        ax.set_ylim3d(-2.5, 2.5)
        ax.set_zlim3d(-2.5, 2.5)

        # 描画データを追加
        x.append(tpoints_2[i])
        y.append(xpoints_2[i])
        z.append(ypoints_2[i])

        # 描画
        ax.plot(x, y, z, color="black")

    ani = animation.FuncAnimation(fig, animate, frames=range(0, 10000, 50), interval = 1)
    #plt.show()
    ani.save("{}/{}.gif".format(path, mass), writer="pillow")
gif("2022")
