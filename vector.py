


class Vector:
    """ Represent a multi dimensional space """
    def __init__(self, d):
        """"Create a d dimensonal vector of zeros"""
        self._coords = [0]*d
    def __len__(self):
        return len(self._coords)
    def __getitem__(self,j):
        """ Return jth coordinate of the vector."""
        return self._coords[j]
    def __setitem__(self, j,val):
        """set the jth coordinate of the vector to the given val"""
        self._coords[j] == val
    def __add__(self, other):
        if len(self)!=len(other):
            raise ValueError("two vectors should have the same length")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    
    def __eq__(self, other):
        return self._coords == other._coords
    def __ne__(self,other):
        return not self==other
    def __str__(self):
        return f"< {self._coords[0:]}>"    
    
