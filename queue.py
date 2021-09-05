class MyQueue:

    def __init__(self):
        self.array = []
        self.head = 0
        self.i = 0

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.array.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.array) > 0:
            a = self.array[0]
            self.array.pop(0)

            return a

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.array[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """

        return self.array == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
