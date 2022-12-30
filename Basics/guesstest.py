import unittest
import guessgame as gg


class TestGame(unittest.TestCase):
    def test_input(self):
        result = gg.fcnGuess(5, 5)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = gg.fcnGuess(1, 5)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = gg.fcnGuess(11, 5)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        result = gg.fcnGuess("11", 5)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
