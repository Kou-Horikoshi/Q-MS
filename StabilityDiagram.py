"""
Sepulchre, Cyrille. Ion guiding, filtering and trapping with a single quadrupole device. Ecole polytechnique de Louvain, Université catholique de Louvain, 2020. Prom. : Lauzin, Clément ; Urbain, Xavier.
https://dial.uclouvain.be/downloader/downloader.php?pid=thesis%3A25238&datastream=PDF_01&cover=cover-mem
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import scipy.special as sp
import matplotlib
plt.rcParams['font.family'] = 'Arial'       # 使用するフォント
plt.rcParams["xtick.direction"] = "out"     # 目盛り線の向き、内側"in"か外側"out"かその両方"inout"か
plt.rcParams["ytick.direction"] = "out"     # 目盛り線の向き、内側"in"か外側"out"かその両方"inout"か
plt.rcParams["axes.labelsize"] = 25         # 軸ラベルのフォントサイズ
#plt.rcParams["xtick.top"] = True            # 上部に目盛り線を描くかどうか
#plt.rcParams["xtick.bottom"] = True         # 下部に目盛り線を描くかどうか
#plt.rcParams["ytick.left"] = True           # 左部に目盛り線を描くかどうか
#plt.rcParams["ytick.right"] = True          # 右部に目盛り線を描くかどうか
plt.rcParams["xtick.major.size"] = 10.0      # x軸主目盛り線の長さ
plt.rcParams["ytick.major.size"] = 10.0      # y軸主目盛り線の長さ
plt.rcParams["xtick.major.width"] = 4.0     # x軸主目盛り線の線幅
plt.rcParams["ytick.major.width"] = 4.0     # y軸主目盛り線の線幅
plt.rcParams["xtick.minor.visible"] = True  # x軸副目盛り線を描くかどうか
plt.rcParams["ytick.minor.visible"] = True  # y軸副目盛り線を描くかどうか
plt.rcParams["xtick.minor.size"] = 6.0      # x軸副目盛り線の長さ
plt.rcParams["ytick.minor.size"] = 6.0      # y軸副目盛り線の長さ
plt.rcParams["xtick.minor.width"] = 2     # x軸副目盛り線の線幅
plt.rcParams["ytick.minor.width"] = 2     # y軸副目盛り線の線幅
plt.rcParams["xtick.labelsize"] = 15        # 目盛りのフォントサイズ
plt.rcParams["ytick.labelsize"] = 15        # 目盛りのフォントサイズ
plt.rcParams["lines.linewidth"] = 3         # グラフの線の太さ
plt.rcParams["legend.frameon"] = False      # 凡例を囲うかどうか、Trueで囲う、Falseで囲わない
plt.rcParams["axes.grid"] = True           # グリッドを表示するかどうか


qu = np.linspace(0,10,1001)
qu_2 = np.linspace(0.1,10,101)
# au = np.linspace(0.18,0.26,101)


fig = plt.figure(figsize = (6,4))
ax = fig.add_subplot(111)

a0 = sp.mathieu_a(0,qu)
a1 = sp.mathieu_a(1,qu)
a2 = sp.mathieu_a(2,qu)
a3 = sp.mathieu_a(3,qu)

b1 = sp.mathieu_b(1, qu)
b2 = sp.mathieu_b(2, qu)
b3 = sp.mathieu_b(3, qu)
b4 = sp.mathieu_b(4, qu)


a0_2 = sp.mathieu_a(0,qu_2)
b1_2 = sp.mathieu_b(1,qu_2)

ax.fill_between(qu,a0,b1,alpha = 0.5,facecolor='blue')#,hatch='|') x安定
ax.fill_between(qu,-a0,-b1,alpha = 0.5,facecolor='red')#,label='stable in y') y安定
#ax.fill_between(qu_2,a0_2,b1_2,alpha = 0.5,facecolor='yellow')#,hatch='|') x安定
#ax.fill_between(qu_2,-a0_2,-b1_2,alpha = 0.5,facecolor='green')#,label='stable in y') y安定


ax.fill_between(qu,a1,b2,alpha = 0.5,facecolor='blue')#,hatch='|',label='stable in x')
ax.fill_between(qu,a2,b3,alpha = 0.5,facecolor='blue')
ax.fill_between(qu,a3,b4,alpha = 0.5,facecolor='blue')
ax.fill_between(qu,-a1,-b2,alpha = 0.5,facecolor='red')
ax.fill_between(qu,-a2,-b3,alpha = 0.5,facecolor='red')
ax.fill_between(qu,-a3,-b4,alpha = 0.5,facecolor='red')



plt.plot(qu,-a0, color = "red")
plt.plot(qu, b1, color = "blue")
plt.plot(qu,-b1, color = "red")
plt.plot(qu, a0, color = "blue")

"""
plt.plot(qu,-a1, color = "red")
plt.plot(qu, a1, color = "blue")
plt.plot(qu,-a2, color = "red")
plt.plot(qu, a2, color = "blue")
plt.plot(qu,-a3, color = "red")
plt.plot(qu, a3, color = "blue")

plt.plot(qu, b2, color = "blue")
plt.plot(qu,-b2, color = "red")
plt.plot(qu, b3, color = "blue")
plt.plot(qu,-b3, color = "red")
plt.plot(qu, b4, color = "blue")
plt.plot(qu,-b4, color = "red")


plt.plot(qu_2,-a0_2, color = "red")
plt.plot(qu_2, a0_2, color = "blue")
plt.plot(qu_2, b1_2, color = "blue")
plt.plot(qu_2,-b1_2, color = "red")
"""
U = 2
V_1 = 150
V_2 = 88
ax.plot(qu, (2*U/ V_1)*qu, color = "yellow")
ax.plot(qu, (2*U/ V_2)*qu, color = "greenyellow")
# plt.legend()


ax.set_xlabel(r'$q_u = \frac{4zV}{mr_0^2\omega^2}$')
ax.set_ylabel(r'$a_u = \frac{8zU}{mr_0^2\omega^2}$')

ax.set_xlim(0,10)
ax.set_ylim(-5,5)

#print(b1)
plt.show()
#plt.savefig("StabilityDiagram", dpi = 600, bbox_inches = "tight")
