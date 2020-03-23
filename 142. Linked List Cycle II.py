class Solution(object):
    def detectCycle(self, head):
        first_ptr = second_ptr = head
        while second_ptr is not None:
            first_ptr = first_ptr.next
            if second_ptr.next is None:
                return None
            second_ptr = second_ptr.next.next
            if first_ptr == second_ptr:
                while head != first_ptr:
                    head = head.next
                    first_ptr = first_ptr.next
                return head
        return None