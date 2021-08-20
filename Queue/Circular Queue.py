# a circular queue built with a list of Nones, it has a certain size which doesn't change if an element is removed.
class CircularQueue:
    def __init__(self, capacity: int):
        self.queue = [None]*capacity
        self.capacity = capacity
        self.size = 0
        self.head = 0
        self.tail = 0

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.size == self.capacity:
            return True
        else:
            return False

    def getHead(self) -> int:
        return self.queue[self.head]

    def getTail(self) -> int:
        return self.queue[self.tail]

    def enQueue(self, val: int) -> bool:
        if self.size < self.capacity:
            self.queue[self.tail] = val
            self.size += 1
        if self.tail < self.capacity:
            self.tail = self.tail+1
        if self.tail == self.capacity and self.size < self.capacity:
            self.tail = 0
        return True

    def deQueue(self) -> bool:
        self.queue[self.head] = None
        if self.head < self.capacity:
            self.head = self.head+1
        if self.head == self.capacity and self.capacity > self.size:
            self.head = 0
        self.size -= 1
        return True

myCircularQueue = CircularQueue(3)
myCircularQueue.enQueue(1)
myCircularQueue.enQueue(5)
myCircularQueue.deQueue()
myCircularQueue.enQueue(2)
myCircularQueue.enQueue(3)
myCircularQueue.deQueue()
print(myCircularQueue.queue, myCircularQueue.size, myCircularQueue.isFull(), myCircularQueue.getHead())
