## A compilation of various sorting techniques
from numpy import *
import random	

# INSERTION SORT
def INSERTIONSORT(A):
	s=shape(A)[0]
	for i in range(s):
		key = A[i]
		j=i-1
		while (j>0 and A[j]>key):
			A[j+1]=A[j]
			j=j-1
		A[j+1]=key
	return A
	
# MERGE SORT
def MERGE(A,p,q,r):
	"""Merges sorted array from (p,q) and (q+1,r)"""
	n1 = q-p+1
	n2 = r-q
	L=[];R=[]
	for i in range(n1):
		L.append(A[p+i-1])
	for j in range(n2):
		R.append(A[q+j])
	L.append(float('inf'))
	R.append(float('inf'))
	i=0;j=0
	for k in range(p-1,r):
		if L[i]<=R[j]:
			A[k]=L[i]
			i=i+1
		else:
			A[k]=R[j]
			j=j+1
def MERGESORT(A,p,r):
	"""Merge sort"""
	if p<r:
		q=int(floor((p+r)*0.5))
		MERGESORT(A,p,q)
		MERGESORT(A,q+1,r)
		MERGE(A,p,q,r)
	return A
	
# BUBBLE SORT
def BUBBLESORT(A):
	s=shape(A)[0]
	for i in range(s):
		for j in range(s-1,i,-1):
			if A[j]<A[j-1]:
				temp = A[j]
				A[j] = A[j-1]
				A[j-1]=temp
	return A
	
# HEAP SORT 
PARENT =lambda i : i/2
LEFT = lambda i: 2*i
RIGHT = lambda i:2*i+1
def MAXHEAPIFY(A,i,s):
	l = LEFT(i)
	r = RIGHT(i)
	if (l<=s and A[l-1]>A[i-1]):
		largest = l
	else:
		largest=i
	if r<=s and A[r-1]>A[largest-1]:
		largest = r
	if largest != i:
		temp=A[i-1]
		A[i-1]=A[largest-1]
		A[largest-1]=temp
		MAXHEAPIFY(A,largest,s)
		
def BUILDMAXHEAP(A,s):
	for i in range(int(floor(s/2))-2,0,-1):
		MAXHEAPIFY(A,i,s)

def HEAPSORT(A):
	size = shape(A)[0]
	BUILDMAXHEAP(A,size)	
	for i in range(size,1,-1):
		temp=A[0]			
		A[0]=A[i-1]
		A[i-1]=temp
		size=size-1
		MAXHEAPIFY(A,1,size)
	return A
	
# QUICK SORT

def PARTITION(A,p,r):
	x=A[r-1]
	i = p-1
	for j in range(p,r):
		if A[j-1]<=x:
			i=i+1
			temp=A[i-1]
			A[i-1]=A[j-1]
			A[j-1]=temp
	temp1=A[i]
	A[i]=A[r-1]
	A[r-1]=temp1
	return i+1
	
def QUICKSORT(A,p,r):
	if p<r:
		q=PARTITION(A,p,r)
		QUICKSORT(A,p,q-1)
		QUICKSORT(A,q+1,r)
		
	
def RANDPARTITION(A,p,r):
	i=random.randint(p,r)
	temp2=A[r-1]
	A[r-1]=A[i-1]
	A[i-1]=temp2
	return PARTITION(A,p,r)
	
def RANDQUICKSORT(A,p,r):
	if p<r:
		q=RANDPARTITION(A,p,r)
		RANDQUICKSORT(A,p,q-1)
		RANDQUICKSORT(A,q+1,r)
