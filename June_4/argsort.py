import sys
import copy

def find(n,a):
    for ii in range(len(a)):
        if a[ii] == n:
            return ii

def largest(a):
    current_largest = a[0]
    largest_index = 0
    for ii in range(len(a)-1):
        if current_largest < a[ii+1]:
            current_largest = a[ii+1]
            largest_index = ii + 1
    return(largest_index, current_largest)

def sort(a):
    sorted_list = []
    for ii in range(len(a)):
        largest_index, largest_num = largest(a)
        sorted_list.append(largest_num)
        a.pop(largest_index)
    return(sorted_list)

def argsort(a, b):
    b_copy = copy.deepcopy(b)
    sorted_b = sort(b_copy) 
    sorted_indices = []
    for BVals in sorted_b:
        sorted_indices.append(b.index(BVals)) 
    return(sorted_indices)

a = [1, 2, 3, 4]
b = [66, 11, 33,77 ]
sorted_indices = argsort(a,b)
print(sorted_indices)
