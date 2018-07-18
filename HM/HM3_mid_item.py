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
        # choose pivot on median item
        # in order to utilize same partition function, we need to swap array 
        # manipulation when p = A[right] or A[mid]
        mid = (right-left)/2 + left
        if A[left] <= A[mid] <= A[right] or A[right] <= A[mid] <= A[left]:
            temp = A[mid]
            A[mid] = A[left]
            A[left] = temp
        elif A[left] <= A[right] <= A[mid] or A[mid] <= A[right] <= A[left]:
            temp = A[right]
            A[right] = A[left]
            A[left] = temp
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
    
#alist = [2, 20, 1, 15, 3, 11, 13, 6, 16, 10, 19, 5, 4, 9, 8, 14, 18, 17, 7, 12]
#total = Qsort(alist)
#print(alist)
#print(total)
#test = l[:9]
#print test
total = Qsort(l)
print l
print total

#def partition(A, left, right):        
#    mid = (right-left)/2 + left
#    # choose pivot, always choose median item
#    t = [A[left],A[mid],A[right]]
#    p = sorted(t)[1]
#    if p == A[left]:
#        i = left+1
#        for j in range(left+1, right+1):
#            if A[j] < p:
#                temp = A[i]
#                A[i] = A[j]
#                A[j] = temp
#                i = i+1
#        index = i-1
#        temp = A[index]
#        A[index] = A[left]
#        A[left] = temp
#    elif p == A[right]:
#        i = left
#        for j in range(left, right):
#            if A[j] < p:
#                temp = A[i]
#                A[i] = A[j]
#                A[j] = temp
#                i = i+1
#        index = i
#        temp = A[index]
#        A[index] = A[right]
#        A[right] = temp  
#    else:
#        i = left
#        for j in range(left, mid) + range(mid+1,right+1):
#            if A[j] < p:
#                # smaller element needs swap
#                temp = A[i]
#                A[i] = A[j]
#                A[j] = temp
#                i = i+1
#                # move to next if 
#                if i == mid:
#                    i = i+1
#        if mid < i:
#            index = i-1
#            temp = A[index]
#            A[index] = A[mid]
#            A[mid] = temp 
#        elif mid >= i:
#            index = i
#            temp = A[index]
#            A[index] = A[mid]
#            A[mid] = temp 
#            
#    return index