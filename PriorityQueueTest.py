import unittest
from utils.PriorityQueue import PriorityQueue

class PriorityQueueTest(unittest.TestCase):
    def test_emptyWhenConstructed(self):
        pq = PriorityQueue()
        self.assertEqual(len(pq), 0)

    def test_len(self):
        pq = PriorityQueue()
        pq.add(1)
        pq.add(2)
        pq.add(3)
        print(pq)
        self.assertEqual(len(pq), 3)
        
        pq.clear()

    def test_add(self):
        pq = PriorityQueue()
        pq.add(3)
        pq.add(1)
        pq.add(5)
        self.assertEqual(pq._heap, [1, 3, 5])
        pq.clear()
        self.assertEqual(len(pq), 0)

    def test_peek(self):
        pq = PriorityQueue()
        pq.add(1)
        pq.add(2)
        self.assertEqual(pq.peek(), 1)
        self.assertEqual(pq.poll(), 1)
        self.assertEqual(pq.poll(), 2)
        self.assertEqual(len(pq), 0)
        pq.clear()
        with self.assertRaises(IndexError):
            pq.remove()

if __name__ == '__main__':
    t = unittest.TestLoader().loadTestsFromTestCase(PriorityQueueTest)
    unittest.TextTestRunner(verbosity=2).run(t)