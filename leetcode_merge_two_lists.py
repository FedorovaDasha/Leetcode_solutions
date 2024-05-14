class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_linked_list(nodelist):
    while nodelist:
        print(nodelist.val, end=" -> ")
        nodelist = nodelist.next
    print("None")


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        result_list = ListNode()
        curr = result_list
        while (list1 and list2):
            if list1.val < list2.val:
                curr.next = ListNode(list1.val)
                list1 = list1.next
            else:
                curr.next = ListNode(list2.val)
                list2 = list2.next
            curr = curr.next
        curr.next = list1 or list2
        return result_list.next


n3 = ListNode(4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)
print_linked_list(n1)

m3 = ListNode(4)
m2 = ListNode(3, m3)
m1 = ListNode(1, m2)
print_linked_list(m1)

sol = Solution()
print_linked_list(sol.mergeTwoLists(n1, m1))
