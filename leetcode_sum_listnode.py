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
    def addTwoNumbers(self, l1, l2):
        tens = 0
        result_list = ListNode()
        curr = result_list
        while l1 or l2 or tens:
            res = tens
            if l1:
                res += l1.val
                l1 = l1.next
            if l2:
                res += l2.val
                l2 = l2.next
            tens = res//10
            curr.next = ListNode(res % 10)
            curr = curr.next
        return print_linked_list(result_list.next)


n3 = ListNode(4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)
print_linked_list(n1)

m3 = ListNode(4)
m2 = ListNode(3, m3)
m1 = ListNode(1, m2)
print_linked_list(m1)

sol = Solution()
sol.addTwoNumbers(n1, m1)
