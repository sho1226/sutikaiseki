import matplotlib.pyplot as plt
#-------------------------------------------------------
#初期化
def init():
	#キャンバスの作成
	fig, ax = plt.subplots()
	#キャンバスの表示
	fig.show()
	fig.canvas.draw()
	fig.canvas.flush_events()
	return fig,ax

#軸の更新
def axis_update(x,y,ax):
	xlim_min,xlim_max = ax.get_xlim()
	if x.min() < xlim_min:
		ax.set_xlim([x.min(),xlim_max])
		xlim_min = x.min()
	if x.max() > xlim_max:
		ax.set_xlim([xlim_min,x.max()*1.1])

	ylim_min,ylim_max = ax.get_ylim()
	if y.min() < ylim_min:
		ax.set_ylim([y.min(),ylim_max])
		ylim_min = y.min()
	if y.max() > ylim_max:
		ax.set_ylim([ylim_min,y.max()*1.1])
#-------------------------------------------------------
#折れ線グラフ
def line_init(x,y,fig,ax,marker = "",label = ""):
	#新しいLineの作成
	line, = ax.plot(x,y,marker = marker,label = label)
	#軸の更新
	axis_update(x,y,ax)
	#キャンバスの更新
	fig.canvas.draw()
	fig.canvas.flush_events()
	return line

def line_update(x,y,fig,ax,line):
	#lineの値の更新
	line.set_xdata(x)
	line.set_ydata(y)
	#軸の更新
	axis_update(x,y,ax)
	#キャンバスの更新
	fig.canvas.draw()
	fig.canvas.flush_events()
#-------------------------------------------------------


