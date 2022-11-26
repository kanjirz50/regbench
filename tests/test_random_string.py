import unittest

from regbench.random_string import (
        generate_random_string,
        generate_random_string_contains_expected
)


class TestGenerateRandomString(unittest.TestCase):
    def test_generate(self):
        self.assertEqual(len(generate_random_string(10)), 10)
        self.assertEqual(len(generate_random_string(1)), 1)
        self.assertIsInstance(generate_random_string(0), str)

    def test_generate_empty(self):
        self.assertEqual(len(generate_random_string(0)), 0)
        self.assertEqual(generate_random_string(0), '')
        self.assertIsInstance(generate_random_string(0), str)

        self.assertEqual(len(generate_random_string(-1)), 0)
        self.assertEqual(generate_random_string(-1), '')
        self.assertIsInstance(generate_random_string(-1), str)


class TestGenerateRandomStringContainsExpected(unittest.TestCase):
    def test_generate(self):
        self.assertEqual(
            len(generate_random_string_contains_expected('test', 100)),
            100
        )
        self.assertEqual(
            len(generate_random_string_contains_expected('test', 10)),
            10
        )
        self.assertIsInstance(
            generate_random_string_contains_expected('test', 10),
            str
        )
        self.assertIn(
            'test',
            generate_random_string_contains_expected('test', 6),
        )
        self.assertNotIn(
            'test',
            generate_random_string_contains_expected('hoge', 6),
        )

    def test_invalid_generate(self):
        with self.assertRaises(ValueError):
            generate_random_string_contains_expected('test', 2)


if __name__ == '__main__':
    unittest.main()
