# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        t1 = l1
        t2 = l2
        
        ret = ListNode(0)
        f = ret
        
        while t1 != None and t2 != None:
            if t1.val <= t2.val:
                f.next = ListNode(t1.val)
                
                t1 = t1.next
            else:
                f.next = ListNode(t2.val)
                t2 = t2.next
                
            f = f.next
        
        if t1 == None:
            f.next = t2
        else:
            f.next = t1
            
        return ret.next
                
        
