from collections import deque
from queue import Queue
"""Requests proceed in the order in which they arrive.
If Queue module, big O complexity: O(1); if list, big O = O(list elements)"""


# implementation using build-in list structure
def list_queue(queue, to_add):
    queue = queue
    # dequeue
    queue.pop(0)
    # enqueue
    queue.append(to_add)
    return queue


def collection_queue(queue, to_add):
    queue = deque(queue)
    queue.popleft()
    queue.append(to_add)
    return queue


def queue_queue(list_queue, to_add):
    max_size = 10
    queue = Queue(maxsize=max_size)
    for i in list_queue:
        if queue.qsize()+1 <= max_size:
            queue.put(i)
    queue.get()
    queue.put(to_add)
    queue.task_done()
    return queue.qsize()


if __name__ == '__main__':
    print(list_queue(queue=[1, 2, 3, 4, 5, 6], to_add=7),
          collection_queue(queue=[1, 2, 3, 4, 5, 6], to_add=7),
          queue_queue(list_queue=[1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12], to_add=7)
          )
