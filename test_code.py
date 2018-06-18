import unittest
from loader import FileLoader
__loader__ = FileLoader(__file__)


def test_code(globals):
    """Test the result of the code execution."""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestQuicksort)
    runner = unittest.TextTestRunner()
    runner.run(suite)
    
class TestQuicksort(unittest.TestCase):
    """Test the quicksort algorithm according to its specification."""
    
    def test_false(self):
        self.assertTrue(False)
