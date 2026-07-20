"""
Name: insertion_sort.py
Author: Kevin Warschkow
Created: 16.07.2026
License: MIT
Task: Implement the insertion sort algorithm to sort a list in-place.
Input: Field of numbers (list)
Output: Sorted field of numbers (list)
"""
def insertion_sort(lst):
    """This function implements the insertion sort algorithm to sort a list """
    n = len(lst)
    for i in range(1, n):
        key = lst[i]
        j = i - 1
        while (j>=0 and lst[j] > key):
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    return lst