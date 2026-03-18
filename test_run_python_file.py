
import unittest
from functions.run_python_file import run_python_file


class TestRunPythonFile(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_empty(self):
        try:
            result = run_python_file()
        except: 
            result = None
        self.assertEqual(result, None)

    def test_calculator_main(self):
        result = run_python_file("calculator", "main.py")
        print(f"Results:\n{result}\n\n")
        self.assertEqual(type(result), type(''))

    def test_calculator_add(self):
        result = run_python_file("calculator", "main.py", ["3 + 5"])
        print(f"Results:\n{result}\n\n")
        self.assertEqual(type(result), type(''))

    def test_calculator_tests(self):
        result = run_python_file("calculator", "tests.py")
        print(f"Results:\n{result}\n\n")
        self.assertEqual(type(result), type(''))

    def test_calculator_up_dir(self):
        result = run_python_file("calculator", "../main.py")
        print(f"Results ../main.py:\n{result}\n\n")
        self.assertEqual(type(result), type(''))

    def test_calculator_non_exist(self):
        result = run_python_file("calculator", "nonexistent.py")
        print(f"Results:\n{result}\n\n")
        self.assertEqual(type(result), type(''))

    def test_calculator_non_python(self):
        result = run_python_file("calculator", "lorem.txt")
        print(f"Results:\n{result}\n\n")
        self.assertEqual(type(result), type(''))


if __name__ == "__main__":
    unittest.main()

