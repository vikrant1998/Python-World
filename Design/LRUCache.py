class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = dict()
        self.head = None
        self.tail = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1

        oldVal = self.cache[key].value
        self._DeleteListNode(self.cache[key])
        del(self.cache[key])
        self._InsertIntoDoublyLinkedList(key, oldVal)
        self.cache[key] = self.tail
        return oldVal

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """

        # If it's already in the cache, update it and move it to the end.
        if key in self.cache:
            self._DeleteListNode(self.cache[key])
            del(self.cache[key])
            self._InsertIntoDoublyLinkedList(key, value)
            self.cache[key] = self.tail
            return

        # If it's not in the cache and there's space in cache.
        if len(self.cache) < self.capacity:
            #print(key, value, len(self.cache))
            #print(self.cache)
            self._InsertIntoDoublyLinkedList(key, value)
            self.cache[key] = self.tail
            return

        # If it's not in the cache not there's no space in cache.
        keyToDel = self.head.key
        self._DeleteListNode(self.head)
        del(self.cache[keyToDel])
        self._InsertIntoDoublyLinkedList(key, value)
        self.cache[key] = self.tail

    def _InsertIntoDoublyLinkedList(self, key, value):
        # Empty.
        if self.head == None and self.tail == None:
            self.tail = ListNode(key, value)
            self.head = self.tail
        # Non empty.
        else:
            newNode = ListNode(key, value)
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode

    def _DeleteListNode(self, node):
        if node == None:
            return
        
        if node == self.head and node == self.tail:
            del(node)
            self.head = None
            self.tail = None
            return

        if node == self.head:
            nextNode = node.next
            nextNode.prev = None
            del(node)
            self.head = nextNode
            return

        if node == self.tail:
            prevNode = node.prev
            prevNode.next = None
            del(node)
            self.tail = prevNode
            return

        # Neither head nor tail.
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        del(node)
        return

if __name__ == "__main__":
    # Your LRUCache object will be instantiated and called as such:
    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))

    #print(cache.head.value)
    #print(cache.tail.value)

    cache.put(3, 3)
    print(cache.get(2))
    '''
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))
    '''
    '''
    nodePtr = obj.head
    while nodePtr != None:
        print(nodePtr.key)
        nodePtr = nodePtr.next

    print('\n')

    nodePtr = obj.tail
    while nodePtr != None:
        print(nodePtr.key)
        nodePtr = nodePtr.prev
    '''