"""Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
Example:
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""


# Solution 1
class Solution1(object):
    def mergeKLists1(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        v_map = {}
        for element in lists:
            while element is not None:
                # Append node to dictionary if its key already exists. Otherwise create a key
                try:
                    v_map[element.val].append(element)
                except KeyError:
                    v_map[element.val] = [element]
                element = element.next

        # sort the dictionary according to its key
        sorted_keys = sorted(v_map.keys())
        first_key = sorted_keys[0]
        head = end = v_map[first_key][0]

        # link nodes one by one
        for key in sorted_keys:
            for t in v_map[key]:
                # print(t.val)
                end.next = t
                end = t
        end.next = None

        return head     # return its head


# Solution 2
class Solution2(object):
    def mergeKLists2(self, lists):
        x = []
        while lists:
            minVal = min([lists[i].val for i in range(len(lists))])     # get the min value for each 3 nodes
            index = 0       # determine which item in 3 nodes has min value
            for l in lists:
                if l.val == minVal:
                    x.append(l)
                    if l.next is None:      # remove the this item from list if it has no following nodes
                        lists.remove(l)
                    else:
                        lists[index] = l.next      # pass the value instead
                    break
                index += 1

        x_length = len(x) - 1
        for i in range(x_length):
            x[i].next = x[i + 1]
        x[x_length].next = None

        return x[0]


class linked_list:
    def __init__(self, x):
        self.val = x
        self.next = None

    def next_list(self, next_list):
        self.next = next_list


x1 = linked_list(1)
x2 = linked_list(4)
x3 = linked_list(5)

x4 = linked_list(1)
x5 = linked_list(3)
x6 = linked_list(4)

x7 = linked_list(2)
x8 = linked_list(6)

x1.next_list(x2)
x2.next_list(x3)

x4.next_list(x5)
x5.next_list(x6)

x7.next_list(x8)

val = [x1, x4, x7]
y = Solution2()

result = y.mergeKLists2(val)

while result is not None:
    print(result.val)
    result = result.next
