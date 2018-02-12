import matplotlib.pyplot as plt
import random

'''
对几个数组绘制折线图
'''
def plot_data(x=[], data=[[]], labels=[], title = "T=???", show=False):
	#计算需要的中间变量
	count = len(data)
	if count == 0:
		print("待绘制数据为空！")
		return
	if labels==[]:
		print("自动生成数据的labels")
		for i in range(count):
			labels += ["%04d"%i]
	if count!=len(labels):
		print("数据名称和数据数组个数不符，无法绘制")
		return
	length = []
	alldata = []
	for i in range(count):
		length += [len(data[i])]
		alldata += data[i]
	dataMin = min(alldata)
	dataMax = max(alldata)	
	lenMax = max(length)
	#生成颜色数据
	if count<=7:
		colors="bgryckm"
	else:
		colors = []
		for i in range(count):
			random.seed()
			(r,g,b)=random.randint(0,0x7f), random.randint(0x7f,0xff), random.randint(0,0xff)
			if i%3==0:
				colors += [ '#%02x%02x%02x'%(r,g,b)]
			if i%3==1:
				colors += [ '#%02x%02x%02x'%(b,r,g)]
			if i%3==2:
				colors += [ '#%02x%02x%02x'%(g,b,r)]
	#折线图初始化配置	
	plt.rcParams['font.sans-serif'] = ['SimHei']  # for Chinese characters
	plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
	fig,ax = plt.subplots()
	plt.title(title)
	plt.grid(True)
	#定义x, y的坐标轴
	ax.set_ylim([dataMin-(dataMax-dataMin)*0.1,dataMax+(dataMax-dataMin)*0.1])    
	if x==[] or len(x)!=lenMax:
		x= range(lenMax)
	#绘制
	for i in range(count):
		plt.plot(x[0:length[i]], data[i], "o-",label=labels[i], color=colors[i])
	plt.legend(loc='best')
	plt.close(0)
	if show==True:
		plt.show()
	return

A=[1,2,3,4,5]
B=[5,6,3,4,8,1,-2]
C=[0.1, 0.4, 10]
x=[4,5,6,7,8,9,10]
plot_data(x, data=[B,C,A],labels=["A", "B","C"], title=u'测试', show=True)
