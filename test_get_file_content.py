
# get_file_content/tests.py

import unittest
from functions.get_file_content import get_file_content


class TestCalculator(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_empty(self):
        try:
            result = get_file_content()
        except: 
            result = None
        self.assertEqual(result, None)

    def test_truncate(self):
        result = get_file_content('calculator', 'lorem.txt')
        print(f"Results:\n{len(result)}\n\n")
        self.assertEqual(type(result), type(''))

    def test_main(self):
        result = get_file_content("calculator", "main.py")
        print(f"\nResult:\n{result}\n\n")
        self.assertEqual(type(result), type(''))

    def test_pkg_calculator(self):
        result = get_file_content("calculator", "pkg/calculator.py")
        print(f"\nResults:\n{result}\n\n")
        self.assertEqual(type(result), type(''))

    def test_bin_cat(self):
        result = get_file_content("calculator", "/bin/cat")
        print(f"\nResults:\n{result}\n\n")
        self.assertEqual(type(result), type(''))

    def test_no_file(self):
        result = get_file_content("calculator", "pkg/does_not_exist.py")
        print(f"\nResults:\n{result}\n\n")
        self.assertEqual(type(result), type(''))



if __name__ == "__main__":
    unittest.main()


