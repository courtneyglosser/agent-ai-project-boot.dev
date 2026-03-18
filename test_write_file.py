

# write_file tests

import unittest
from functions.write_file import write_file


class TestWriteFile(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_empty(self):
        try:
            result = write_file()
        except: 
            result = None
        self.assertEqual(result, None)

    def test_write_lorem(self):
        content = "wait, this isn't lorem ipsum"
        result = write_file('calculator', 'lorem.txt', content)
        print(f"Results:\n{result}\n\n")
        self.assertEqual(type(result), type(''))

    def test_write_more_lorem(self):
        content = "lorem ipsum dolor sit amet"
        result = write_file("calculator", "pkg/morelorem.txt", content)
        print(f"\nResult:\n{result}\n\n")
        self.assertEqual(type(result), type(''))

    def test_root_access(self):
        content = "This shouldn't be allowed."
        result = write_file("calculator", "/tmp/temp.txt", content)
        print(f"\nResults:\n{result}\n\n")
        self.assertEqual(type(result), type(''))




if __name__ == "__main__":
    unittest.main()


