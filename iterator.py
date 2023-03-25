# an iterator for a collection provides one key behavior: it supports a special method named __next__ that
# returns the next element of the collection. 

class SequenceIterator:
    """"an iterator for any type of pythons's sequence type"""
    def __init__(self, sequence):
        self.sequence = sequence # keeping a reference to the underlying data
        self.k = -1 # will increment to 0 on first call to next
    
    def __next__(self):
        """Return the next element, or raise StopIterationError """
        self.k = self.k + 1
        if self.k < len(self.sequence):
            return (self.sequence[self.k])
        else:
            raise StopIteration
    
    def __iter__(self):
        return self
    
a = SequenceIterator([32,342])
a1 = a.__next__()
a2 = a.__next__()
# a3 = a.__next__()
print(a1,a2)