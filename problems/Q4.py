#!/bin/env python
# coding: utf8
# author: Kairong
# create time: 2019-04-11
# 4. Median of Two Sorted Arrays

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_list = nums1 + nums2
        l_total_list = len(total_list)
        if len(total_list) % 2 == 0:
            return (total_list[l_total_list / 2] + total_list[l_total_list / 2 - 1]) /2.0
        else:
            return total_list[l_total_list/2]

