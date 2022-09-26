# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        else:
            temp = head
            visited_nodes =[head.val]
            while temp.next is not None:
                if temp.next.val in visited_nodes:
                    temp.next = temp.next.next
                else:
                    visited_nodes.append(temp.next.val)
                    temp = temp.next
            return head