# This file is a part of hexomega software.
# It contains the functions of voltage reduction and matrix building.


class HOBuildMat():
    # From giving parameters build admittance matrix Y
    # Y should be an n dimension complex matrix
    def __init__(self):
        """Start with an empty Y matrix."""
        self.Y = [] # Build a empty matrix, may use different implement

    def addBus(self, newBusID):
        """Add a new bus to the Y matrix, update Y, dimension + 1."""
        # ID is from 1 to n, agree with the size of Y.
        # The VTheta bus always has the ID of 1.
        pass

    def addLine(self, lineID1, lineID2):
        """Add a new line to Y matrix, update y related to both i and j."""
        # The ID points to (index-1) position in Y matrix.
        # Only add line between exist buses.
        pass

    # Since if any element is changed the matrix will be redrawed,
    # the features such as remove or modify is not supported here.

    def getY():
        # return the matrix
        pass
    
