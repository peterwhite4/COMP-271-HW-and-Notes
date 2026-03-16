from __future__ import annotations
import unittest

# The following line requires the presence of file backpack.py in the same
# folder as this week07.py file.
from backpack import Backpack


class Test_Backpack(unittest.TestCase):
    
    def test_empty_new_backpack(self):
        """Test to see if new backpack is created empty."""
        new_backpack = Backpack("Peter")
        # See if count is correct, no items are in, and is_full is false
        self.assertTrue(new_backpack.count() == 0)
        self.assertEqual(new_backpack.items(), [])
        self.assertFalse(new_backpack.is_full())

    def test_default_capacity(self):
        """Test to see if the default capacity of a backpack is five."""
        new_backpack = Backpack("Peter")
        # Add 5 items to backpack, use a loop to reduce redundancy
        items = ["1", "2", "3", "4", "5"]
        for item in items:
            self.assertTrue(new_backpack.add_item(item))
        self.assertTrue(new_backpack.count() == 5)
        self.assertTrue(new_backpack.is_full())

    def test_increasing_count(self):
        """Test to see if the count correctly increases."""
        new_backpack = Backpack("Peter")
        items = ["1", "2", "3", "4", "5"]
        # Create counter variable to compare to item count to verify it works
        test_count: int = 0
        for item in items:
            # This count starts at 0 so we put index at start of loop
            test_count += 1
            new_backpack.add_item(item)
            self.assertEqual(new_backpack.count(), test_count)

    def test_insertion_order(self):
        """Test the insertion order when items are added."""
        new_backpack = Backpack("Peter")
        items = ["1", "2", "3", "4", "5"]
        for item in items:
            new_backpack.add_item(item)
        # See if the list in backpack items is in the same order as the list
        # we added - Insertion order should be the same and True
        self.assertEqual(new_backpack.items(), items)

    def test_full_capacity(self):
        """Test to see if backpack functions correctly at full capacity."""
        new_backpack = Backpack("Peter")
        items = ["1", "2", "3", "4", "5"]
        for item in items:
            new_backpack.add_item(item)
        # Make sure it didn't add 6th item and count is still 5
        self.assertFalse(new_backpack.add_item("6"))
        # Make sure it didn't add to count or change contents
        self.assertTrue(new_backpack.count() == 5)
        self.assertEqual(new_backpack.items(), items)

    def test_removing_existing_item(self):
        """Test if removing an item that exists already functions correctly."""
        new_backpack = Backpack("Peter")
        items = ["1", "2", "3", "4", "5"]
        for item in items:
            new_backpack.add_item(item)
        # Remove item "3" - Should return true
        self.assertTrue(new_backpack.remove_item("3"))
        # See if backpack count correctly went down 1
        self.assertTrue(new_backpack.count() == 4)

    def test_removing_missing_item(self):
        """Test if removing an item that doesn't exist functions correctly."""
        new_backpack = Backpack("Peter")
        items = ["1", "2", "3", "4", "5"]
        for item in items:
            new_backpack.add_item(item)
        # Remove item "6". It doesn't exist it our items list
        self.assertFalse(new_backpack.remove_item("6"))
        # Make sure count stays at 5
        self.assertTrue(new_backpack.count() == 5)

    def test_adding_and_removing_duplicates(self):
        """Test to see if adding and removing duplicate strings functions
        correctly.
        """
        new_backpack = Backpack("Peter")
        items = ["1", "1", "1", "1", "1"]
        # Loop to add
        for item in items:
            self.assertTrue(new_backpack.add_item(item))
        self.assertTrue(new_backpack.count() == 5)
        # One test to see if we can remove just one duplicate item
        self.assertTrue(new_backpack.remove_item("1"))
        self.assertTrue(new_backpack.count() == 4)

    def test_is_full(self):
        """Test to see if the method is_full is correctly working."""
        new_backpack = Backpack("Peter")
        items = ["1", "2", "3", "4"]
        # Check first four items, is_full should be false
        for item in items:
            new_backpack.add_item(item)
            self.assertFalse(new_backpack.is_full())
        # Check is_full and count in addition of last item.
        new_backpack.add_item("5")
        self.assertTrue(new_backpack.count() == 5)
        self.assertTrue(new_backpack.is_full())

    def test_items_return_and_mutation(self):
        """Test to see if items() is functioning correctly. It should create
        a copy and not allow for itself to be mutated directly.
        """
        new_backpack = Backpack("Peter")
        # Add items to the list
        items = ["1", "2", "3"]
        for item in items:
            new_backpack.add_item(item)
        # Make a list equal to items(), mutating this shouldn't change items()
        item_list = new_backpack.items()
        # Add something to the new list
        item_list.append("4")
        # Check and make sure everything went as it should
        self.assertNotEqual(new_backpack.items(), item_list)
        self.assertEqual(new_backpack.items(), items)
        self.assertTrue(new_backpack.count() == 3)

    def test_str_method(self):
        """Test to see if the __str__ method is returning what it should when
        needed.
        """
        new_backpack = Backpack("Peter")
        # Make sure that an empty string returns as direction says
        self.assertEqual(str(new_backpack),
                         "Backpack(owner=Peter, items=empty)"
                         )
        # Make a loop to add items and check the string
        # (could do manually, but this is much easier and less redundant)
        items = ["1", "2", "3", "4"]
        # Make a index to pull number of items/5 in loop
        index: int = 1
        for item in items:
            new_backpack.add_item(item)
            self.assertEqual(str(new_backpack),
                             "Backpack(owner=Peter, items=" + str(index) + "/5)"
                             )
            index += 1


# ----- Run the tests
#
# If you test in a .PY file, uncomment TEST-LINE-1 and TEST-LINE-2 and
# comment out TEST-LINE-3 to run the tests.
#
if __name__ == "__main__":              #   TEST-LINE-1
    unittest.main()                     #   TEST-LINE-2
#
# If you test in a Jupyter notebook, comment out TEST-LINE-1 and TEST-LINE-2
# and uncomment TEST-LINE-C to run the tests in the notebook.
#
# unittest.main(argv=[''], exit=False)    #   TEST-LINE-3

