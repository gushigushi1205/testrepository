import unittest
import sample


class TestSample(unittest.TestCase):
    def test_fizzbuzz(self):
        result = sample.fizzbuzz(3)
        self.assertEqual(result,'fizzbuzz')
