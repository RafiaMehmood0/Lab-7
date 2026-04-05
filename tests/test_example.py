import unittest

class TestApp(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 3, 6)   # ❌ intentionally wrong

if __name__ == "__main__":
    unittest.main()
