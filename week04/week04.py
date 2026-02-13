class Person:
    """A super class that lends characteristics to Actors and Characters"""

    def __init__(self, first_name: str, last_name: str):
        """Instantiate a Person object with the given first and last names."""
        self.__first_name = first_name
        self.__last_name = last_name

    # Plain accessors
    def get_first_name(self) -> str:
        return self.__first_name

    def get_last_name(self) -> str:
        return self.__last_name

    # String representation and its constants
    __FNU = "First Name Unknown"
    __LNU = "Last Name Unknown"

    def __str__(self) -> str:
        """A string representation suitable for user-facing printing"""
        first = self.__FNU if self.__first_name == "" else self.__first_name
        last = self.__LNU if self.__last_name == "" else self.__last_name
        return f"{first} {last}"

    def __repr__(self) -> str:
        """A string representation suitable for developer-facing printing."""
        return f"{self.__class__.__name__}: {self}"


class Actor(Person):
    """Actor objects are just plain Persons -- the pass statement below
    signals that we don't need anything more than what the superclass Person
    already provides
    """

    pass


class Character(Person):
    """Character objects extend the superclass Person by adding one more
    attribute: a description of the character's role.
    """

    def __init__(self, first_name: str, last_name: str, role: str):
        # First instantiate a Person object by invoking the __init__
        # method of the superclass (Person)
        super().__init__(first_name, last_name)
        # Τhen initialize the role field for the δerived object (Character)
        self.__role = role

    # Plain accessor for the additional field
    def get_role(self) -> str:
        return self.__role

    # Constant for local __str__
    __ROLE_UNKNOWN = "Role Unknown"

    def __str__(self) -> str:
        """Local implementation of the string method to include
        the Character's role in the output. The method uses the
        string function of the superclass object and concatenates
        a string with the role information."""
        role = self.__ROLE_UNKNOWN if self.__role == "" else self.__role
        return super().__str__() + f" {role}"


class Cast:
    """A class to represent the cast of a show, consisting of multiple
    Character objects."""

    def __init__(self, title: str):
        # The title of the show being represented
        self.__title = title
        # A list of Character objects
        self.__underlying = []

    def __len__(self) -> int:
        """Return the number of characters in the show. This allows
        the use of len() on Cast objects."""
        return len(self.__underlying)

    def __bool__(self) -> bool:
        """Return True if there is at least one character in the
        show, False otherwise. This allows the use of bool() on
        Cast objects."""
        return len(self.__underlying) > 0

    def add_character(self, first_name: str, last_name: str, role: str) -> None:
        """Add a new character to the show."""
        # First create a new Character object, then append it to the
        # object's underlying list.
        new_character = Character(first_name, last_name, role)
        # Part 1: Update add_character
        # I have changed what is appended because of no information
        # about the corresponding character.
        self.__underlying.append([None, new_character])

    # Making two new methods to be able to call into my assign_to_character 
    # to make it more readable and allow for new index_of methods to work
    def actor_match(self, actor, first_name, last_name) -> bool:
        """Improves class 'Cast' by allowing to check and see if the header given
        by the user matches to an Actor in the class. First, it checks and makes sure
        that something exists in the Actor index, then it matches first name and last
        name with the header. If ONE instance does not match, it will return false.
        If not, it returns True verifying the Actor matches the header. This method 
        will also be used in index_of to allow for our add_unqiue methods to work.
        """
        # Bool to return
        matching_actor = False
        # Make sure something exists in the actor slot, then make sure header matches
        if (actor != None and 
            actor.get_first_name() == first_name and 
            actor.get_last_name() == last_name):
            matching_actor = True
        # Return a bool to then call later in assign_to_character
        return matching_actor
    
    def character_match(self, character, first_name, last_name, role) -> bool:
        """Improves class 'Cast' by allowing to check and see if the header given
        by the user matches to an Character in the class. First, it checks and makes 
        sure that something exists in the Character index, then it matches first name, 
        last name, and role of the Character with the header. If ONE instance does not 
        match, it will return false. If not, it returns True verifying the Character
        matches the header. This method will also be used in index_of to allow for 
        our add_unqiue methods to work.
        """
        # Bool to return
        matching_character = False
        # Same thing as actor_match, but add in role to the check
        if (character != None and
            character.get_first_name() == first_name and
            character.get_last_name() == last_name and
            character.get_role() == role):
            matching_character = True
        return matching_character
    
    # Defining locations for the actor and character pairs inside of underlying
    # They are private CONSTANTS so we have no magics in our code
    _ACTOR_CONSTANT = 0
    _CHARACTER_CONSTANT = 1

    # We HAVE to change index_of method or else or add_unique methods won't work
    # Did so by making an index_of for characters and actors
    def index_of_character(self, first_name: str, last_name: str, role: str) -> int:
        """Returns the index position of a specified character object. If
        the object is not found, the method returns -1."""
        # Assume the object is not in the underlying list
        index: int = -1
        # Prepare to traverse the list
        i: int = 0
        # Loop ends as soon as we find a match, by updating variable
        # index to the position of the match, or when we search the
        # entire list with no luck.
        while i < len(self.__underlying) and index < 0:
            # Instead of having multiple references to the underlying list
            # in the if statement below, let's assign the current item
            # from the list to a local variable.
            pair = self.__underlying[i]
            # We now have [Actor, Character] so we need to make local variables
            # for character to make it easier to read
            character = pair[self._CHARACTER_CONSTANT]
            if self.character_match(character, first_name,
                                    last_name, role):
                # Match found at i in the list
                # Save position to the return variable
                # This will end the loop
                index = i
            # Prepare to consider the next element in the underlying list
            i += 1
        # Done
        return index
    
    def index_of_actor(self, first_name: str, last_name: str) -> int:
        """Returns the index position of a specified actor object. If
        the object is not found, the method returns -1."""
        # Assume the object is not in the underlying list
        index: int = -1
        # Prepare to traverse the list
        i: int = 0
        # Loop ends as soon as we find a match, by updating variable
        # index to the position of the match, or when we search the
        # entire list with no luck.
        while i < len(self.__underlying) and index < 0:
            # Instead of having multiple references to the underlying list
            # in the if statement below, let's assign the current item
            # from the list to a local variable.
            pair = self.__underlying[i]
            # We now have [Actor, Character] so we need to make local variables
            # for actor to make it easier to read
            actor = pair[self._ACTOR_CONSTANT]
            if self.actor_match(actor, first_name, last_name):
                # Match found at i in the list
                # Save position to the return variable
                # This will end the loop
                index = i
            # Prepare to consider the next element in the underlying list
            i += 1
        # Done
        return index

    # Part 3: Update add_unique method
    def add_unique_character(self, 
                             first_name: str, last_name: str, role: str) -> bool:
        """Improves class `Cast` by allowing to add a `Character` to the `Cast`
        object only if there is no other object with the same first name,
        last name, and role description. The method returns `True` if the addition
        was succesful and `False` otherwise.
        """
        found: bool = self.index_of_character(first_name, last_name, role) > -1
        unique = not found  # superfluous but helps with readability
        if unique:
            # No record found, so we can add it here.
            # This logic stays the same because all we needed to do was change the
            # add_character method which we call now
            self.add_character(first_name, last_name, role)
        return unique
    
    # Part 2: add_actor method
    def add_actor(self, first_name: str, last_name: str) -> None:
        """Improves class 'Cast' by allowing to add only an 'Actor' when we do not
        have information about the corresponding 'Character'.
        """
        # Copy add_character, but just make it actor
        # Also make sure the None is after the Actor for the Character slot
        new_actor = Actor(first_name, last_name)
        self.__underlying.append([new_actor, None])

    # Part 4: add_unique_actor method
    def add_unique_actor (self, first_name: str, last_name: str) -> bool:
        """Improves class 'Cast' by allowing to add an 'Actor' to the 'Cast'
        object only if there is no other object with the same first name and last 
        name. The method returns 'True' if succesful and 'False' if not.
        """
        # This method is basically the same as add_unique_character, but
        # it does not use the 'role' string and calls add_actor instead of character
        found: bool = self.index_of_actor(first_name, last_name) > -1
        unique = not found  # superfluous but helps with readability
        if unique:
            # No record found, so we can add it here.
            self.add_actor(first_name, last_name)
        return unique
    
    # Part 5: assign_to_character method
    def assign_to_character(self, character_first_name, 
                            character_last_name, character_role,
                            actor_first_name, actor_last_name) -> None:
        """Improves 'Cast'. This method will loop through the underlying list with
        the header. If a pair with matching Actor and Character information 
        already exists there will be no change. If partial entry of only Actors 
        or only Characters exist, they will be merged together under the Actor index. 
        This method will return a result which will be None, and will also make sure 
        there are no remaining entries in the underlying list that contain None 
        in them.
        """
        # Create indexes to track what we see when we search in our loop
        # -1 means we didn't find anything in these indices
        actor_index: int = -1
        character_index: int = -1
        # Also create a bool if we found an actor and character that match header
        found_pair: bool = False
        # Index for our loop to go through the underlying list
        i: int = 0
        # Loop to search through list
        while i < len(self.__underlying):
            # Assign current pairs in underlying. Easier to read
            pair = self.__underlying[i]
            # Assign actor and character to where they will be in the pairs
            actor = pair[self._ACTOR_CONSTANT]
            character = pair[self._CHARACTER_CONSTANT]

            # If for both actor and character already paired
            if (self.actor_match(actor, actor_first_name, actor_last_name) and 
                self.character_match(character, character_first_name,
                                     character_last_name, character_role)):
                # Mark we found a matching pair
                found_pair = True

            # If for empty actor, but matching character
            elif (actor == None and 
                self.character_match(
                    character, character_first_name,
                    character_last_name, character_role)):
                # Mark location of the lone character
                character_index = i

            # If for empty character, but matching actor
            elif (character == None and
                  self.actor_match(
                      actor, actor_first_name, actor_last_name)):
                #Mark location of lone actor
                actor_index = i
            # Index through loop
            i += 1

        # Now we make a way to edit entries and clean the underlying list

        # Make objects that will make a new pair to the list if not found
        # later in our method
        new_character = Character(character_first_name, 
                                  character_last_name, character_role)
        new_actor = Actor(actor_first_name, actor_last_name)

        # First case, both are found
        if found_pair == True:
            # Nothing happens, we skip and move on
            # This is the one return statement in the method
            return
        
        # Second case, both are partial (Actor or Character)
        elif actor_index > -1 and character_index > -1:
            # Get objects of actor who is alone and character who is alone so we can merge
            actor_in_pair = self.__underlying[actor_index][self._ACTOR_CONSTANT]
            character_in_pair = self.__underlying[character_index][self._CHARACTER_CONSTANT]
            # Combine partial records of actor and character
            # using the index found for actor
            self.__underlying[actor_index] = [actor_in_pair, character_in_pair]
            # Delete the original character index
            self.__underlying.pop(character_index)
            
        # Only Actor exists
        elif actor_index > -1 and character_index == -1:
            # Name the actor we have that is in our underlying alone as "old"
            old_actor = self.__underlying[actor_index][self._ACTOR_CONSTANT]
            # Put the old actor and new character together at actor index
            self.__underlying[actor_index] = [old_actor, new_character]
          
        # Only Character exists 
        # Same as elif above, but now with old character and new actor
        elif actor_index == -1 and character_index > -1:
            # Name the character that is in our underlying list alone
            old_character = self.__underlying[character_index][self._CHARACTER_CONSTANT]
            # Put the old actor and new character together at character index
            self.__underlying[character_index] = [new_actor, old_character]
        
        # Neither exist
        else:
            # Create a totally new entry to underlying list
            self.__underlying.append([new_actor, new_character])