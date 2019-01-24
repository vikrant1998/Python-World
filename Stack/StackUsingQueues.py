class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.q.insert(0, x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if len(self.q) <= 0: return None
        itrSize = len(self.q) - 1
        i = 0
        while i < itrSize:
            self.q.insert(0, self.q.pop())
            i += 1

        val = self.q.pop()
        return val

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if len(self.q) <= 0: return None
        itrSize = len(self.q) - 1
        i = 0
        while i < itrSize:
            self.q.insert(0, self.q.pop())
            i += 1

        val = self.q[-1]       

        self.q.insert(0, self.q.pop())
        return val
        
    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if len(self.q) == 0: return True
        return False


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.top())
print(obj.pop())
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()