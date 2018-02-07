import sys
import math
import matplotlib.pyplot as plt


#根据T计算不同的衍生函数T1，T2
def cal_arr(T, color = "blue", title = "T=???"):
	T1 = []
	T2 = []
	lenT = len(T)
	for i in range(0, lenT-1):
		T1 += [T[i+1] - T[i]]
		T2 += [float(T1[i])/T[i+1]]
	T1 += [0]
	T2 += [0]
	# show T1
	fig,ax = plt.subplots()
	plt.title(title)
	ax.set_yticks(range(min(T1),max(T1),1))  
	ax.set_ylim([min(T1),max(T1)])  
	plt.plot(T, T1, "x-",label="T(n+1)-T(N)", color=color)
	plt.grid(True) 
	plt.legend(loc='upper center', bbox_to_anchor=(0.2,1))  
	plt.close(0)
	# show T2
	fig,ax = plt.subplots()
	plt.title(title) 
	ax.set_ylim([0,1])  
	plt.plot(T, T2, "x-",label="(T(n+1)-T(N))/T(N=1)", color=color)
	plt.grid(True)  
	plt.legend(loc='upper center', bbox_to_anchor=(0.2,1)) 
	plt.close(0)
	return T1,T2
	
#去重、排序并打印数组
def do_sth(arr):
	arr = list(set(arr))
	arr.sort()
	print(len(arr))
	print(arr)
	return (arr, len(arr))

# part1: cal A & B
A=[]
B=[]
rangeAB = range(0,7+1)
rangeA = range(0,1+1)
rangeB = range(-1,1+1)
for x in rangeAB:
	for y in rangeAB:
		for i in rangeA:
			for j in rangeA:
				A += [i*(2**x)+j*(2**y)]
			for i in rangeB:
				for j in rangeB:
					temp = i*(2**x)+j*(2**y)
					if temp>=0:
						B += [temp]
A, lenA = do_sth(A)
B, lenB = do_sth(B)
				
# part2: Cal C	
C=[]				
rangeC1 = range(0,7+1)
rangeC2 = range(0,5+1)
rangeC3 = range(6,7+1)
rangeC4 = range(0,1+1)
for x in rangeC1:
	for y in rangeC2:			
		for z in rangeC3:
			for i in rangeC4:
				for j in rangeC4:
					for k in rangeC4:
						C += [i*(2**x)+j*(2**y)+k*(2**z)]
C, lenC = do_sth(C)

# part3: show A,B,C
lenMax = max([lenA, lenB, lenC])
maxRes = max(A+B+C)
minRes = min(A+B+C)
fig,ax = plt.subplots() 
ax.set_yticks(range(minRes-10,maxRes+10,20))  
ax.set_ylim([minRes-10,maxRes+10])  
x= range(0, lenMax)
plt.plot(x, A+[0]*(lenMax-lenA), "x-",label="a*2^x+b*2^y")  
plt.plot(x, B+[0]*(lenMax-lenB), "+-",label="a*2^x+b*2^y") 
plt.plot(x, C+[0]*(lenMax-lenC), "*-",label="a*2^x+b*2^y+c*2^z")
plt.grid(True)  
plt.legend(loc='upper center', bbox_to_anchor=(0.2,1))  
plt.close(0)

#part4: Show A,B,C more
cal_arr(A, "blue", "A=a*2^x+b*2^y")
cal_arr(B, "red", "B=a*2^x+b*2^y")
cal_arr(C, "yellow", "C=a*2^x+b*2^y+c*2^z")

# final: show off
plt.show()
