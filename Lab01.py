import sys
import math

#出现6的四位数之和，比出现5的四位数之和，多多少？
five=set([])
six=set([])
for i in range(1000, 9999):
	st=str(i)
	if st.find('5')>=0:
		five.add(i)
	if st.find('6')>=0:
		six.add(i)
print("交集 %s" %sorted(list(five & six)))
print("有5没6 %s" %sorted(list(five - six)))
print("有6没5 %s" %sorted(list(six -five)))
sumA=sum(list(five - six))
sumB=sum(list(six -five))
print(len(list(six - five)))
print("sum5=%d, sum6=%d, diff=%d" %(sumA, sumB, sumB-sumA))

temp=[]
for i in range(100,1000):
	st=str(i)
	if (st.find('5')==-1):
		temp.append(i)
print(temp)
print(len(temp))
