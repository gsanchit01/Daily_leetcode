class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.data = iterator.v
        self.index = -1
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.data[self.index+1]

    def next(self):
        """
        :rtype: int
        """
        self.index += 1
        return self.data[self.index]

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.index + 1 < len(self.data) else False