import unittest
from utils.Stack import Stack

class StackTest(unittest.TestCase):
    def test_emptyWhenConstructed(self):
        s = Stack()
        self.assertEqual(len(s), 0)

    def test_push(self):
        s = Stack()
        s.push(3)
        self.assertEqual(s.toList(), [3])

if __name__ == '__main__':
    t = unittest.TestLoader().loadTestsFromTestCase(StackTest)
    unittest.TextTestRunner(verbosity=2).run(t)