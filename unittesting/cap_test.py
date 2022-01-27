import unittest
import cap


class TestCap(unittest.TestCase):
    def test_one_word(self):
        text = "python"
        result = cap.cap_text(text)
        self.assertEqual(result, "Python")  # add assertion here

    def test_multi_word(self):
        text = "monty python"
        result = cap.cap_text(text)
        self.assertEqual(result, "Monty Python")  # add assertion here


if __name__ == '__main__':
    unittest.main()
