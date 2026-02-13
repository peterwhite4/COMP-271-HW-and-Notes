#Week 2

# We did this in class, so I thought it was important to try to include into my code as well
# I am going to declare 2 constants for each collumn of "underlying" so that we don't have "magic variables" wandering in my code, per the pact
# They are also _private because we are not allowed to have any public variables
_FIRST_NAME_LOCATION: int = 0
_LAST_NAME_LOCATION: int = 1


# Method 1 - add
def add(first_name: str,
    last_name:str,
    role: str,
    underlying: list[list[str]]) -> None:

    # Since we know that we are given a list with lists of strings inside, and that there is 3 columns (first_name, last_name, role) 
    # we can simply just add the new entries to the underlying list
    underlying += [[first_name, last_name, role]]


# This method is to make our code less repetitive. We will call this in our "unique_add" functions when needed
# fol = first or last name
def name_found(fol_name: str, 
               column: int, #CONSTANTS
               underlying: list[list[str]]):

    # We need a loop that can go through all of the entries of underlying
    i: int = 0 # Index for loop
    found: bool = False # Boolean variable to check if we found the first or last name
    while i < len(underlying) and not found:
        # This if statement checks each entry of underlying [i], and checks the the first or last name columns to see if it already exists
        # If it does, we set found to True and exit the loop
        if underlying[i][column] == fol_name:
            found = True
        i += 1
    
    return found

# Method 2 - add_unique_first_name
def add_unique_first_name(
    first_name: str,
    last_name:str,
    role: str,
    underlying: list[list[str]]) -> None:

    # Since it is a "unique first name" we need to check if the first name already exists in underlying
    # In order to do that we need a loop that can go through all of the entries of underlying
    # We are going to call the name_found method that we made
    # We put our first_name variable and _FIRST_NAME_LOCATION in for the fol_name and column
    # We make sure the first name isn't found in underlying
    if not name_found(first_name, _FIRST_NAME_LOCATION, underlying):
        # Then we call our previous add method
        add(first_name, last_name, role, underlying)
    

# Method 3 - add_unique_last_name
def add_unique_last_name(
    first_name: str,
    last_name:str,
    role: str,
    underlying: list[list[str]]) -> None:

    # With the difference of the constant and the last_name variable that are used,
    # This is really just the same as the "add_unique_first_name" method
    if not name_found(last_name, _LAST_NAME_LOCATION, underlying):
        add(first_name, last_name, role, underlying)
   

# Method 4 - remove_first_name
def remove_first_name(
    first_name: str,
    underlying: list[list[str]]) -> str|None:

    # This function is works in similar ways as the "add_unique_first_name" and "add_unique_last_name" methods,
    # in terms of looping through underlying and looking at what is inside of it
    # So we are going to use a similar loop

    # First we need to declare our variable we will return at the end, because of only one return statment
    deleted_name = None

    i: int = 0 # Index for loop
    found: bool = False # Boolean variable to check if we found the first name
    while i < len(underlying) and not found:
        # This if statement checks each entry of underlying [i], and checks the first name column [0] (or _FIRST_NAME_LOCATION) to see if it already exists
        # If it does, we set found to True, delete the name, and exit the loop
        if underlying[i][_FIRST_NAME_LOCATION] == first_name:
            found = True
            
            # Since we have found a first name matching the value of first_name, we can now remove it from underlying using pop (per directions)
            # We have to set a variable to store the deleted name, because we need to return it, but we can only return one value so we set it = to that variable
            # This will also overwrite our earlier deleted_name
            deleted_name = underlying.pop(i)

        # We need to keep the loop going only IF we dont find or delete an identical first name
        else:
            i += 1

    return deleted_name
    

# Method 5 - remove_all_first_name
def remove_all_first_name(
    first_name: str,
    underlying: list[list[str]]) -> list[str]|None:

    # This method is similar to the "remove_first_name" method, but instead of removing just one entry, we need to remove all entries with a matching first name to first_name
    # We are going to use a similar loop to "remove_first_name", but we need to make it keep going until the end of underlying

    # We are going to declare deleted_names as a list of strings that will hold all of the rows that are deleted in the loop. 
    # We will keep adding onto this list as we delete names and have it be our one return statement at the end
    deleted_names: list[str] = []

    i: int = 0 # Index for loop
    # This while loop isn't going to check for "found" because we do not care, we're going through all of the entries no matter what
    while i < len(underlying):
        
        if underlying[i][_FIRST_NAME_LOCATION] == first_name:
           
            # Since we have found a first name matching the value of first_name, we can now remove it from underlying using pop (per directions)
            # We have to set a variable to store the deleted name, because we need to return it, but we can only return one value so we set it = to that variable
            deleted_name = underlying.pop(i)
            # We need to keep deleted name in brackets to keep the form of lists inside of a list
            deleted_names += [deleted_name]
        
        # This else statement is important for our check through underlying. 
        # If we delete the first_name and row that we found, we don't need to index up because we just deleted the previous one - taking its place
        else: 
            i += 1

        # When the loop ends, we need to check if deleted_names is empty, because if it is we need to return None (per directions)
        if deleted_names == []:
            deleted_names = None

    return deleted_names
