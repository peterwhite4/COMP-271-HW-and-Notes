#Class copied from HW directions, unchanged
class Character:
    """A class to represent a character in a show."""

    def __init__(self, first_name: str, last_name: str, role: str):
        """Initialize a Character object with the specified first name,
        last name, and role."""
        self.__first_name = first_name
        self.__last_name = last_name
        self.__role = role

    def __str__(self) -> str:
        """Returns a string representation of the Character object. Specifically,
        the string consists of the first letter of the first name, last name,
        and role concatenated together.
        """
        return (
            ("" if self.__first_name == "" else self.__first_name[0])
            + ("" if self.__last_name == "" else self.__last_name[0])
            + ("" if self.__role == "" else self.__role[0])
        )

    def __repr__(self) -> str:
        """Returns a string representation of the Character object for debugging"""
        return self.__str__()

    def get_first_name(self) -> str:
        """Accessor for the first name of the character."""
        return self.__first_name

    def get_last_name(self) -> str:
        """Accessor for the last name of the character."""
        return self.__last_name

    def get_role(self) -> str:
        """Accessor for the role of the character."""
        return self.__role

#Class copied from directions, added "add_unique" and "remove" functions
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
        # object's underlying list. The following two steps can be
        # done in one step, but for illustration purposes they are
        # shown separately here.
        new_character = Character(first_name, last_name, role)
        self.__underlying.append(new_character)

    def __contains_by(self, target: str, getter) -> bool:
        """Return True if any character's getter() equals target.
        Here's something wonderful about Python: we can pass functions
        as arguments to other functions. In this case, we can pass in
        any of the getter methods defined in the Character class
        (get_first_name, get_last_name, or get_role) and use that
        to compare against the target string. This allows us to
        avoid duplicating code for each of the three "contains" methods.

        This method is private (indicated by the leading double underscore)
        because it is only intended to be used internally by the other
        "contains" methods."""
        # Prepare to iterate through the underlying list
        i = 0
        # Assume we wont find what we are looking for
        found = False
        # Iterate through the list until we either find a match
        # or run out of items to check
        while i < len(self.__underlying) and not found:
            # Check if the current character's getter() matches target
            # Note that we call the getter function passed in as an argument
            # rather than trying to access it as an attribute of the Character
            # object. If we get a match, variable found becomes True and
            # the loop will exit.
            found = getter(self.__underlying[i]) == target
            # Move to the next character in the list
            i += 1
        # Done searching, return whether we found a match
        return found

    def contains_first_name(self, first_name: str) -> bool:
        """Return True if any character has the specified first name.
        This is a public method that uses the private __contains_by()
        method to perform the actual search."""
        return self.__contains_by(first_name, Character.get_first_name)

    def contains_last_name(self, last_name: str) -> bool:
        """Return True if any character has the specified last name.
        This is a public method that uses the private __contains_by()
        method to perform the actual search."""
        return self.__contains_by(last_name, Character.get_last_name)

    def contains_role(self, role: str) -> bool:
        """Return True if any character has the specified role.
        This is a public method that uses the private __contains_by()
        method to perform the actual search."""
        return self.__contains_by(role, Character.get_role)

    # Constant string template for the report header - used in report()
    # In compliance with the "no magic value" principle
    _REPORT_HEADER = 'There are {} characters in your data about "{}"'

    def report(self) -> str:
        """Generate a nicely formatted report of all characters in the show."""
        output = self._REPORT_HEADER.format(len(self.__underlying), self.__title)
        for character in self.__underlying:
            output += f"\n\t{character.get_first_name()} {character.get_last_name()} - {character.get_role()}"
        return output


    # Problem 1
    def add_unique(self, first_name: str, last_name: str, role: str) -> bool:
        """Adds a Character to the Cast object only if there is no other object with the same first name, last name, and role.
        Returns True if Character is added correctly, and False if a Character cannot be added because of duplicate."""
        
        # Create bool and index for loop
        i = 0
        found = False

        while i < len(self.__underlying) and not found:
            character = self.__underlying[i]

            # Make sure all 3 categories aren't duplicate
            # Set it = to found to make it true if they are all equal to the new list
            found = (character.get_first_name() == first_name and character.get_last_name() == last_name and character.get_role() == role)
            
            i += 1
        
        # Have to switch our "found" bool because of return statement requirements
        if found:
            found = False
        else:
            found = True
            # Add character to Cast using add_character
            self.add_character(first_name, last_name, role)
        
        # Only returns T/F
        return found

      
    # Problem 2
    def remove(self, first_name: str, last_name: str, role: str) -> Character | None:
        """Removes and returns the first Character object that matches the specified first name, last name, and role.
        If no such object exists, the function returns None."""

        i = 0
        found = False
        # Make sure its returning None and not a string of "None"
        removed_character = None

        while i < len(self.__underlying) and not found:
            character = self.__underlying[i]

            # Make sure all 3 categories aren't duplicate
            if (character.get_first_name() == first_name and character.get_last_name() == last_name and character.get_role() == role):
                # Use pop to delete the entry
                removed_character = self.__underlying.pop(i)
                # Set to true to end loop
                found = True

                # Index up only if NOT found
            else:
                i += 1

        # Returns the deleted entry or None
        return removed_character


# Problem 3
# I am on Episode 7 of Season 7 so please do not SPOIL anything for me if you have previously watched Game of Thrones!

a = Character("Daenerys", "Targaryen", "Mother of Dragons")
b = Character("Jon", "Snow", "King of the North")

"""
Comparison Discussion
I previously wrote this discussion about the contents of Game of Thrones. This consisted of what both Daenerys and Jon have accomplished
throughout the show, but after class on 2/6, we discussed that computers don't compare and think that way. To compare these two characters,
we have to look at where they are coming from: the class Character. This means that quantitative data has to be used to compare/contrast such things.
Since a regular program like the one we have here doesn't know that Daenerys freed many slaves or united many armies, we can't use that information.
The same goes with Jon Snow and what he has done during the show. To compare these two, we can only use what we are given as Characters of this class: strings.
Daenerys Targaryen is better than Jon Snow. This is simply because of the fact that I am comparing them based on the length of their strings.
Daenerys, consisting of 8 letters, compared to Jon's 3, means she is greater. Targaryen for Daenerys consists of 9 letters, while Snow for Jon's last name consists of only 4.
Daenerys' last name is also greater = better. Finally, the role. Daenerys' "Mother of Dragons" consists of 15 letters (17 counting the spaces),
Compared to Jon Snow's "King of the North," adding up to 14 (or 16) letters shows that Daenerys is also greater.
Although, when I previously wrote this comparison and came to the conclusion that Daenerys was better than Jon, I didn't use the same data.
We have to work with what is given to us and known information and compare in those ways. Leading to the conclusion that...
Daenarys Targaryen is better and greater than Jon Snow.

"""
