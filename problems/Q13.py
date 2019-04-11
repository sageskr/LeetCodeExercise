#!/bin/env python
# coding: utf8
# author: Kairong
# create time: 2019-04-11
# 13. Roman to Integer
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            'I': 1,
            'V': 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        temp_result = []
        result_num = 0
        for _letter in s:
            temp_result.append(roman[_letter.upper()])
        temp_result.reverse()
        x = temp_result.pop()
        while True:
            if len(temp_result) <= 0:
                result_num += x
                break
            else:
                y = temp_result.pop()
            if x >= y:
                z = x
                x = y
                result_num += z
            elif x < y:
                result_num += y - x
                if len(temp_result) <=0:
                    break
                else:
                    x = temp_result.pop()
        return result_num

ll = Solution()
print ll.romanToInt("IV")


class Solution:
    def romanToInt(self, s):
        res = 0
        hashmap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        i = 0
        s += 'I'
        while i < len(s) - 1:
            if hashmap[s[i]] < hashmap[s[i + 1]]:
                res += hashmap[s[i + 1]] - hashmap[s[i]]
                i += 2
            else:
                res += hashmap[s[i]]
                i += 1
        return res