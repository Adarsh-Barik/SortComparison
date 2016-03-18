# Comparing various sorting algorithms

This repository contains naive python implementation of various sorting algorithms[ Cormen's book as reference](http://www.amazon.com/Introduction-Algorithms-Edition-Thomas-Cormen/dp/0262033844). The repository has two python files :

* `sort.py` : This has python implementation for following sorting algorithms:
	* Insertion sort
	* Merge sort
	* Heap sort
	* Bubble sort
	* Quick sort
	* Randomized quick sort
* `compare.py` : This compares these algorithms for randomly generated data sets of various size (`10,100,500,1000,5000,10000`).

## Some results 
Some plots:

* All algorithms
![alt tag](https://raw.githubusercontent.com/Adarsh-Barik/SortComparison/master/image/lines_all.png)
* Good algorithms
![alt tag](https://raw.githubusercontent.com/Adarsh-Barik/SortComparison/master/image/bar_good.png)
* Not so good algorithms 
![alt tag](https://raw.githubusercontent.com/Adarsh-Barik/SortComparison/master/image/bar_bad.png)