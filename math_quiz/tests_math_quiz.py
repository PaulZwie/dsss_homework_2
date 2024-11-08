import unittest

from math_quiz import get_random_int, get_random_operator, calculate_operation


class TestMathGame(unittest.TestCase):

    def test_get_random_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _8 in range(1000):  # Test a large number of random values
            rand_num = get_random_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_get_random_operator(self):
        operators = ['+', '-', '*']
        for _ in range(100):
            result = get_random_operator()
            self.assertIn(result, operators)

    def test_calculate_operation(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (-1, -1, '+', '-1 + -1', -2),
            (1.5, 2.5, '+', '1.5 + 2.5', 4.0),
            (5, 2, '-', '5 - 2', 3),
            (0, 0, '-', '0 - 0', 0),
            (-1, -1, '-', '-1 - -1', 0),
            (1.5, 2.5, '-', '1.5 - 2.5', -1.0),
            (5, 2, '*', '5 * 2', 10),
            (0, 0, '*', '0 * 0', 0),
            (-1, -1, '*', '-1 * -1', 1),
            (1.5, 2.5, '*', '1.5 * 2.5', 3.75)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            self.assertEqual(calculate_operation(number_1=num1, number_2=num2, operator=operator),
                             (expected_problem, expected_answer))


if __name__ == "__main__":
    unittest.main()
