from __future__ import annotations


class ProbingHashTable:
    """Hash table demonstrating linear vs. quadratic probing."""

    # Consstants for default values and error messages
    _DEFAULT_CAPACITY: int = 11
    _PROBE_MODES: tuple[str, str] = ("linear", "quadratic")
    _DEFAULT_PROBING_MODE: str = _PROBE_MODES[0]
    _ERROR_MODE: str = f"mode must be one of {', '.join(_PROBE_MODES)}"
    _ERROR_FULL: str = "Hash table is full"

    def __init__(
        self, capacity: int = _DEFAULT_CAPACITY, mode: str = _DEFAULT_PROBING_MODE
    ):
        """Initialize the hash table with the given capacity and probing mode."""
        if mode not in self._PROBE_MODES:
            # If the mode is not valid,
            # use default mode.
            mode = self._DEFAULT_PROBING_MODE
        self._capacity = capacity
        self._mode = mode
        # Each slot is a string or None
        self._table: list[str | None] = [None] * capacity
        self._size = 0

    def _hash(self, key: int) -> int:
        """Convert an integer value to an index in the underlying table."""
        return key % self._capacity

    def _probe(self, position: int, attempt: int) -> int:
        """"""
        if self._mode == self._DEFAULT_PROBING_MODE:  # linear
            return (position + attempt) % self._capacity
        else:  # quadratic
            return (position + attempt * attempt) % self._capacity

    def load_factor(self) -> float:
        """Return the current load factor of the hash table."""
        return self._size / self._capacity

    def insert(self, value: str) -> list[int]:
        """Insert key-value pair. Returns list of indices probed."""
        # Initialize list to track probe indices
        probes: list[int] = []
        # Check if the hash table has space for a new entry.
        # If not, we will not attempt to insert and will return
        # an empty list of probes.
        if self._size < self._capacity:
            # Generate a non-negative integer key from the value
            key: int = abs(hash(value))
            # Convert the key to an index in the underlying table
            index: int = self._hash(key)
            # Attempt to insert the key-value pair, probing for an empty
            # slot.
            i: int = 0
            insertion_successful: bool = False
            # Loop to attempt to find an empty slot. The loop ends as soon as
            # we have probed the entire table or successfully inserted the
            # value.
            while i < self._capacity and not insertion_successful:
                # Location in the underlying table to check
                probe_index: int = self._probe(index, i)
                # Record the location we are probing
                probes.append(probe_index)
                # Obtain the contents at the location we are probing
                slot: str | None = self._table[probe_index]
                # Determine if we can insert the value at the location we are probing.
                # If insertion is successful, we will exit the loop. If not, we will
                # try the next probe index in the next iteration of the loop.
                insertion_successful = slot is None or slot == value
                if insertion_successful:
                    # The slot is empty or contains the same value already,
                    # so we can insert the value pair here (or update the existing
                    # value if it is the same).
                    self._table[probe_index] = value
                    if slot is None:
                        # Update the size of the hash table if we added
                        # this value for the first time, ie, we have not
                        # overwriten it.
                        self._size += 1
                # If the slot is not empty, we will try the next probe index
                # in the next iteration of the loop.
                i += 1
        return probes

    def contains(self, value: str) -> bool:
        """Check if value is in the hash table."""
        # Generate a non-negative integer key from the value
        key: int = abs(hash(value))
        # Convert the key to an index in the underlying table
        index: int = self._hash(key)
        # Loop to probe for the value. The loop ends as soon as we have probed the
        # entire table or found the value.
        found: bool = False
        i: int = 0
        # Loop ends when we have probed the entire table or found the value
        while i < self._capacity and not found:
            probe_index: int = self._probe(index, i)
            slot: str | None = self._table[probe_index]
            if slot is not None:
                found = slot == value
            i += 1
        return found

    # Formating constants for display
    _FMT_HEADER: str = f"{'Idx':<5}{'Content'}"
    _FMT_EMPTY: str = "---"
    _FMT_SLOT: str = "{idx:5} -> {content}"
    _FMT_HORIZONTAL: str = "-" * 20

    def display(self) -> str:
        """Return a string representation of the hash table."""
        lines: list[str] = [self._FMT_HEADER]
        lines.append(self._FMT_HORIZONTAL)
        for i in range(self._capacity):
            slot: str | None = self._table[i]
            content: str = (
                self._FMT_SLOT.format(idx=i, content=slot) if slot else self._FMT_EMPTY
            )
            lines.append(content)
        return "\n".join(lines)

 
# MY DEMO / Simulation - Derived from your demo and your help of my outline
# I had a good amount of trouble figuring out the failed insertions. Found
# The easiest way for it to function was to track the count as discussed in
# Option A

import random
import string

capacity: int = 101

modes: tuple[str, str] = ("linear", "quadratic")

def random_string(n: int) -> str:
    """Generate a random string of length n using alphabetical characters."""
    return "".join(random.choices(string.ascii_letters, k=n))

def simulation(trials: int):
    """My simulation (using teacher template from directions and help) that
    covers linear and quadratic probing. This method will record the load
    factor and average probes after each insertion.
    """

    # Raise error if trials amount is too large.
    if trials > capacity:
        raise IndexError(
            f"Invalid Number of trials. "
            f"Trials must be <= {capacity}")
    
    # Used from your demo - Helps with start of my simulation
    for mode in modes:

        # Where all of our probes for trials will be located
        # Table 1 is index 0 in probe_collection. First probe of table 1 will 
        # be index 0
        probe_collection: list[list[int]] = []
        # Initiate variable to keep count of failures (Option A) 
        failure_count = 0
        # Initiate amount of simulations want to run
        tables_count = 25 # Create 25 different tables - multiple trials

        for _ in range(tables_count):
            ht = ProbingHashTable(capacity=capacity, mode=mode)
            # Keep track of probes from each table seperately
            table_probes: list[int] = []
            for _ in range(trials):
                # Keep track of load factor before insertion
                before_insertion = ht.load_factor()
                # Generate random string
                value: str = random_string(5)
                # Insert random string
                probes: list[int] = ht.insert(value)
                # Track load factor after insertion in variable
                after_insertion = ht.load_factor()
                # If load factor DIDN'T change after insertion was attempted
                if before_insertion == after_insertion:
                    # Failure
                    failure_count += 1
                else:
                    # Append to this trial's probe list
                    table_probes.append(len(probes))
                        
            # Append this table's probes list to collection list
            probe_collection.append(table_probes)

        # Average the probes
        avg_probes: list[float] = []
        # Loop as many times as trials
        for i in range (trials):
            probe_sum: int = 0
            # Amount of probes in a trial
            probe_count: int = 0
            # Look at each table in probe_collection [list[list]]
            for table in probe_collection:
                # Make sure that insertions suceeded. If they didn't, 
                # don't look at their probes
                if i < len(table):
                    # Take element i in this trial and add it to total at "i"
                    probe_sum += table[i]
                    probe_count += 1
            # Now that we have total from all the tables at position/load
            # factor "i" & average them with the amount of trials that occured
            probe_average: float = probe_sum / probe_count
            # Append to final probe list that will print averages
            avg_probes.append(probe_average)

        # Print results
        print(f"{mode} probing | Capacity = {capacity}\n")
        # Have to make a loop to print the load factor and avg_probes together
        for i in range(trials):
            print(
                f"{i+1}: " # Insertion number
                # I had to look up how to round decimal places
                # Determine load factor through capacity (i+1 for readability)
                f"Load Factor = {round((i+1)/capacity, 3)}      "    
                f"Probe Average = {round(avg_probes[i], 3)}     "
                )
        print("\n")
        print (f"Failed Insertion Attempts = {failure_count}")
        print("\n")

if __name__ == "__main__":
    simulation(101)       