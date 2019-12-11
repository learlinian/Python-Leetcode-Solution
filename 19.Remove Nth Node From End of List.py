class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        pointer = head
        num = 0
        while pointer is not None:
            num += 1
            pointer = pointer.next
        # print(num)
        if num == 1:
            return None

        pointer = head
        count = 0
        if num - n - 1 < 0:
            head = head.next
        else:
            while count < num - n - 1:
                pointer = pointer.next
                count += 1

            if pointer.next.next is None:
                pointer.next = None
            else:
                pointer.next = pointer.next.next

        return head


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5

    head = Solution().removeNthFromEnd(l1, 4)
    while head is not None:
        print(head.val)
        head = head.next
