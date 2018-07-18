# -*- coding: utf-8 -*-
"""
Created on Fri Jul 06 14:42:28 2018

@author: yinjiang

The file contains all of the 100,000 integers between 1 and 100,000 (inclusive)
in some order, with no integer repeated.

Your task is to compute the number of inversions in the file given, where the ith
row of the file indicates the ith entry of an array.
implement the fast divide-and-conquer algorithm.

"""
# number of inversions in an unsorted array

# step1: convert txt file into list
l = []
filename = 'IntegerArray.txt'
with open(filename,'r') as f:
    for item in f.readlines():
        l.append(int(item.strip()))

# step2: use merge sort algorithm for split inversion case  
def CountSplitInv(left, right):
    i = 0
    j = 0
    count = 0
    result = []
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        elif left[i] > right[j]:
            result.append(right[j])
            count = count+len(left)-i
            j += 1
    # in case miss some data when one of list finish early
    result += left[i:]
    result += right[j:]
    return result,count

# step3: divide-and-conquer, seperate into three cases
# first two cases use recursive calls          
def SortandCount(A):
    n = len(A)
    if n < 2:
        return (A,0)
    n_2 = n/2
    left = A[0:n_2]
    right = A[n_2:]
    B,X = SortandCount(left)
    C,Y = SortandCount(right)
    D,Z = CountSplitInv(B,C)
    Z = Z+X+Y
    return D, Z

merge_array, inversions = SortandCount(l)           
#if __name__=="__main__":
#    array = [2,3,1,4,5,6]
#    merge_array, inversions = SortandCount(array)
#    print "Start with array: %s;\nSorted array:   %s;\nInversions: %s."%(array, merge_array, inversions)