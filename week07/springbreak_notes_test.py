from __future__ import annotations
import unittest

from week07.springbreak_notes import SpringBreak

class TestSpringBreak(unittest.TestCase):

    def test_empty_on_init(self):
        test_object = SpringBreak()
        self.assertTrue(test_object.count()==0)

    def test_add_items(self):
        test_object = SpringBreak()
        test_object.add_item("Chicago")
        self.assertTrue(test_object==1)

# Execute the tests
if __name__ == "__main__":
    unittest.main()