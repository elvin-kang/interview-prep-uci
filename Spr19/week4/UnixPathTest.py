import unittest
from unixpath import Solution

class PathTest(unittest.TestCase):
    def test1(self):
        s = Solution()
        self.assertEqual(s.unixpath("/usr/bin/../"), "/usr/")
    
    def test2(self):
        s = Solution()
        self.assertEqual(s.unixpath("/usr/./bin/./test/../"), "/usr/bin/")

    def test3(self):
        s = Solution()
        self.assertEqual(s.unixpath("/usr/bin/../src/./test/main/.././"), "/usr/src/test/")

if __name__ == '__main__':
    t = unittest.TestLoader().loadTestsFromTestCase(PathTest)
    unittest.TextTestRunner(verbosity=2).run(t)