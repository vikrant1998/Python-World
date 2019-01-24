class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.s1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.s2) != 0:
            return self.s2.pop()

        while len(self.s1) > 0:
            self.s2.append(self.s1.pop())

        if len(self.s2) != 0:
            return self.s2.pop()
        else:
            return None

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.s2) != 0:
            return self.s2[-1]
        
        while len(self.s1) > 0:
            self.s2.append(self.s1.pop())

        if len(self.s2) > 0:
            return self.s2[-1]

        return None

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.s1) == 0 and len(self.s2) == 0: return True
        return False