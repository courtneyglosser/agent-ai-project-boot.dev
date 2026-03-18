
# get_files_info/tests.py

import unittest
from functions.get_files_info import get_files_info


class TestCalculator(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_empty(self):
        try:
            result = get_files_info()
        except: 
            result = None
        self.assertEqual(result, None)

    def test_basic(self):
        result = get_files_info('.', '.')
        self.assertEqual(type(result), type(''))

    def test_calculator(self):
        result = get_files_info("calculator", ".")
        print(f"\nResult:\n{result}\n\n")
        self.assertEqual(type(result), type(''))

    def test_pkg(self):
        result = get_files_info("calculator", "pkg")
        print(f"\nResults:\n{result}\n\n")
        self.assertEqual(type(result), type(''))

    def test_bin(self):
        result = get_files_info("calculator", "/bin")
        print(f"\nResults:\n{result}\n\n")
        self.assertEqual(type(result), type(''))

    def test_previous(self):
        result = get_files_info("calculator", "../")
        print(f"\nResults:\n{result}\n\n")
        self.assertEqual(type(result), type(''))



if __name__ == "__main__":
    unittest.main()


