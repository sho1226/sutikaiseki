from math import *
import sys
import numpy as np
import time
import matplotlib.pyplot as plt
sys.path.append('../Lib/')
from graph_anime import init,line_init,line_update

#式及び初期条件
f1 = lambda x:x**3-3*x**2+9*x-8
f2 = lambda x:np.sin(x)
f3 = lambda x:np.cos(x)
f4 = lambda x:np.sin(x/4)-np.cos(x/4)
f5 = lambda x:np.sqrt(np.sin(x)/x)
e = 1e-5

#グラフの生成
func_fig,func_ax = init()
x = np.arange(-10,10,0.1)
y = f5(x)
line = line_init(x,y,func_fig,func_ax)
input("Wait Key...")
y = f2(x)
line = line_update(x,y,func_fig,func_ax,line)
input()

fig,ax = init()
plt.title("Intermediate - The number of iterations")
plt.xlabel("The number of iterations")
plt.ylabel("Intermediate")
plt.grid()

x = np.zeros(1)
y1 = np.zeros(1)
y2 = np.zeros(1)
line1 = line_init(x,y1,fig,ax,marker="o",label="for")
line2 = line_init(x,y2,fig,ax,marker="^",label="dot")
plt.legend(loc='upper left')

#2分法
def dichotomy(xn,xp,f,e):
	xc = (xn+xp)/2
	if abs(f(xc)) < e: return xc
	d = dichotomy
	return d(xn,xc,f,e) if f(xc) > 0 else d(xc,xp,f,e)

if __name__=="__main__":
	"""
	print("f1...")
	dichotomy(xn,xp,f1,e)
	print("f2...")
	dichotomy(xn,xp,f2,e)
	print("f3...")
	dichotomy(xn,xp,f3,e)
	print("f4...")
	dichotomy(xn,xp,f4,e)
	"""