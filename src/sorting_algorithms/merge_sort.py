"""
Name: merge_sort.py
Author: Kevin Warschkow
Created: 31.05.2026
License: MIT
Task: Implement the merge sort algorithm to sort a list and return a new sorted list.
"""

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