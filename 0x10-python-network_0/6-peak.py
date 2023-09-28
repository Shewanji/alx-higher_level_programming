#!/usr/bin/python3
"""
This function finds a peak in a list of unsorted integers.

It uses a binary search-like approach to efficiently locate a peak element.
"""


def find_peak(list_of_integers):
    """
    Find a peak element in the given list.

    """
    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return list_of_integers[left]
