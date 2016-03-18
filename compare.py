from sort import *
from time import clock
from numpy import random
from sys import setrecursionlimit
from matplotlib import pyplot as pl

setrecursionlimit(15000)
ins=[]
mer=[]
heap=[]
bubble=[]
quick=[]
rquick=[]
points1=[10,100,500,1000,5000,10000]
for i in points1:
	A=random.rand(int(i),)
	fname = 'A'+str(int(i))+'.txt'
	savetxt(fname,A)
	#points.append(int(i))
	start=clock()
	INSERTIONSORT(A)
	ins.append(clock()-start)
	start=clock()
	MERGESORT(A,1,shape(A)[0])
	mer.append(clock()-start)
	start=clock()
	HEAPSORT(A)
	heap.append(clock()-start)
	start=clock()
	BUBBLESORT(A)
	bubble.append(clock()-start)
	start=clock()
	QUICKSORT(A,1,shape(A)[0])
	quick.append(clock()-start)
	start=clock()
	RANDQUICKSORT(A,1,shape(A)[0])
	rquick.append(clock()-start)
pl.figure(1)
pl.plot(points1,ins,'b',points1,mer,'r',points1,heap,'k',points1,bubble,'green',points1,quick,'y',points1,rquick,'brown')
pl.legend(['Insertion Sort','Merge Sort','Heap Sort','Bubble Sort','Quick Sort','Randomized Quick Sort'],loc='upper left')
pl.xlabel('Number of data points')
pl.ylabel('CPU time in seconds')
pl.show()
pl.figure(2)
pl.plot(points1,mer,'r',points1,heap,'green',points1,rquick,'b')
pl.legend(['Merge Sort','Heap Sort','Randomized Quick Sort'],loc='upper left')
pl.xlabel('Number of data points')
pl.ylabel('CPU time in seconds')
pl.show()

pl.figure(3)
dummy_points = range(len(points1))
dummy_points1 = [3*x for x in dummy_points]
pl.bar([x-1.2 for x in dummy_points1], ins,width=0.4,color='b',align='center')
pl.bar([x-0.8 for x in dummy_points1], mer,width=0.4,color='r',align='center')
pl.bar([x-0.4 for x in dummy_points1], heap,width=0.4,color='k',align='center')
pl.bar([x for x in dummy_points1], bubble,width=0.4,color='green',align='center')
pl.bar([x+0.4 for x in dummy_points1], quick,width=0.4,color='y',align='center')
pl.bar([x+0.8 for x in dummy_points1], rquick,width=0.4,color='brown',align='center')
pl.legend(['Insertion Sort','Merge Sort','Heap Sort','Bubble Sort','Quick Sort','Randomized Quick Sort'],loc='upper left')
pl.xlabel('Number of data points')
pl.ylabel('CPU time in seconds')
pl.xticks(dummy_points1, [str(x) for x in points1])
pl.autoscale(tight=True)
pl.show()

pl.figure(4)
dummy_points = range(len(points1))
dummy_points1 = [3*x for x in dummy_points]
pl.bar([x-0.4 for x in dummy_points1], mer,width=0.4,color='k',align='center')
pl.bar([x for x in dummy_points1], heap,width=0.4,color='green',align='center')
pl.bar([x+0.4 for x in dummy_points1], rquick,width=0.4,color='y',align='center')
pl.legend(['Merge Sort','Heap Sort','Randomized Quick Sort'],loc='upper left')
pl.xlabel('Number of data points')
pl.ylabel('CPU time in seconds')
pl.xticks(dummy_points1, [str(x) for x in points1])
pl.autoscale(tight=True)
pl.show()

pl.figure(5)
dummy_points = range(len(points1))
dummy_points1 = [3*x for x in dummy_points]
pl.bar([x-0.4 for x in dummy_points1], ins,width=0.4,color='k',align='center')
pl.bar([x for x in dummy_points1], bubble,width=0.4,color='green',align='center')
pl.bar([x+0.4 for x in dummy_points1], quick,width=0.4,color='y',align='center')
pl.legend(['Insertion Sort','Bubble Sort','Quick Sort'],loc='upper left')
pl.xlabel('Number of data points')
pl.ylabel('CPU time in seconds')
pl.xticks(dummy_points1, [str(x) for x in points1])
pl.autoscale(tight=True)
pl.show()

