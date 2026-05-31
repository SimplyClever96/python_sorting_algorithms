"""
Name: quick_sort.py
Author: Kevin Warschkow
Created: 31.05.2026
License: MIT
Task: Implement the quick sort algorithm to sort a list and return a new sorted list.
"""

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