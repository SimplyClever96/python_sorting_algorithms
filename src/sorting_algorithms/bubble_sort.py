"""
Name: bubble_sort.py
Author: Kevin Warschkow
Created: 31.05.2026
License: MIT
Task: Implement the bubble sort algorithm to sort a list in-place. The function should take an optional key parameter that specifies a function to be called on each list element prior to making comparisons. The function should also take an optional op parameter that specifies a comparison operator (e.g., operator.gt for greater than, operator.lt for less than) to determine the sorting order. If no op is provided, the default should be operator.gt for ascending order.
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
  


