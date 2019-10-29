class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head

        # move head until it is not the duplicate one
        while head is not None and (head.next is not None and head.val == head.next.val):
            head_val = head.val
            while head is not None and head.val == head_val:
                head = head.next

        if head is None or head.next is None:
            return head

        # define 2 pointers: a and b
        a = head
        b = head.next
        while b is not None:
            # print(b.val)
            if b.next is not None:
                if b.val != b.next.val:
                    a = b
                else:
                    # if next node's value has the same value as this node or next node is still part of duplicate node, move forword
                    while b.next is not None and (b.val == b.next.val or (b.next.next is not None and b.next.val == b.next.next.val)):
                        b = b.next

                    a.next = b.next

                b = b.next
            else:
                break
        return head


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(1)
    c = ListNode(3)
    d = ListNode(3)
    e = ListNode(4)
    f = ListNode(4)
    g = ListNode(5)

    all = [a, b, c, d]
    for i in range(3):
        all[i].next = all[i+1]

    new_list = Solution().deleteDuplicates(a)
    while new_list is not None:
        print(new_list.val)
        new_list = new_list.next