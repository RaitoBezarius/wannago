from src.parser import Stream
import unittest

class TestStream(unittest.TestCase):

    def test_stream_list(self):
        stream = Stream("Hello")
        self.assertEqual(list(stream), ['H', 'e', 'l', 'l', 'o'])
