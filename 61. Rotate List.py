class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


"""not efficient solution"""
# class Solution(object):
#     def rotateRight(self, head, k):
#         if head is None or head.next is None:
#             return head
#         last = head.next
#         last_second = head
#         count = 2
#         while last.next is not None:
#             last_second = last
#             last = last.next
#             count += 1
#
#         for _ in range(k % count):
#             while last.next is not None:
#                 last_second = last
#                 last = last.next
#             last.next = head
#             last_second.next = None
#             head = last
#         return head


class Solution(object):
    def rotateRight(self, head, k):
        if head is None or head.next is None:
            return head
        last = head.next
        start = head
        count = 2
        while last.next is not None:
            last = last.next
            count += 1

        k %= count
        if k == 0:
            return head
        for _ in range(count-k-1):
            start = start.next
        temp = start.next
        start.next = None
        last.next = head
        return temp
