#!/bin/env python
# coding: utf8
# author: Kairong
# create time: 2019-04-11
# 7. Reverse Integer
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        temp_result = []
        for _x in str(x):
            temp_result.append(_x)
        if temp_result[0] == "-":
            temp_result = temp_result[1:]
            temp_result.reverse()
            temp_result.insert(0,"-")
        else:
            temp_result.reverse()
        rtn = int(''.join(temp_result))
        if rtn < -2 ** 31 or rtn > 2** 31 -1:
            return 0
        else:
            return rtn