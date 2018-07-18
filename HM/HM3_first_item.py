# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 20:51:38 2018

@author: yinjiang
"""
# quick sort in a unsorted array

# step 1: convert txt file into array
l = []
filename = 'QuickSort.txt'
with open(filename, 'r') as f:
    for item in f.readlines():
        l.append(int(item.strip()))
        
# step 2: quick sort helper function
def QsortHelper(A, left, right):
    # as long as left < right, keep go deeper, if left=right, no need to sort
    if left < right:
        # keep track of comparison times
        c = right - left
        global count
        count = count + c
        # choose pivot on first item
        # no need manipulation on array
        # partition based on pivot
        boundary = partition(A, left, right)
        # two recursive calls
        QsortHelper(A, left, boundary-1)
        QsortHelper(A, boundary+1, right)
        # do not need return anything, after swapping, A will be sorted
    
def partition(A, left, right): 
    p = A[left]
    i = left+1
    for j in range(left+1,right+1):
        if A[j] < p:
            # smaller element needs swap
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
            i = i+1
    # swap pivot to correct (i-1)th position
    # now i point to 1st item > p
    temp = A[i-1]
    A[i-1] = A[left]
    A[left] = temp
    # return the correct pivot position
    return i-1
    
def Qsort(l):
    global count
    count=0
    length = len(l)
    QsortHelper(l, 0, length-1)
    return count        
    
#test = l[:9]
#print test
#total = Qsort(test)
#print total

total = Qsort(l)
print l
print total