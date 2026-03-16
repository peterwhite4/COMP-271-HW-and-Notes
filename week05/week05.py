from abc import ABC, abstractmethod


class PantheonADT(ABC):
    """
    Pantheon ADT 

    Concept:
        A Pantheon stores a set of unique gods. Each god has:
            - a unique name (the key)
            - a domain (the value), e.g., "war", "wisdom", "harvest"

    ADT Rule (invariant):
        God names are unique. Domains do NOT need to be unique.
    """

    @abstractmethod
    def register(self, god_name: str, domain: str) -> bool:
        """
        Register a god into the pantheon.

        Parameters:
            god_name: unique identifier for the god (key)
            domain: the god's domain (value)

        Returns:
            True  if the god_name was not already present and was newly added.
            False if the god_name already existed (no changes made).

        Notes:
            - This operation does NOT overwrite existing entries.
            - Use change_domain(...) to update an existing god.
        """
        ...

    @abstractmethod
    def change_domain(self, god_name: str, new_domain: str) -> bool:
        """
        Change the domain of an already-registered god.

        Parameters:
            god_name: the god to update
            new_domain: the new domain to store

        Returns:
            True  if god_name exists and the update was performed.
            False if god_name does not exist (no changes made).
        """
        ...

    @abstractmethod
    def get_domain(self, god_name: str) -> str:
        """
        Retrieve the domain for a god.

        Parameters:
            god_name: the god to look up

        Returns:
            The domain (str) if the god exists; otherwise None.

        Important:
            - This method must NOT mutate the pantheon.
        """
        ...

    @abstractmethod
    def remove_god(self, god_name: str) -> bool:
        """
        Remove a god from the pantheon.

        Parameters:
            god_name: the god to remove

        Returns:
            True  if the god existed and was removed.
            False if the god was not found.
        """
        ...

    @abstractmethod
    def contains(self, god_name: str) -> bool:
        """
        Check whether a god is registered.

        Parameters:
            god_name: the god name to check

        Returns:
            True if present, otherwise False.
        """
        ...

    @abstractmethod
    def count(self) -> int:
        """
        Return the number of gods currently registered in the pantheon.
        """
        ...

    @abstractmethod
    def list_all(self):
        """
        Return a snapshot list of all registered gods and their domains.

        Returns:
            A NEW list of pairs, where each pair is [god_name, domain].

        Requirements:
            - Must return a copy (caller mutations must not affect internals).
            - Ordering is up to the implementation unless otherwise specified
              by a derived class / assignment variant.
        """


class Deities(PantheonADT):
    
    # 1: Make init method
    def __init__(self):
        """Creates a Deites object. This is an empty list that will later store 
        lists of God's Names and their domains.
        """
        self.__underlying = []

    # Constants for God and Domain's spot inside of underlying
    __GOD: int = 0
    __DOMAIN: int = 1

    # 2: Make String method
    def __str__(self) -> str:
        """String method to return the Gods and their corresponding domains.
        If it is empty, the string will return that as well.
        """
        # Create a string that we can return
        string_return: str = ""
        # Create a loop to repeat all the names in the list or if its empty
        i = 0
        if len(self.__underlying) != 0:
            while i < len(self.__underlying):
                string_return += (
                    "God: " + self.__underlying[i][self.__GOD] + 
                    "| Domain: " + self.__underlying[i][self.__DOMAIN] + "\n"
                )
                i += 1
        else:
            string_return = "The Pantheon is empty."
        return string_return
    
    # 10: REFACTORING, Making an index_of method to cut down loops in different methods
    def index_of(self, god_name) -> int:
        """"Making an index_of method to make looping in other methods
        simpler and cleaner. This method will loop through the underlying
        list and return an integer. If god_name is found, it will return 1,
        if it is not found, it will return -1.
        """
        # Assume object isn't in list
        index: int = -1
        i: int = 0
        while i < len(self.__underlying) and index < 0:
            # Make more readable by asigning to a local variable
            god = self.__underlying[i][self.__GOD]
            # See if the god at position i is equal to the god_name given
            if god == god_name:
                # Get the index of where its at
                index = i
            i += 1
        return index
    
    # 3: Make contains method, seems easiest and will be used later on
    def contains(self, god_name: str) -> bool:
        """Implements the contains method as specified in the PantheonADT class.
        This method will use our index_of method to search through underlying
        and return True if found, false if not."""
        found: bool = False
        # Use index_of, return true if not equal to -1
        if self.index_of(god_name) > -1:
            found = True
        return found

    # 4: Make count method
    def count(self) -> int:
        """Implements the count method as specified by the PantheonADT class.
        It will return the number of gods currently registered in the Pantheon."""
        # With the pantheon having to store a God with its domain, there should be
        # no "None" for God in our list. Just return the length of our underlying.
        return len(self.__underlying)

    # 5: Make register method
    def register(self, god_name: str, domain: str) -> bool:
        """Implements the register method as specificed in the PantheonADT class
        The method will use the contains method to search through the underlying 
        list of God's names and domains. This method will return true if the 
        god_name was not already present and was succesfully added. It will return 
        False if the god_name already exists and no changes were made. This will 
        not overwrite any existing entries and will use the change_domain method.
        """
        # Create a boolean to return
        registered: bool = False
        # Call contains method
        if self.contains(god_name):
            registered = False
        # If god_name is not found, append it to underlying
        else:
            registered = True
            self.__underlying.append([god_name, domain])
        return registered

    # 6: Make get_domain method
    def get_domain(self, god_name: str) -> str:
        """Implements the get_domain method as specified in the PantheonADT class.
        This method will retrieve the domain for a god using index_of method.
        It will return the domain as a string.
        """
        # Create domain string for one return statement
        domain: str = None
        # Pull index from index_of method
        index = self.index_of(god_name)
        if index > -1:
            domain = self.__underlying[index][self.__DOMAIN]
        # Don't need an else statement, domain will remain none
        return domain

    # 7: Make change_domain method
    def change_domain(self, god_name: str, new_domain: str) -> bool:
        """Implements the change_domain method as specified in the PantheonADT class.
        This method will change the domain of an already-registered God.
        This method will return True if the god_name exists and change was performed,
        and False if the god_name does not exist and no changes are made.
        This method will search through the list with the index_of method.
        """
        # Create bool to return
        found: bool = False
        # Pull index from index_of
        index = self.index_of(god_name)
        if index > -1:
            found = True
            # Set new_domain
            self.__underlying[index][self.__DOMAIN] = new_domain
        return found

    # 8: Make list_all method
    def list_all(self):
        """Implements the list_all domain method as specified in the PantheonADT class.
        This method will return a snapshot of all registered gods and their domains
        as a NEW list of pairs where each pair is [god_name, domain].
        """
        # Create a new empty list to return
        snapshot = []
        # Create a loop to go through underlying
        i = 0
        while i < len(self.__underlying):
            # Make it more readable for when added to snapshot
            god = self.__underlying[i][self.__GOD]
            domain = self.__underlying[i][self.__DOMAIN]
            # Append god and domain to snapshot
            snapshot.append([god, domain])
            # Go to next entry
            i += 1
        return snapshot
    
    # 9: Make remove_god method
    def remove_god(self, god_name: str) -> bool:
        """Implements the remove_god method as specified in the PantheonADT class.
        This method will search for the god given in the underlying list.
        If the god exists, this method will remove it and return
        True. If not, it will not do anything and return False.
        """
        # Create one bool to return based off of what happens
        removed: bool = False
        # Pull index from index_of
        index = self.index_of(god_name)
        # If index returns as found or > -1
        if index > -1:
            removed = True
            # Pop out this entry
            self.__underlying.pop(index)
        return removed
