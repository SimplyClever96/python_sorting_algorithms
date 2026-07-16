"""
Name: selection_sort.py
Author: Kevin Warschkow
Created: 16.07.2026
License: MIT
Task: Implement the selection sort algorithm to sort a list in-place.
Input: Field of numbers (list)
Output: Sorted field of numbers (list)
"""
def selection_sort(lst):
    """This function implements the selection sort algorithm to sort a list in-place."""
    n = len(lst)
    for i in range(n):
        sort_position = i
        for j in range(i + 1, n):
            if lst[j] < lst[sort_position]:
                sort_position = j
        lst[i], lst[sort_position] = lst[sort_position], lst[i]
    
    return lst # return is not necessary, but it allows to use the function in a functional style, e.g. sorted_lst = selection_sort(lst)