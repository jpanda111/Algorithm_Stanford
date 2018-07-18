# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 18:01:05 2018

@author: yinjiang

organize HM3 all combined in class
two benefits
you don't need to pass A all around
you don't need to define global variables to keep track of comparison
you don't need to use 3 different qsort functions for the assignments, you can utilize class's inheriance
"""

# parent class for quick sort
class QuickSort(object):
    
    def __init__(self, text):
        self.textname = text
        self.array = []
        with open(self.textname, 'r') as f:
            for item in f.readlines():
                self.array.append(int(item.strip()))
        self.comparisons = 0
        
    def sort(self):
        length = len(self.array)
        if length > 1:
            self.qsort(0, length-1)
            
    def qsort(self, left, right):
        if left < right:
            boundary = self.partition(left, right)
            self.qsort(left, boundary-1)
            self.qsort(boundary+1, right)
            
    def partition(self, left, right):
        self.comparisons += right - left
        p = left
        i = left+1
        for j in range(left+1, right+1):
            if self.array[j] < self.array[p]:
                self.array[j], self.array[i] = self.array[i], self.array[j]
                i = i + 1
        self.array[i-1], self.array[p] = self.array[p], self.array[i-1]
        return i-1
        
# child class if pivot = first item always
class QsortFirstItemPivot(QuickSort):
    def partition(self, left, right):
        return super(QsortFirstItemPivot, self).partition(left, right)

# child class if pivot = last item always
class QsortLastItemPivot(QuickSort):
    def partition(self, left, right):
        # manipulate array before main partition subroutine
        self.array[left], self.array[right] = self.array[right], self.array[left]
        return super(QsortLastItemPivot, self).partition(left, right)

# child class if pivot = median item always
class QsortMedianItemPivot(QuickSort):
    def partition(self, left, right):
        # manipulate array 
        self.choose_median_pivot(left, right)
        return super(QsortMedianItemPivot, self).partition(left, right)
    
    def choose_median_pivot(self, left, right):
        mid = (right-left)/2 + left
        if self.array[left] <= self.array[mid] <= self.array[right] or self.array[right] <= self.array[mid] <= self.array[left]:
            self.array[left], self.array[mid] = self.array[mid], self.array[left]
        elif self.array[mid] <= self.array[right] <= self.array[left] or self.array[left] <= self.array[right] <= self.array[mid]:
            self.array[left], self.array[right] = self.array[right], self.array[left]
    
# generate main function for more OOP programming style
if __name__=="__main__":
    sorters = (QsortFirstItemPivot('QuickSort.txt'), QsortLastItemPivot('QuickSort.txt'), QsortMedianItemPivot('QuickSort.txt'))      
    for sorter in sorters:
        sorter.sort()
    print(sorters[0].comparisons, sorters[1].comparisons, sorters[2].comparisons)