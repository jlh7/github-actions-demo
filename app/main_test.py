from main import return_backwards_string, get_mode
import unittest
import os


class TestMain(unittest.TestCase):
    def test_return_backwards_string(self):
        self.assertEqual(return_backwards_string("hello"), "olleh")
        self.assertEqual(return_backwards_string("hello world"), "dlrow olleh")
        self.assertEqual(return_backwards_string("12345"), "54321")

    def test_get_mode(self):
        os.environ["MODE"] = "test"
        self.assertEqual(get_mode(), "test")
        os.environ["MODE"] = "prod"
        self.assertEqual(get_mode(), "prod")
        os.environ["MODE"] = "dev"
        self.assertEqual(get_mode(), "dev")


if __name__ == '__main__':
    unittest.main()
