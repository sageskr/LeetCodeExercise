#!/bin/env python
# coding: utf8
# author: Kairong
# create time: 2019-04-10
# 3. Longest Substring Without Repeating Characters
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max=0
        lens = len(s)
        for _j in xrange(lens):
            tmp_result = []
            tmp_result.append(s[_j])
            for _k in xrange(_j+1,lens):
                if s[_k] in tmp_result:
                    break
                else:
                    tmp_result.append(s[_k])
            if max < len(tmp_result):
                max = len(tmp_result)
        return max