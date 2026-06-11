# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1
        if not list1:
            return list2
        if not list2:
            return list1
        dummy = ListNode()
        tail = dummy
        # if list1.val <= list2.val:
        #     print("IF 1")
        #     head=list1
        #     list1 = list1.next
        # else:
        #     print("IF 2")

        #     head = list2
        #     list2 = list2.next
        while list1 and list2:
            if list1.val <= list2.val: 
                print("IF 3")

                tail.next = list1
                list1 = list1.next
                tail = tail.next
            else:
                print("IF 4")
    
                tail.next = list2
                list2 = list2.next
                tail = tail.next
        
        if list1:
            tail.next = list1
            tail = tail.next
        if list2:
            tail.next = list2
            tail = tail.next
        return dummy.next
