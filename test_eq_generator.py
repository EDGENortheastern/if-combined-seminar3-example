import unittest  # provides the unit testing framework
from equation_generator import generate_equation  # function under test

class TestGenerateEquation(unittest.TestCase):

    def test_return_types(self):
        equation, solution = generate_equation()

        self.assertIsInstance(equation, str)
        self.assertIsInstance(solution, int)

    def test_equation_is_correct(self):
        equation, solution = generate_equation()

        coefficient = int(equation.split("x")[0])
        right_hand_side = int(equation.split("=")[1].strip())

        self.assertEqual(coefficient * solution, right_hand_side)
        self.assertGreater(coefficient, 0)


if __name__ == "__main__":
    unittest.main()