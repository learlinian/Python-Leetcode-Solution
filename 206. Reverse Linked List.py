class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


"""iterative methods"""
# class Solution(object):
#     def reverseList(self, head):
#         if head is None or head.next is None:
#             return head
#         first_ptr = None
#         second_ptr = head
#         while second_ptr is not None:
#             temp_ptr = second_ptr.next
#             second_ptr.next = first_ptr
#             first_ptr = second_ptr
#             second_ptr = temp_ptr
#         return first_ptr


"""recursive method"""
class Solution(object):
    def reverseList(self, head):
        p = head
        if head is not None and head.next is not None:
            p = self.reverseList(head.next)
            head.next.next = head
            head.next = None
        return p


a = ListNode(1)
b = ListNode(2)
a.next = b
result = Solution().reverseList(a)
while result:
    print(result.val)
    result = result.next
