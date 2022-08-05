'''
# @Time : 2022/7/29 10:33
# @Author : Admin
# @Project : PythonCode
'''


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []
        self.front = None

    def push(self, x: int) -> None: # 入队
        """
        Push element x to the back of queue.
        """
        if not self.s1: self.front = x
        self.s1.append(x)

    def pop(self) -> int: # 出队
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
            self.front = None
        return self.s2.pop()

    def peek(self) -> int:  # 获取队头元素
        """
        Get the front element.
        """
        if self.s2:
            return self.s2[-1]
        return self.front

    def empty(self) -> bool:    # 判空
        """
        Returns whether the queue is empty.
        """
        if not self.s1 and not self.s2:
            return True
        return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
