# https://leetcode.com/problems/min-stack/


class ListNode:
    def __init__(self, x, next, prev):
        self.val = x
        self.next = next
        self.prev = prev


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.size = 0
        self.dummy_head = ListNode(0, None, None)
        self.dummy_min = ListNode(0, None, None)

    def push(self, x: int) -> None:
        if self.size == 0 or x <= self.dummy_min.val:
            self.dummy_min.next = ListNode(x, None, self.dummy_min)
            self.dummy_min = self.dummy_min.next

        self.dummy_head.next = ListNode(x, None, self.dummy_head)
        self.dummy_head = self.dummy_head.next
        self.size += 1

    def pop(self) -> None:
        if self.size == 0:
            return

        if self.dummy_head.val == self.dummy_min.val:
            self.dummy_min = self.dummy_min.prev
            self.dummy_min.next = None

        self.dummy_head = self.dummy_head.prev
        self.dummy_head.next = None
        self.size -= 1

    def top(self) -> int:
        return self.dummy_head.val

    def getMin(self) -> int:
        return self.dummy_min.val

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
