"""
Name: sort.py
Author: Kevin Warschkow
Created: 21.05.2026
License: MIT
"""
import operator

def bubble_sort(lst, op=operator.gt, key=lambda x: x):
    """This function implements the bubble sort algorithm to sort a list in-place."""
    n = len(lst)
    for i in range(n - 1):
        swapped = False

        for j in range (n - i - 1):
            # if lst[j] > lst[j+1]:     
            if op(key(lst[j]), key(lst[j+1])):
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True

        if not swapped:
            break
    
    return lst # return is not necessary, but it allows to use the function in a functional style, e.g. sorted_lst = bubble_sort(lst)


def quick_sort(lst):
    """This function implements the quick sort algorithm to sort a list and returns a new sorted list."""
    n = len(lst)
    
    if n <= 1:
        return lst
    else:
        pivot = lst[0]
        smaller = [x for x in lst if x < pivot]
        equal = [x for x in lst if x == pivot]
        larger = [x for x in lst if x > pivot]

    return quick_sort(smaller) + equal + quick_sort(larger)    


def merge_sort(lst):
    """This function implements the merge sort algorithm to sort a list and returns a new sorted list."""

    def merge(lst1, lst2):
        lst = []
        i = j = 0

        while i < len(lst1) and j < len(lst2):
            if lst1[i] <= lst2[j]:
                lst.append(lst1[i])
                i += 1
            else:
                lst.append(lst2[j])
                j += 1
        
        lst.extend(lst1[i:])
        lst.extend(lst2[j:])
        return lst

    n = len(lst)

    if n <= 1:
        return lst
    else:
        n1 = n // 2
        lst1 = merge_sort(lst[:n1])
        lst2 = merge_sort(lst[n1:])
        return merge(lst1, lst2)
