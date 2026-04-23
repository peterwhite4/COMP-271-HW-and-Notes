from __future__ import annotations


class NameBins:

    # Constants for no magic values
    _ZERO: int = 0
    _ONE: int = 1
    _EMPTY: str = "Empty Structure"
    _A_ASCII_VALUE: int = 65
    _ALPHABET_SIZE: int = 26

    def __init__(self, n: int) -> None:
        """Initialize our underlying, n, and counter for our class."""
        self._number_of_bins = n
        self._underlying = []
        # Add an empty array for the amount of bins given
        for i in range(self._number_of_bins):
            self._underlying.append([])
        # Counter that is used in add_name and then called for size
        self._counter: int = 0

    def __str__(self) -> str:
        """String method to return a nicely formatted representation of the
        underlying structure.
        """
        # Create our string to return if empty (declared outside because magic)
        result = self._EMPTY
        # Make sure we have something inside underlying
        if self._counter > 0:
            # Clear out our result string
            result = ""
            # Go through each bin (n)
            for i in range(self._number_of_bins):
                # Write down what is in each bin (use i + 1 because of 0 index)
                result += f"Bin {i + 1}: {self._underlying[i]}\n"
        return result
    
    def _letters_per_bin(self) -> int:
        """Helper method to make last bin smaller than the other bins and\
        allow for add_name to function correctly.
        """
        # I emailed you previously about how I could fix my add_name method.
        # With your reply and the hint email you gave us on Thursday morning,
        # I was able to figure out I needed to try to implement "ceiling"
        # acting math, to which I used the ceiling formula which is (a+b-1)/b 
        # which I've done in this helper method. This makes the first initial
        # bins bigger, with the final bin being smaller
        return (self._ALPHABET_SIZE + 
                self._number_of_bins - self._ONE) // self._number_of_bins

    def add_name(self, name: str) -> None:
        """Method to add a name to the underlying. This method will use integer
        division to determine what set of letters correspond to which bins. 
        This method doesn't use any conditional statements like "if". We are 
        able to assume the first letter of the names is capital and in the
        english alphabet due to the directions.
        """
        # Get the alphabetical value of the first letter in the name
        first_letter = ord(name[self._ZERO]) - self._A_ASCII_VALUE
        
        # Now we know amount of letters per bin due to ceiling division, we get
        # the correct bin number for this first corresponding letter
        assigned_bin = first_letter // self._letters_per_bin()

        # Append the name to the correct bin we have found
        self._underlying[assigned_bin].append(name)

        # Increment our counter
        self._counter += 1

    def size(self) -> int:
        """Method to return the total number of names in all bins."""
        return self._counter
