# test_metafault.py
"""
Tests for MetaFault module.
"""

import unittest
from metafault import MetaFault

class TestMetaFault(unittest.TestCase):
    """Test cases for MetaFault class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MetaFault()
        self.assertIsInstance(instance, MetaFault)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MetaFault()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
