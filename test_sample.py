import unittest
import sample


class TestSample(unittest.TestCase):
    def test_fizzbuzz(self):
        result = sample.fizzbuzz(15)
        self.assertEqual(result,'fizzbuzz')

    def test_fizzbuzz2(self):
        result = samplefizzbuzz(5)
        self.assertEqual(result,'cas')

    def test_fizzbuzz3(self):
        result = samplefizzbuzz(4)
        self.assertEqual(result,'cas')
