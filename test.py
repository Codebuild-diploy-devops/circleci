import unittest
from main import convert_to_uppercase

class TestUppercaseFunction(unittest.TestCase):

    def test_lowercase_string(self):
        """Test that a standard lowercase string is correctly converted."""
        self.assertEqual(convert_to_uppercase("hello"), "HELLO")

    def test_mixed_case_string(self):
        """Test that a mixed-case string is completely capitalized."""
        self.assertEqual(convert_to_uppercase("PyThOn 2026"), "PYTHON 2026")

    def test_empty_string(self):
        """Test that an empty string returns an empty string."""
        self.assertEqual(convert_to_uppercase(""), "")

    def test_invalid_input_type(self):
        """Test that passing a non-string raises a TypeError."""
        with self.assertRaises(TypeError):
            convert_to_uppercase(123)

if __name__ == "__main__":
    unittest.main()
