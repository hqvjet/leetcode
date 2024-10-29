# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # reverse linked list from end to start
    def reverse_linked_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current is not None:
            next_node = current.next  
            current.next = prev  
            prev = current  
            current = next_node  

        return prev 
    
    # idea: handle all of these trees nodes and use a variable to save residual value, create new tree to save answer
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        memory = 0
        res = ListNode()

        # handle all nodes of trees
        while l1 != None or l2 != None:
            # if thera is no node, value = 0
            val1 = l1.val if l1 != None else 0
            val2 = l2.val if l2 != None else 0

            # sum of two nodes in the same linked list level
            temp = val1 + val2 + memory

            # add the last digit of temp
            res.val = temp % 10
            # get the residual value
            memory = temp // 10

            # check for if the tree still have unhandle node
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next

            # mock the new node at begin of result tree and set result tree = mocked tree
            new_node = ListNode(next=res)
            res = new_node

        # check for if there is still have residual value
        if memory != 0:
            res.val = 1        
        if res.val == 0:
            res = res.next

        # return reverse tree
        return self.reverse_linked_list(res)
