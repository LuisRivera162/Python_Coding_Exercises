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
        self.head = ListNode(0, None, None)
        self.min_head = ListNode(0, None, None)

    def push(self, x: int) -> None:
        if self.size == 0 or x <= self.min_head.val:
            self.min_head.next = ListNode(x, None, self.min_head)
            self.min_head = self.min_head.next

        self.head.next = ListNode(x, None, self.head)
        self.head = self.head.next
        self.size += 1

    def pop(self) -> None:
        if self.size == 0:
            return

        if self.head.val == self.min_head.val:
            self.min_head = self.min_head.prev
            self.min_head.next = None

        self.head = self.head.prev
        self.head.next = None
        self.size -= 1

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.min_head.val

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
