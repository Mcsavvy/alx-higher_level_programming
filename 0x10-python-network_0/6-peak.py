#!/usr/bin/python3
"""
This file contains a function that gets the peak number in a list
"""


def find_peak(nums):
    """
    find the peak number in an array
    """
    if nums == []:
        return
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums)
    if nums[0] > nums[1]:
        return nums[0]
    if nums[-1] > nums[-2]:
        return nums[-1]
    # get the mid element
    if len(nums) % 2:
        mid = len(nums) // 2
    else:
        mid = (len(nums) + 1) // 2
    left = nums[:mid + 1]
    right = nums[mid:]
    if nums[mid] >= left[-2] and nums[mid] >= right[1]:
        return nums[mid]
    if mid < left[-2]:
        pl = find_peak(left)
        if pl is not None:
            return pl
        pr = find_peak(right)
        if pl is not None:
            return pl
    else:
        pr = find_peak(right)
        if pr is not None:
            return pr
        pl = find_peak(left)
        if pl is not None:
            return pl
