import unittest

from generator_order_box import GeneratorOrderBox, OrderSizeException


class MyTestCase(unittest.TestCase):
    correct_values = [
        {
            'large_box': 0,
            'average_box': 0,
            'small_box': 1,
            'multiply': 0
        },
        {
            'large_box': 0,
            'average_box': 0,
            'small_box': 1,
            'multiply': 0
        },
        {
            'large_box': 0,
            'average_box': 0,
            'small_box': 1,
            'multiply': 0
        },
        {
            'large_box': 0,
            'average_box': 1,
            'small_box': 0,
            'multiply': 0
        },
        {
            'large_box': 0,
            'average_box': 1,
            'small_box': 0,
            'multiply': 0
        },
        {
            'large_box': 0,
            'average_box': 1,
            'small_box': 0,
            'multiply': 0
        },
        {
            'large_box': 1,
            'average_box': 0,
            'small_box': 0,
            'multiply': 0
        },
        {
            'large_box': 1,
            'average_box': 0,
            'small_box': 0,
            'multiply': 0
        },
        {
            'large_box': 1,
            'average_box': 0,
            'small_box': 0,
            'multiply': 0
        },
        {
            'large_box': 0,
            'average_box': 2,
            'small_box': 0,
            'multiply': 1
        },
        {
            'large_box': 0,
            'average_box': 2,
            'small_box': 0,
            'multiply': 1
        },
        {
            'large_box': 0,
            'average_box': 2,
            'small_box': 0,
            'multiply': 1
        },
        {
            'large_box': 2,
            'average_box': 0,
            'small_box': 0,
            'multiply': 1
        },
        {
            'large_box': 2,
            'average_box': 0,
            'small_box': 0,
            'multiply': 1
        },
        {
            'large_box': 2,
            'average_box': 0,
            'small_box': 0,
            'multiply': 1
        },
        {
            'large_box': 2,
            'average_box': 0,
            'small_box': 0,
            'multiply': 1
        },
        {
            'large_box': 2,
            'average_box': 0,
            'small_box': 0,
            'multiply': 1
        },
        {
            'large_box': 2,
            'average_box': 0,
            'small_box': 0,
            'multiply': 1
        },
        {
            'large_box': 2,
            'average_box': 0,
            'small_box': 1,
            'multiply': 1
        },
        {
            'large_box': 2,
            'average_box': 0,
            'small_box': 1,
            'multiply': 1
        },
        {
            'large_box': 2,
            'average_box': 0,
            'small_box': 1,
            'multiply': 1
        },
        {
            'large_box': 2,
            'average_box': 1,
            'small_box': 0,
            'multiply': 1
        },
        {
            'large_box': 2,
            'average_box': 1,
            'small_box': 0,
            'multiply': 1
        },
        {
            'large_box': 2,
            'average_box': 1,
            'small_box': 0,
            'multiply': 1
        },
        {
            'large_box': 3,
            'average_box': 0,
            'small_box': 0,
            'multiply': 1
        },
        {
            'large_box': 3,
            'average_box': 0,
            'small_box': 0,
            'multiply': 1
        },
        {
            'large_box': 3,
            'average_box': 0,
            'small_box': 0,
            'multiply': 1
        },
        {
            'large_box': 3,
            'average_box': 0,
            'small_box': 1,
            'multiply': 2
        },
        {
            'large_box': 3,
            'average_box': 0,
            'small_box': 1,
            'multiply': 2
        },
        {
            'large_box': 3,
            'average_box': 0,
            'small_box': 1,
            'multiply': 2
        },
        {
            'large_box': 3,
            'average_box': 1,
            'small_box': 0,
            'multiply': 2
        },
        {
            'large_box': 3,
            'average_box': 1,
            'small_box': 0,
            'multiply': 2
        },
        {
            'large_box': 3,
            'average_box': 1,
            'small_box': 0,
            'multiply': 2
        },
        {
            'large_box': 4,
            'average_box': 0,
            'small_box': 0,
            'multiply': 2
        },
        {
            'large_box': 4,
            'average_box': 0,
            'small_box': 0,
            'multiply': 2
        },
        {
            'large_box': 4,
            'average_box': 0,
            'small_box': 0,
            'multiply': 2
        },
    ]

    generator = GeneratorOrderBox()

    def test_box_quantity(self):
        for index, value in enumerate(self.correct_values, 1):
            self.assertDictEqual(value, self.generator.get_box_quantity(index))

    def test_raise_lower_than_zero(self):
        with self.assertRaises(OrderSizeException) as context:
            self.generator.__check_quanity__(-1)
            self.assertTrue('Quantity not allowed!' in context.exception)

    def test_raise_greaten_than_hundred(self):
        with self.assertRaises(OrderSizeException) as context:
            self.generator.__check_quanity__(101)
            self.assertTrue('Quantity not allowed!' in context.exception)


if __name__ == '__main__':
    unittest.main()
