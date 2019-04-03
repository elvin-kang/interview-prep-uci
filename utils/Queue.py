from collections import deque

class Queue:
    def __init__(self):
        self._queue = deque()

    def add(self, val):
        self._queue.appendleft(val)

    def peek(self):
        """Retrieves, but doesn't remove head of the queue"""
        x = self._queue.pop()
        self._queue.append(x)
        return x

    def poll(self):
        """Retrieves and removes the head of the queue, returns None if queue is empty"""
        if not self._queue:
            return None
        return self._queue.pop()

    def remove(self):
        """Retrieves and removes the head of the queue"""
        return self._queue.pop()

    def isEmpty(self):
        return len(self._queue) == 0

    def __len__(self):
        return len(self._queue)