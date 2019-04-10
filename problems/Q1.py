#!/bin/env python
# coding: utf8
# author: Kairong
# create time: 2019-04-10
# question 	#1 Two Sum


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l_nums = len(nums)
        if l_nums < 2:
            pass
        else:
            for _index in xrange(l_nums):
                temp_list = nums[:]
                temp_list.pop(_index)
                gap = target - nums[_index]
                if gap in temp_list:
                    return [_index, temp_list.index(gap)+1]
