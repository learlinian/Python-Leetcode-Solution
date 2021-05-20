class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def getOneNumber(self, l, val):
        if val == 0:
            return l
        start = l
        while l is not None:
            total_val = l.val + val
            l.val = total_val % 10
            val = total_val // 10
            if l.next is None and val == 1:
                l.next = ListNode(1)
                break
            l = l.next
        return start

    def addTwoNumbers(self, l1, l2):
        if l1 is None:
            return l2
        next_digit = 0
        start, prev = l1, l1
        while l1 is not None:
            if l2 is None:
                prev.next = self.getOneNumber(l1, next_digit)
                return start
            prev = l1
            total_val = l1.val + l2.val + next_digit
            next_digit = total_val // 10
            l1.val = total_val % 10
            l1, l2 = l1.next, l2.next
        if l2 is not None:
            prev.next = self.getOneNumber(l2, next_digit)
            return start
        if next_digit > 0:
            prev.next = ListNode(1)
        return start


if __name__ == '__main__':
    node = ListNode(1)
