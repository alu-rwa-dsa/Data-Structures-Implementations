"""
Build an a list (associative list) which has the following methods
    - add(key,value)
    - remove(key)
    - modify(key,newvalue)
    - lookup(key)
"""


class AssociativeList():
    def __init__(self):
        self.d = {}

    def add(self, key, val):
        """
        add function adds the given key and value to the dictionary
        :param key: given key
        :param val: given value for the key
        """
        self.d[key] = val

    def remove(self, key):
        """
        remove function takes in a key and removes it from the dictionary
        :param key: given key
        """
        if self.d.get(key):
            del self.d[key]
        else:
            raise KeyError

    def modify(self, key, newValue):
        """
        modeify function updates the value of an existing key with a new value
        :param key: given key
        :param newValue: new value given to the key
        """
        self.d[key] = newValue

    def lookUp(self, key):
        """
        LookUp function takes in a key and returns its value if the key is in the dictionary and None if the key
        doesn't exist
        :param key: given key
        :return: the key's value if the key exist in the dictionary, None otherwise
        """
        # use the get method to check if the key exist or not
        if self.d.get(key):
            return self.d[key]
        return None


if __name__ == "__main__":
    AssociativeList()
