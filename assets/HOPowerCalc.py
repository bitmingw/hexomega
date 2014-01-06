# This file is a part of hexomega software.
# It contains the functions of power system calculation.


from numpy import matrix
from numpy import linalg

class HOPowerCalc():
    def __init__(self, Y, YType, vLev, lineConnect, eps):
        """The init do two kinds of things.
    First it split the Y matrix to get G and B matrix.
    Then it init the vector x."""
        # G and B are real, x is real vector of (2n-2) length
        # To init x, set all e (real) to reduction voltage
        # and f (imag) to 0
        
        # NOTICE that bus 1 is the generator
        # and should be REMOVED from the calculation
        
        self.G = Y.real
        self.B = Y.imag
        self.X = (Y.I).imag
        self.YType = []
        
        self.deltaX = [] # init to zero but have the according size
        self.deltaF = [] # init to zero but ~
 
        self.invJ = [] # ~
        self.lineConnect = lineConnect
        self.eps = eps
        self.complete = 0
        pass

    def getYType(self):
        """Return the n dimension type vector."""

    def getJ(self):
        """Build the (2n-2) dimension Jacobi matrix."""
        
        self.J = []
        pass

    def getdeltaF(self):
        """Build (2n-2) length vector of deltaF."""
        # deltaF has deltaP, deltaQ, deltaU2 etc.
        self.deltaF = []
        pass

    def getInverseJ(self):
        """Determine the inverse of Jacobi matrix."""
        self.invJ = []
        pass

    def getdeltaX(self):
        """From the inverse of J and deltaF, calculate deltaX."""
        # deltaX has delta_e, delta_f etc.
        self.deltaX = []
        pass

    def updateX(self):
        """Add deltaX to X."""
        pass

    def isLoopAgain(self):
        """From the value of deltaF and eps, determine if to run another time."""
        # First check self.complete
        # If the condition is approved set self.complete
        pass

    def getVoltages(self):
        """If complete, return (n-1) voltages as complex vector
    in ascending ID."""
        pass

    def getPowers(self):
        """If complete, return (n-1) powers as complex vector
    in ascending ID, and a complex vector of power loss in the order
    given by lineConnect."""
        # lineConnect is a m*2 matrix give the first side and
        # second side of a line or transformer.
        pass

    def getGenPower(self):
        """If complete, return the power of generator."""
        pass


# Test data    
ty = matrix([[4.2+8.93j,5.90-1.23j],[9.78-9.3j,8.23+2.00j]])
test = HOPowerCalc(ty,220,0,0)

print test.G
print test.B
print test.X
