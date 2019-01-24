class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if len(self.minStack) > 0 and x < self.minStack[-1]:
            self.minStack.append(x)
        elif len(self.minStack) > 0:
            self.minStack.append(self.minStack[-1])
        else:
            self.minStack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack) > 0:
            self.stack.pop()
            self.minStack.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
            return self.stack[-1]

        return None

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.minStack) > 0: return self.minStack[-1]
        return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()