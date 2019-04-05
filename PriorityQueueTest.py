import unittest
from utils.PriorityQueue import PriorityQueue

class PriorityQueueTest(unittest.TestCase):
    def test_emptyWhenConstructed(self):
        pq = PriorityQueue()
        self.assertEqual(len(pq), 0)

    def test_len(self):
        q = Queue()
        q.add(1)
        q.add(2)
        q.add(3)
        self.assertEqual(len(q), 3)
        self.assertFalse(q.isEmpty())

    def test_add(self):
        q = Queue()
        q.add(3)
        q.add(5)
        self.assertEqual(q.poll(), 3)
        self.assertEqual(q.poll(), 5)

    def test_peek(self):
        q = Queue()
        q.add(1)
        q.add(2)
        self.assertEqual(q.peek(), 1)
        self.assertEqual(q.poll(), 1)
        self.assertEqual(q.poll(), 2)
        self.assertEqual(len(q), 0)
        with self.assertRaises(IndexError):
            q.remove()

if __name__ == '__main__':
    t = unittest.TestLoader().loadTestsFromTestCase(PriorityQueueTest)
    unittest.TextTestRunner(verbosity=2).run(t)