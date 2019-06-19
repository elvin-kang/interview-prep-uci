class PriorityQueue:
    def __init__(self, arr=list()):
        self._heap = arr
        n = len(self._heap)
        for i in range(n, -1, -1):
            self.heapify(self._heap, n, i)

    def heapify(self, arr: list, n: int, i: int=0):
        """Heapifies given array arr, length n, and index i."""
        smallest = i
        l = 2 * i + 1
        r = 2 * i + 2

        # if left child exists and is smaller than root
        if l < n and arr[l] < arr[i]:
            smallest = l
        # if right child exists and is smaller than root & left child
        if r < n and arr[r] < arr[smallest]:
            smallest = r
        # if root is not smallest
        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            self.heapify(arr, n, smallest) # heapify

    def add(self, e: "element"):
        """Inserts e into this priority queue"""
        self._heap.append(e)
        self._bubble_up()

    def clear(self):
        """Removes all elements from this priority queue"""
        self._heap = []

    def contains(self, o: "object"):
        """Retruns true if this queue contains o"""
        return o in self._heap

    def peek(self):
        """Retrieves, but doesn't remove the head of this queue"""
        if not self._heap:
            return None
        return self._heap[0]

    def poll(self):
        """Retrieves and removes the head of queue.
           return None if queue is empty"""
        if not self._heap:
            return None
        if len(self._heap) == 1:
            return self._heap.pop()
        head = self._heap[0]
        self._heap[0] = self._heap.pop()
        self._bubble_down()
        return head

    def size(self):
        """returns the number of elements in this collection"""
        return len(self._heap)

    def isEmpty(self):
        return len(self._heap) == 0

    def __len__(self):
        return len(self._heap)

    def __str__(self):
        return str(self._heap)

    def toArray(self):
        return self._heap

    def _bubble_up(self):
        i = len(self._heap) - 1
        while i > 0 and self._heap[i//2] > self._heap[i]:
            self._heap[i], self._heap[i//2] = self._heap[i//2], self._heap[i]
            i //= 2

    def _bubble_down(self):
        n = len(self._heap)
        i = 0
        leftChildIndex = 2 * i + 1
        rightChildIndex = 2 * i + 2
        while leftChildIndex < n:
            if rightChildIndex < n:
                j = leftChildIndex if self._heap[leftChildIndex] < self._heap[rightChildIndex] else rightChildIndex
                if self._heap[i] > self._heap[j]:
                    self._heap[i], self._heap[j] = self._heap[j], self._heap[i]
                    i = j
                else:
                    break
            else:
                if self._heap[leftChildIndex] < self._heap[i]:
                    self._heap[leftChildIndex], self._heap[i] = self._heap[i], self._heap[leftChildIndex]
                    i = leftChildIndex
                else:
                    break

            leftChildIndex = 2 * i + 1
            rightChildIndex = 2 * i + 2


if __name__ == '__main__':
    pq = PriorityQueue()
    pq.add(5)
    pq.add(3)
    pq.add(4)
    pq.add(1)
    print(pq.peek())
    print(pq)
    print(pq.poll())
    print(pq)
    print(pq.poll())
    print(pq)

    print("###############")
    pq2 = PriorityQueue([24, 31, 77])
    pq2.poll()
    print(pq2)