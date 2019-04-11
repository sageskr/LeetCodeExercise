#!/bin/env python
# coding: utf8
# author: Kairong
# create time: 2019-04-11
# 9. Palindrome Number
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        letter_x = str(x)
        len_x = len(letter_x)
        result = 0
        for _num in xrange(len_x):
            result += int(letter_x[_num]) * (10 ** _num)
        if result == x:
            return True
        else:
            return False