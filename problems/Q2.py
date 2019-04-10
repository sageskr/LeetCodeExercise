#!/bin/env python
# coding: utf8
# author: Kairong
# create time: 2019-04-10
# #2 Add Two Numbers
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list_l1 = []
        num_l1 = 0
        list_l2 = []
        num_l2 = 0
        while l1:
            tmp_val = l1.val
            list_l1.append(tmp_val)
            l1 = l1.next
        while l2:
            tmp_val = l2.val
            list_l2.append(tmp_val)
            l2 = l2.next
        for _num in xrange(len(list_l1)):
            num_l1 += int(list_l1[_num]) * (10**_num)
        for _num in xrange(len(list_l2)):
            num_l2 += int(list_l2[_num]) * (10 ** _num)
        _tmp_result = num_l1 + num_l2
        _tmp_result2 = str(_tmp_result)[-1::-1]
        head = ListNode(_tmp_result2[0])
        current = head
        for i in _tmp_result2[1:]:
            current.next = ListNode(i)
            current = current.next

        return head
