class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# class Solution(object):
#     def hasCycle(self, head):
#         visited_node = []
#         while head:
#             if head in visited_node:
#                 return True
#             visited_node.append(head)
#             head = head.next
#         print(visited_node)
#         return False


class Solution(object):
    def hasCycle(self, head):
        first_ptr = second_ptr = head
        while second_ptr is not None:
            first_ptr = first_ptr.next
            if second_ptr.next is None:
                return False
            second_ptr = second_ptr.next.next
            if first_ptr == second_ptr:
                return True
        return False


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c

print(Solution().hasCycle(a))