from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Tuple, Type, Union

# ADTs given
class QueueADT(ABC):
    @abstractmethod
    def enqueue(self, item: Any) -> None:
        pass

    @abstractmethod
    def dequeue(self) -> Any:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def size(self) -> int:
        pass

    @abstractmethod
    def peek(self) -> Any:
        pass


class StackADT(ABC):
    @abstractmethod
    def push(self, item: Any) -> None:
        pass

    @abstractmethod
    def pop(self) -> Any:
        pass

    @abstractmethod
    def peek(self) -> Any:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def size(self) -> int:
        pass


# My Queue class
class Queue(QueueADT):

    # No magics!
    _ZERO: int = 0
    _APPEND: str = 'at'
    _WRITE: str = 'wt'
    _READ: str = 'rt'
    _EMPTY_QUEUE: str = "Empty Queue"
    _NEWLINE: str = "\n"
    _TEMP_FILE: str = "temp.txt"

    def __init__(self, filename):
        """Set up file to be used."""
        self.filename = filename
        file = open(filename, self._APPEND)
        # Always close files at end of methods
        file.close()

    def __str__(self) -> str:
        """String representation of our Queue."""
        if not self.is_empty():
            string = "Queue in a file with " + str(self.size()) + " items."
        else:
            string = self._EMPTY_QUEUE
        return string

    def size(self) -> int:
        """Check the amount of lines in the Queue. Returns an int that accounts
        for the number of lines in the Queue.
        """
        file = open(self.filename, self._READ)
        # Create an index variable that is also our count.
        count: int = 0
        # Loop through the whole file while keeping count
        for line in file:
            count += 1
        file.close()
        return count

    def is_empty(self) -> bool:
        """Check if Queue is empty. Returns a booelean that is True if empty,
        False if not.
        """
        empty: bool = False
        if self.size() == self._ZERO:
            empty = True
        return empty

    def peek(self) -> Any:
        """Look and return at the front of the queue. This method will also
        check if the file is empty by using the is_empty method before peeking.
        It will return a copy of the string of the front of queue or a string
        stating that it couldn't peek succesfully.
        """
        file = open(self.filename, self._READ)
        # Make sure the queue is NOT empty
        if not self.is_empty():
            # Create a front_of_queue str where we can put the front string
            # to return it
            front_of_queue = file.readline()
        else:
            front_of_queue = self._EMPTY_QUEUE
        file.close()
        return front_of_queue

    
    def enqueue(self, item: Any) -> None:
        """Add to the Queue. This will append to the end of file since
        enqueuing something works in such way.
        """
        # use 'a' to automatically go to end of a file and append there
        file = open(self.filename, self._APPEND)
        file.write(item + self._NEWLINE)
        file.close()
    
    def dequeue(self) -> Any:
        """Dequeue the front item of the queue from the file. This method was
        tricky for me. This method makes a temporary file that copies all of 
        the contents of the original queue WITHOUT the front. This method then 
        rewrites the orignal file equal to the temp, therefore we successfully 
        dequeued the front.
        """
        # Create and open a temporary file to write and transfer the queue
        temp_file = open(self._TEMP_FILE, self._WRITE)
        file = open(self.filename, self._READ)
        # Make sure not empty
        if not self.is_empty():
            # Use peek to get the front of queue that we are going to dequeue
            front_of_queue = self.peek()
            # Skip first line of original file before loop
            file.readline()
            #           Add something here
            for line in file:
                temp_file.write(line)
        else:
            front_of_queue = self._EMPTY_QUEUE
        file.close()
        temp_file.close()

        # Now open original file as w and temp as r to transfer strings
        file = open(self.filename, self._WRITE)
        temp_file = open(self._TEMP_FILE, self._READ)
        for line in temp_file:
            file.write(line)
        file.close()
        temp_file.close()
        return front_of_queue


class Stack(StackADT):

    # No magics!
    _ZERO: int = 0
    _APPEND: str = 'at'
    _WRITE: str = 'wt'
    _READ: str = 'rt'
    _EMPTY_STACK: str = "Empty Stack"
    _NEWLINE: str = "\n"
    _TEMP_FILE: str = "temp.txt"

    def __init__(self, filename):
        """Set up file to be used for stack."""
        self.filename = filename
        file = open(filename, self._APPEND)
        # Always close files at end of methods
        file.close()

    def __str__(self) -> str:
        """String representation of our Stack."""
        if not self.is_empty():
            string = "Stack in a file with " + str(self.size()) + " items."
        else:
            string = self._EMPTY_STACK
        return string
    
    def size(self) -> int:
        """Check the amount of lines in the stack. Returns an int that accounts
        for the number of lines in the stack.
        """
        file = open(self.filename, self._READ)
        # Create an index variable that is also our count.
        count: int = 0
        # Loop through the whole file while keeping count
        for line in file:
            count += 1
        file.close()
        return count

    def is_empty(self) -> bool:
        """Check if stack is empty. Returns a booelean that is True if empty,
        False if not.
        """
        empty: bool = False
        if self.size() == self._ZERO:
            empty = True
        return empty
    
    def peek(self) -> Any:
        """Look and return at the top of the Stack. This method will also
        check if the file is empty by using the is_empty method before peeking.
        It will return a copy of the string of the top of the stack or a string
        stating that it couldn't peek succesfully.
        """
        file = open(self.filename, self._READ)
        # Make sure the queue is NOT empty
        if not self.is_empty():
            for line in file:
                # Just keep setting the top as the top_of_stack, the last
                # one will eventually be the top
                top_of_stack = line
        else:
            top_of_stack = self._EMPTY_STACK
        file.close()
        return top_of_stack

    def push(self, item: Any) -> None:
        """Push an item to the top of the stack. This uses the "append" option
        in file handling which automatically goes to the end of the file.
        """
        file = open(self.filename, self._APPEND)
        file.write(item + self._NEWLINE)
        file.close()

    def pop(self) -> Any:
        """Remove the item at the top of the stack."""
        # Same look as dequeue method, but the end of the file
        # Open original file and create temp
        file = open(self.filename, self._READ)
        temp_file = open(self._TEMP_FILE, self._WRITE)
        # Make a counter so we can compare to size
        index: int = 0
        # Store size for readability
        size_of_stack: int = self.size()
        if not self.is_empty():
            for line in file:
                # Increment before we write so we can check that its not top
                index += 1
                if index != size_of_stack:
                    temp_file.write(line)
                else:
                    # Grab the last line to return
                    popped = line
            file.close()
            temp_file.close()

            # Now open file as 'w' and temp as 'r'
            file = open(self.filename, self._WRITE)
            temp_file = open(self._TEMP_FILE, self._READ)
            for line in temp_file:
                file.write(line)
            file.close()
            temp_file.close()
        else:
            popped = self._EMPTY_STACK
        return popped