""" QUESTIONS ANSWERED: 

    8) If I insert n strings in sorted order, length of self._underlying is
        2^(n)-1.

    Comparing space for Weirdo and TreeNode
        If WeirdoBST is a bushy tree like our Z, M, F example we did as test,
        then there will be very little wasted space. This is where the gap is
        small compared to a TreeNode Binary Tree which doesn't waste space.
        Catostrophic events will occur if we have values that create wasted 
        space. For example A, B, C, D, E, F -> Each value is bigger than 
        previous creating 2^(6)-1 spaces along with it which is A LOT of waste.

    Heap's Array
        A heap array doesn't waste space because it focuses on the array being
        complete. Every level of a heap has to be filled from left to right
        before inputting values into the next level, allowing there to only be 
        values that actually exist (no Nones).
"""


class WeirdoBST:


    def __init__(self):
        # Our underlying array
        self._underlying: list[str | None] = []
        # Variable to keep track of "n" so we can call it in our len method
        self._n: int = 0

    def __str__(self) -> str:
        """Method to return a well formatted string for our underlying list.
        """
        return f"{self._underlying}"
    
    def insert(self, value: str) -> None:
        """Insert a string into the Binary Search Tree. Assumption of no
        duplicates will be used for simplicity.
        """
        # Variable to end loop when we insert
        inserted: bool = False
        # Variable so our parent we're working with is at "i" everytime
        # start at 0 for first index of self._underlying
        i: int = 0
        while not inserted:
            # Build the size of array as we go
            while i >= len(self._underlying):
                self._underlying.append(None)
            if self._underlying[i] is None:
                # If we find the spot we're supposed 
                self._underlying[i] = value
                inserted = True
                self._n += 1
            elif value < self._underlying[i]:
                # If value is less than parent go left
                i = self._left(i)
            elif value > self._underlying[i]:
                # if value is greater than parent go right
                i = self._right(i)
            else:
                # Duplicate, we just have to ignore and end loop
                inserted = True
    
    # Helper methods for left and right children
    def _left(self, parent: int) -> int:
        return 2 * parent + 1
    
    def _right(self, parent: int) -> int:
        return self._left(parent) + 1
    
    def search(self, value: str) -> bool:
        """Search through the Binary Search Tree to see if a value exists. If
        it does, this method will return a boolean that is true, if not, it
        it will return a boolean that is false.
        """
        # Bool to return if found value
        found: bool = False
        # index to keep our loop functioning
        i: int = 0
        while not found and i < len(self._underlying):
            if self._underlying[i] is None:
                # This is our condition if we find a value with "None"
                # Here we make sure our loop exists so we make i > len of list
                i += len(self._underlying)
            elif value == self._underlying[i]:
                # If same as our value, exit loop
                found = True
            elif value < self._underlying[i]:
                # If value is less, go left
                i = self._left(i)
            elif value > self._underlying[i]:
                # If value is greater, go right
                i = self._right(i)
        return found
            
    def __len__(self) -> int:
        """Method that returns the number of actual strings stored in the
        underlying list.
        """
        return self._n