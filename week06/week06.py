"""MIDTERM ASSIGNMENT - Peter White"""

from __future__ import annotations  # Authorized import for advanced type hints
from abc import ABC, abstractmethod  # Authorized import for derived classes


# PROBLEMS 1-3 -> CODEBASE A
class Node:
    """A simple linkable object. The node comprises two fields: a value field,
    here typed a string, and a pointer field to the next node. The default is
    to instantiate a node with just a value, and no other node to point to it,
    for example:

    +------+
    | node |-next--> None
    +------+

    Nodes are connected to each other later, for example,

    chi = Node("Chicago")        spi = Node("Springfield")
    +------+                     +------+
    | node |-next--> None        | node |-next--> None
    +------+                     +------+

    and then chi.set_next(spi) will result to the arrangement below which is,
    essentially, a linked list.

    chi -----------------------> spi

    +------+                     +------+
    | node |-next--------------> | node |-next--> None
    +------+                     +------+

    """

    def __init__(self, value: str) -> None:
        """Object constructor. Requires only a value to instantiate the object.
        The next object may be assigned later"""
        self.__value: str = value
        self.__next: Node | None = None

    def __str__(self) -> str:
        """Simple string representation of the object."""
        return f"{self.__value}"

    def has_next(self) -> bool:
        """Predicate accessor; tells if object points to
        another object"""
        return self.__next is not None

    def get_next(self) -> Node | None:
        """Standard accessor for next object"""
        return self.__next

    def set_next(self, next: Node) -> None:
        """Mutates object by assigning its next pointer to another object"""
        self.__next = next

    def get_value(self) -> str:
        """Accessor for the object's value"""
        return self.__value


class LinkedList:
    """A simple linked list of Node objects. Nodes in this list are
    connected one after the other, as shown below

      head
    +------+         +------+         +------+        +------+
    | node |-next--> | node |-next--> | node |--> ... | node |-next-->  None
    +------+         +------+         +------+        +------+

    Every node, in the linked list, is connected to another node. Except for
    the last node that points to None.

    Problem 1: This modification of the LinkedList class creates a new way 
    to add a new node to the end of the list. Previously, traversing through
    the whole list was neccessary to add a new node. My modification created
    a reference to the tail node which then allows for the addition of new 
    nodes to be easier. This is done by referencing to the previous tail node,
    followed by updating the old tail node to the new tail node.

    Problem 2: This modification of the LinkedList class creates a simpler
    way to keep track of the number of nodes in the linked list. Previously,
    the counter method looped through the whole list of nodes to get the
    length of the linked list. Now, everytime a node is added, the counter 
    variable is updated, which can be called at anytime through the counter 
    method.
    """

    def __init__(self) -> None:
        """Instantiate an empty linked list"""
        self.__head: Node | None = None
        # Create a reference of the last node (Problem 1)
        self.__tail: Node | None = None
        # Create a counter
        self.__counter: int = 0

    # Constants for string representation of the linked list
    __EMPTY_LIST_STR: str = "Empty List"
    __RIGHT_ARROW: str = " → "

    def __str__(self) -> str:
        """String representation."""
        # Assume an empty list
        string: str = self.__EMPTY_LIST_STR
        if self.__head is not None:
            # If the list is not empty, we start with the head node and
            # we keep adding the value of the next node, until we reach
            # the end of the list.
            string = self.__head.get_value()
            # Start with the first node and keep adding the next node
            # until we reach the end of the list.
            current: Node = self.__head.get_next()
            while current is not None:
                # Add the next node to the string and move to the next
                # node. The loop ends when we reach the end of the list
                # and current is None.
                string += self.__RIGHT_ARROW + current.get_value()
                current = current.get_next()
        return string

    def add(self, value: str) -> None:
        """Adds a new node to the linked list. First we create a new node
        with the given value. If there is no linked list, the new node will
        become both the head and tail of the new list. If our list already has
        nodes, we will place the new node after the tail node, and then make 
        that node the new tail node.
        """
        # Create the new node to be added
        new_node: Node = Node(value)
        # Determine if the linked list is empty.
        if self.__head is None:
            # If the list is empty, the new node becomes its head AND tail
            # and then we are done.
            self.__head = new_node
            self.__tail = new_node
            # Add 1 to counter
            self.__counter += 1
        else:
            # Put the new node after the previous tail node
            self.__tail.set_next(new_node)
            # Now, set the node as the new tail node
            self.__tail = new_node
            # Add 1 to counter
            self.__counter += 1

    def count(self) -> int:
        """Returns the number of nodes in the linked list."""
        return self.__counter
    
    def insert(self, new_value: str, after_value: str) -> bool:
        """This method inserts a new node using new_value. This is done
        after a node whose value equals after_value is found. If the new 
        node is successfuly inserted after after_value, the method returns
        True. If not, the method returns False.
        """
        # Create bool to return
        found: bool = False
        # We need to start at head of list. Makes code more readable too
        current_node: Node | None = self.__head
        # Loop through the list, check and make sure something is in the list
        while current_node is not None and not found:
            # If the current value is equal to a value in the list
            if current_node.get_value() == after_value:
                # We found a match
                found = True
                # Create new node
                new_node: Node = Node(new_value)
                # GET the node after current node, then point new node to it
                new_node.set_next(current_node.get_next())
                # Point the current node to the new node to finish insertion
                current_node.set_next(new_node)
                # Check and make sure the current node wasn't the tail
                if current_node == self.__tail:
                    # If current was the tail, update tail to new node
                    self.__tail = new_node
                # Update counter because we added a node
                self.__counter += 1
            else:
                # If we dont find a match, get next value in list and loop
                current_node = current_node.get_next()
        return found
    

# PROBLEM 4 -> CODEBASE B
class Performance(ABC):
    """
    A general live performance event.

    This class captures the shared structure and behavior of all
    live performances: concerts, lectures, theater productions,
    magic shows, etc.

    The purpose of this class is to define:

        • Common data that every performance has.
        • Common behavior shared by all performances.
        • A contract (via abstract methods) that subclasses must fulfill.

    Subclasses are responsible for defining how revenue is calculated
    and how the performance is described.
    """

    def __init__(
        self, title: str, duration_minutes: int, base_ticket_price: float
    ) -> None:
        """
        Initialize a new performance.

        Parameters:
            title               The name of the event.
            duration_minutes    How long the event lasts.
            base_ticket_price   The standard ticket price before
                                any subclass-specific adjustments.

        Note:
            We use protected attributes (_name style) instead of
            private (__name) because subclasses will need direct
            access to these values.
        """
        self._title: str = title
        self._duration_minutes: int = duration_minutes
        self._base_ticket_price: float = base_ticket_price

        # Number of audience members currently admitted.
        # Starts at zero and increases via admit_audience().
        self._audience_count: int = 0

    # ---------------------------------------------------------
    # Concrete (Fully Implemented) Methods
    # These are inherited as-is by subclasses.
    # ---------------------------------------------------------

    def __str__(self) -> str:
        """
        General string representation.

        We call describe() here so that when a Performance
        object is printed, the subclass version of describe()
        is used automatically (polymorphism in action).
        """
        return self.describe()

    def admit_audience(self, number: int) -> None:
        """
        Adds audience members to the performance.

        Only positive numbers are accepted.
        """
        if number > 0:
            self._audience_count += number

    def get_title(self) -> str:
        """Returns the performance title."""
        return self._title

    def get_duration(self) -> int:
        """Returns the duration in minutes."""
        return self._duration_minutes

    def get_audience_count(self) -> int:
        """Returns the number of admitted audience members."""
        return self._audience_count

    def get_base_ticket_price(self) -> float:
        """
        Returns the base ticket price.

        Subclasses may use this value as the starting point
        for their own pricing logic.
        """
        return self._base_ticket_price

    # ---------------------------------------------------------
    # Abstract Methods (Must Be Implemented by Subclasses)
    # ---------------------------------------------------------

    @abstractmethod
    def calculate_revenue(self) -> float:
        """
        Compute total revenue for the performance.

        Subclasses decide how ticket price is adjusted
        (VIP upgrades, student discounts, special pricing, etc.).

        The result should reflect:
            audience_count × adjusted_ticket_price
        """
        ...

    @abstractmethod
    def describe(self) -> str:
        """
        Return a human-readable description of the performance.

        Each subclass should include details specific
        to its type of event.
        """


class Concert(Performance):
    """A concert performance. This class calculates ticket price and revenue's
    for concert performances. If has_vip is True, ticket prices will increase
    by 40%.
    """

    # Constant for VIP increase
    __INCREASE: float = 1.4

    def __init__(self, title: str, duration_minutes: int, 
                 base_ticket_price: float, artist_name: str, 
                 genre: str, has_vip: bool) -> None:
        # Instantiate a Performance object by using its __init__
        super().__init__(title, duration_minutes, base_ticket_price)
        # Initialize attributes associated with Concert
        self._artist_name: str = artist_name
        self._genre: str = genre
        self._has_vip: bool = has_vip

    def adjusted_ticket_price(self) -> float:
        """This method is a helper method to calculate_revenue.
        It will check and see if has_vip is true, if it is, it will multiply
        the base_ticket_price by 1.4. If not, then the ticket price stays equal
        to the base_ticket_price, but copied to the adjusted_ticket_price 
        variable so we do not modify the original ticket price.
        """
        # Check bool
        if self._has_vip:
            # Calculate new ticket price if true
            adjusted_ticket_price = (
                self.get_base_ticket_price() * self.__INCREASE
                )
        else:
            # Copy base price to adjusted price to avoid changing base
            adjusted_ticket_price = self.get_base_ticket_price()
        # Return the price that will be used
        return adjusted_ticket_price

    def calculate_revenue(self) -> float:
        """Method derived from our Performance superclass. 
        This method will compute total revenue for the Concert performance.
        """
        revenue = self.get_audience_count() * self.adjusted_ticket_price()
        return revenue

    def describe(self) -> str:
        """Method derived from our Performance superclass.
        This method returns a readable description of the Concert performance.
        """
        return("Concert Title: " + self.get_title() + "\n"
              + "Artist: " + self._artist_name + "\n"
              + "Genre: " + self._genre + ""
              )
    

class Lecture(Performance):
    """A lecture performance. This class is able to describe and calculate 
    ticket prices and revenue for Lecture's using the super classes variables.
    If a lecture is_university_event, the ticket prices will be discounted by
    50%.
    """

    # Constant for discount
    __DISCOUNT: float = .5

    def __init__(self, title: str, duration_minutes: int, 
                 base_ticket_price: float, speaker_name: str,
                 is_university_event: bool) -> None:
        # Instantiate a Performance object by using its __init__
        super().__init__(title, duration_minutes, base_ticket_price)
        # Initiate fields specific to lecture
        self._speaker_name = speaker_name
        self._is_university_event = is_university_event

    def adjusted_ticket_price(self) -> float:
        """This method is a helper method to calculate_revenue. It will 
        check is_university_event is true, if it is, it will multiply the 
        base_ticket_price by .5. If not, then the ticket price stays equal to 
        the base_ticket_price, but copied to the adjusted_ticket_price 
        variable so we do not modify the original ticket price.
        """
        # Check bool
        if self._is_university_event:
            # Calculate new ticket price if true
            adjusted_ticket_price = (
                self.get_base_ticket_price() * self.__DISCOUNT
                )
        else:
            # Copy base price to adjusted price to avoid changing base
            adjusted_ticket_price = self.get_base_ticket_price()
        # Return the price that will be used
        return adjusted_ticket_price

    def calculate_revenue(self) -> float:
        """Method derived from our Performance superclass. 
        This method will compute total revenue for the lecture performance.
        """
        revenue = self.get_audience_count() * self.adjusted_ticket_price()
        return revenue
    
    def describe(self) -> str:
        """Method derived from our Performance superclass.
        This method returns a readable description of the lecture performance.
        """
        return("Lecture Title: " + self.get_title() + "\n"
                + "Speaker Name: " + self._speaker_name + ""
                )
                

# TEST CODE

# Given...
events: list[Performance] = [
    Concert("Summer Blast", 120, 50.0, "The Meteors", "Rock", True),
    Lecture("AI and Society", 90, 30.0, "Dr. Kwan", True)
]
# Create total revenue variable and set it equal to 0
total_revenue: float = 0.0
# For loop to admit 100 people, print desribes and revenue, and also add to
# total revenue
for event in events:
    # Admit 100 people
    event.admit_audience(100)
    # Printing the event calls the str method from the performance class
    print (event)
    revenue = event.calculate_revenue()
    print ("Revenue = $", revenue, "\n")
    # Add the revenue of this event to the total revenue
    total_revenue += revenue
# Print total revenue across all performances
print("Total Revenue = $", total_revenue, "\n")