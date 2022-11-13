from one_hot_encoder import fit_transform
import unittest


class TestOHE(unittest.TestCase):

    def test_fit_transform_1(self):
        """Test 1 with assertEqual"""
        colors = ['red', 'red', 'green', 'blue', 'green']
        exp_transformed_colors = [
            ('red',   [0, 0, 1]),
            ('red',   [0, 0, 1]),
            ('green', [0, 1, 0]),
            ('blue',  [1, 0, 0]),
            ('green', [0, 1, 0]),
        ]
        transformed_colors = fit_transform(colors)
        self.assertEqual(transformed_colors, exp_transformed_colors)

    def test_fit_transform_2(self):
        """Test 2 with assertEqual"""
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        exp_transformed_cities = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        transformed_cities = fit_transform(cities)
        self.assertEqual(transformed_cities, exp_transformed_cities)

    def test_fit_transform_3(self):
        """Test 3 with assertIn"""
        words = ['hello', 'word']
        exp_transformed_words = [
            ('hello', [0, 1]),
            ('word',  [1, 0]),
        ]
        transformed_words = fit_transform(words)
        self.assertIn(exp_transformed_words[0], transformed_words)
        self.assertIn(exp_transformed_words[1], transformed_words)

    def test_fit_transform_4(self):
        """Test 4 with assertNotIn"""
        words = ['hello', 'word']
        transformed_words = fit_transform(words)
        self.assertNotIn(('hello', [1, 0]), transformed_words)

    def test_fit_transform_exception_1(self):
        """Test 1 that an exception is raised"""
        with self.assertRaises(TypeError) as cm:
            fit_transform()
        self.assertEqual(cm.exception.args[-1],
                         'expected at least 1 arguments, got 0')

    def test_fit_transform_exception_2(self):
        """Test 2 that an exception is raised"""
        with self.assertRaises(TypeError) as cm:
            fit_transform(1)
        self.assertEqual(cm.exception.args[-1],
                         "'int' object is not iterable")


if __name__ == '__main__':
    unittest.main()
