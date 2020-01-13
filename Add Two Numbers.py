#https://leetcode.com/problems/add-two-numbers/
'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

'''

# Answer:

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        flag = 0
        tmp = []
        p1 = l1
        p2 = l2
        while p1 != None and p2 != None:
            val = (p1.val + p2.val + flag) % 10
            flag = (p1.val + p2.val + flag - val) / 10
            t = ListNode(val)
            tmp.append(t)
            p1 = p1.next
            p2 = p2.next
            
        if p1 != None:
            while p1 != None:
                val = (p1.val + flag) % 10
                flag = (p1.val + flag - val) / 10
                t = ListNode(val)
                tmp.append(t)
                p1 = p1.next
        if p2 != None:
            while p2 != None:
                val = (p2.val + flag) % 10
                flag = (p2.val + flag - val) / 10
                t = ListNode(val)
                tmp.append(t)
                p2 = p2.next   
                
        for i, node in enumerate(tmp):
            if i < len(tmp) - 1:
                node.next = tmp[i+1]
            else:
                if flag == 1:
                    node.next = ListNode(1)
            
            
        return tmp[0]
