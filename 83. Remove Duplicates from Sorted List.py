# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        a = head
        b = head
        while b is not None:
            if b.val != a.val:
                a = b
            else:
                a.next = b.next

            b = b.next

        return head


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(1)
    c = ListNode(2)

    a.next = b
    b.next = c
    new_list = Solution().deleteDuplicates(a)
    while new_list is not None:
        print(new_list.val)
        new_list = new_list.next