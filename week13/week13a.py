
class Node:

    """A node in a linked list."""
    
    def __init__(self, value):
        self.__value = value
        self.__next = None

    def __str__(self):
        return str(self.__value)

    def get_value(self):
        return self.__value

    def get_next(self):
        return self.__next

    def set_next(self, next):
        self.__next = next

    def has_next(self):
        return self.__next != None


class LinkedList:
    """A simple linked list data structure."""

    def __init__(self):
        # Fields below are designated as protected (single
        # unferscore) instead of private (double underscore).
        # The objective is still to show other users that 
        # the fields are for internal-use only. And at the 
        # same time to avoid the complications from double
        # underscore name mangling.
        self._head = None
        self._tail = None
        self._size = 0

    def __str__(self):
        """Tragically simple string rendering"""
        result = ""
        current = self._head
        while current != None:
            result += str(current) + " "
            current = current.get_next()
        return result

    def add(self, new_node: Node) -> None:
        """Adds a new node to the linked list."""
        if new_node is not None:
            # Operate only if there is something given to
            # us to add.
            if self._head == None:
                self._head = new_node
            else:
                self._tail.set_next(new_node)
            # In either case, update the tail
            self._tail = new_node
            # Update the size of the object
            self._size += 1
    
    def add_with_string(self, value:str) -> None:
        if value is not None:
            self.add(Node(value))

    # Make a constant for setting things equal to None
    _NONE = None

    # My methods
    def remove(self, value: str) -> bool:
        """Removes a node from the linked list and correctly changes head,
        tail, and pointer nodes if neccessary.
        """
        # Set up our variable for our loop to function
        removed: bool = False
        # Start at head node -> this can be checked to see if empty as well
        current: str = self._head
        # Keep track of what node we just looked at
        previous: str = None
        # Make sure we remove the first node that matches AND
        # Check and see list is empty - also check and see if we are at end
        while not removed and current is not self._NONE:
            # Make sure value is equal to whatever node we're at
            if value == current.get_value():
                # Check to see if its the head
                if current == self._head:
                    # Check to see it is not just a one node linked list
                    if self._head.has_next():
                        self._head = self._head.get_next()
                    else:
                        # If head doesn't have next, it's also the tail 
                        self._head = self._NONE
                        self._tail = self._NONE
                # Check to see if its the tail in multi-node linked list
                elif current == self._tail:
                    # Set previous to new tail
                    self._tail = previous
                    # Set previous to point to None
                    self._tail.set_next(self._NONE)
                else:
                    # Previous node points to what current was previously
                    previous.set_next(current.get_next())
                # Decrement size and set removed to True
                # This is at bottom of loop because of refactoring
                self._size -= 1
                removed = True
            # Set previous and current to correct nodes before continuing
            previous = current
            # If next is None, our loop will end because of our while condition
            current = current.get_next()
        # Return the boolean are supposed to
        return removed

    # We previously discussed about calling the "remove" method to make this
    # method function, but I couldn't find a way to refactor this code without
    # making it to complicated for myself. I thought about it and looked at it
    # and since we keep moving through the loop even if we don't remove, I
    # would need to keep recalling my remove method which starts at the head
    # each time which is unncessary. A seperate method that looped linearly
    # made sense to me, like I have here.
    def remove_all(self, value: str) -> int:
        """Removes all nodes from the LinkedList that are the same as our
        value. This method will correctly point nodes after removing.
        It will return a integer that represents the number of values removed.
        """
        # Variable to return at end: amount of removes
        removed_count: int = 0
        # Start at head node
        current: str = self._head
        # Keep track of what node we just looked at
        previous: str = None
        # Make sure we go through whole linked list if not Empty or at end of
        # it - No need for index or removed variable because this is remove_all
        while current is not self._NONE:
            # Make sure value is equal to whatever node we're at
            if value == current.get_value():
                # Check to see if its the head
                if current == self._head:
                    # Check to see it is not just a one node linked list
                    if self._head.has_next():
                        self._head = self._head.get_next()
                        # Set current to the new head so we can keep looping
                        current = self._head
                    else:
                        # If head doesn't have next, it's also the tail 
                        self._head = self._NONE
                        self._tail = self._NONE
                # Check to see if its the tail in multi-node linked list
                elif current == self._tail:
                    # Set previous to new tail
                    self._tail = previous
                    # Set previous to point to None
                    self._tail.set_next(self._NONE)
                    # Loop will end now because we reached tail
                    current = self._NONE
                else:
                    # Previous node points to what current was previously
                    previous.set_next(current.get_next())
                    # Previous stays same, current goes to the next node
                    current = current.get_next()
                # Decrease the size and increase remove count
                self._size -= 1
                removed_count += 1
            else:
                # Update previous and current if we do not remove anything
                previous = current
                current = current.get_next()
        # Return the count of how many removed values occured
        return removed_count
