# 2/27 Notes

# Object test can store up to N items (def N = 4)

# When object is full -> Double its size, ad move content to enlarged version

# count -> how many items
# init -> empty

class SpringBreak:

    __DEFAULT_CAPACITY = 4

    def __init__(self, capacity =__DEFAULT_CAPACITY):
        # Make storage have four spaces
        self.__storage = [None] * capacity
        self.__capacity = capacity
        self.__current_count = 0

    def count(self):
        return self.__current_count
    
    def add_item(self, item):
        """Bad Code
        # Check and see if there is room
        if self.__current_count < self.__capacity:
            self.__storage[self.__current_count] = item
            self.__current_count += 1
        else: 
            # Create a larger object
            larger_object = [None] * (2*len(self.__storage))
            # Move the contents of __storage to larger object
            for i in range(self.__current_count):
                larger_object[i] = self.__storage[i]
            self.__storage = larger_object
            self.add_item(item)
        """
        # Good Code
        if self.__current_count == self.__capacity:
            # No room, lets make some more
            larger_object = [None] * (2 * self.__capacity)
            # Copy existing contents to larger object
            for i in range(self.__current_count):
                larger_object[i] = self.__storage[i]
        # By the time we are here, we are 100% certain
        # there is room for a new item
        self.__storage[self.__current_count] = item
        self.__current_count += 1