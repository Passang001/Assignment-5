#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Problem 1. Sort With Quicksort.
# Please build a function called "quicksort" that uses recursion to define the quicksort algorithm for a list of any length. 
# Build a main script that reads in the list provided, "numbers.txt", and runs it through your quicksort algorithm. 
# The main script should return the finished sorted list as "sorted.txt"
# All 3 files "In_class_assignment_5.py", "numbers.txt", and "sorted.txt" should all be added to your github repository and submitted as a github link.


'''Info on Quicksort Algorithm: 
The Quicksort algorithm is an efficient sorting algorithm developed by British computer scientist Tony Hoare in 1959.

Quicksort is a divide-and-conquer algorithm. Suppose you have a list of objects to sort. You start by choosing an item in the list, called the *pivot item*. 
This can be any item in the list. You then partition the list into two sublists based on the pivot item and recursively sort the sublists.

The steps of the algorithm are as follows:

1. Choose the pivot item.
2. Partition the list into two sublists:
        Those items that are less than the pivot item
        Those items that are greater than the pivot item
3. Quicksort the sublists recursively.
4. Each partitioning produces smaller sublists, so the algorithm is reductive. 

The base cases occur when the sublists are either empty or have one element, as these are inherently sorted. 
 '''


def quicksort(numbers_in_a_list):

#WRITE YOUR CODE HERE FOR THE RECURSIVE SORTING FUNCTION

    return #WHAT DOES IT RETURN?


def main():

# WRITE YOUR MAIN FUNCTION HERE TO READ IN YOUR numbers.txt FILE, RUN THE LIST THROUGH YOUR SORTING ALGORITHM, 
# AND WRITE OUT YOUR FILE

    return #WHAT DOES IT RETURN?


if __name__ == "__main__":
    main()


# In[ ]:


[449, 48, 242, 44, 65, 520, 332, 173, 931, 667, 146, 
 640, 448, 522, 820, 964, 688, 840, 113, 325, 950, 754, 
 999, 723, 909, 956, 255, 972, 111, 543, 282, 443, 362, 
 968, 725, 549, 356, 828, 566, 193, 107, 982, 580, 606, 
 882, 834, 236, 655, 604, 731, 321, 465, 814, 441, 460, 
 277, 29, 476, 126, 382, 101, 27, 135, 944, 307, 220, 51, 
 153, 536, 711, 901, 507, 139, 94, 155, 214, 724, 315, 33, 
 267, 782, 816, 75, 489, 835, 224, 532, 996, 573, 479, 729,
 484, 505, 508, 875, 709, 589, 425, 454, 702]


# In[18]:


###  QUICKSORT
### Reference "https://stackoverflow.com/questions/20175380/quick-sort-python-recursion"
import re
A=[449, 48, 242, 44, 65, 520, 332, 173, 931, 667, 146, 
 640, 448, 522, 820, 964, 688, 840, 113, 325, 950, 754, 
 999, 723, 909, 956, 255, 972, 111, 543, 282, 443, 362, 
 968, 725, 549, 356, 828, 566, 193, 107, 982, 580, 606, 
 882, 834, 236, 655, 604, 731, 321, 465, 814, 441, 460, 
 277, 29, 476, 126, 382, 101, 27, 135, 944, 307, 220, 51, 
 153, 536, 711, 901, 507, 139, 94, 155, 214, 724, 315, 33, 
 267, 782, 816, 75, 489, 835, 224, 532, 996, 573, 479, 729,
 484, 505, 508, 875, 709, 589, 425, 454, 702]
def main():
    r=len(A)-1
    p=0
    Result=QuickSort(A,p,r)
    print(Result)
def QuickSort(A,p,r):

    if p<r:
        q=partition(A, p, r)
        QuickSort(A, p, q-1)
        QuickSort(A, q+1, r)
    return A
def partition(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i=i+1
            a,b=A.index(A[i]), A.index(A[j])
            A[a],A[b]=A[b],A[a]
    d,c=A.index(A[i+1]),A.index(A[r])
    A[c],A[d]=A[d],A[c]
    return i+1
main()


# In[ ]:





# In[ ]:




