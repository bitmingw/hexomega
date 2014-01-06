# This file is a part of hexomega software.
# It contains some useful function to check I/O arguments.


from numpy import matrix
from numpy import linalg


def isStr(s):
    if type(s) == type(""):
        return True
    return False


def isInt(num):
    if type(num) == type(2):
        return True
    return False


def isFloat(num):
    if type(num) == type(2.2):
        return True
    return False


def isComplex(num):
    if type(num) == type(2+2j):
        return True
    return False


def isInRange(num, low, high):
    if num >= low and num <= high:
        return True
    return False


def isLength(length, l):
    if  len(l) == length:
        return True
    return False


#Check if matrix m has r rows and c columns, return True or False.
def isSizeM(m, r, c):
    if m.shape[0] == r and m.shape[1] == c:
        return True
    return False
    

#Check if matrix m is a square matrix, return True or False.
def isSquareM(m):
    if m.shape[0] == m.shape[1]:
        return True
    return False


#Check if matrix m has determinent != 0, return True or False.
def isInvM(m):
    if isSquareM(m) and linalg.det(m) != 0:
        return True
    return False


def realM(m):
    """Fetch the real part of Matrix"""
    realPart = zeros(shape = (m.shape[0],m.shape[1]))
    for i in range(0, m.shape[0]):
        for j in range(0, m.shape[1]):
            realPart[i,j] = m[i,j].real
    return realPart


def imagM(m):
    """Fetch the imag part of Matrix"""
    imagPart = zeros(shape = (m.shape[0],m.shape[1]))
    for i in range(0, m.shape[0]):
        for j in range(0, m.shape[1]):
            imagPart[i,j] = m[i,j].imag
    return imagPart


def getEveryEntryInvM(m):
    EntryInv = zeros(shape = (m.shape[0],m.shape[1]), dtype=complex)
    for i in range(0, m.shape[0]):
        for j in range(0, m.shape[1]):
            EntryInv[i][j] = m[i,j].conjugate()/pow(abs(m[i,j]),2)
            #Mathematical Expression of Inv
    return EntryInv

    
def rowToColumn(a):
    """Transform an ARRAY to 1-D column vector"""
    column = zeros(shape = (len(a),1), dtype=complex)
    for i in range(0, len(a)):
        column[i,0] = a[i]
    return column


# Voltage standard
voltStdList = [3, 6, 10, 35, 110, 220, 330, 500]
voltGenList = [3.15, 6.3, 10.5, "default"]
voltTransList = [3, 3.15, 3.3, 6, 6.3, 6.6, 10, 10.5, 11, 35, 38.5,\
                 110, 121, 220, 242, 330, 345, 363, 500, 525, 550]


def isInVoltStdList(volt):
    for i in voltStdList:
        if volt >= i * 0.99 and volt <= i * 1.01:
            return True
    return False


def isInVoltGenList(volt):
    if volt == 'default':
        return True
    for i in voltGenList:
        if volt >= i * 0.99 and volt <= i * 1.01: # avoid float accurate problem
            return True
    return False


def isInVoltTransList(volt):
    for i in voltTransList:
        if volt >= i * 0.99 and volt <= i * 1.01:
            return True
    return False


def isInSameLevel(voltBase, volt2):
    if volt2 < voltBase * 0.88 or volt2 > voltBase * 1.12:
        return False
    return True


def roundStdVolt(volt):
    if volt > 0.88*3 and volt < 1.12*3:
        return 3
    elif volt > 0.88*6 and volt < 1.12*6:
        return 6
    elif volt > 0.88*10 and volt < 1.12*10:
        return 10
    elif volt > 0.88*35 and volt < 1.12*35:
        return 35
    elif volt > 0.88*110 and volt < 1.12*110:
        return 110
    elif volt > 0.88*220 and volt < 1.12*220:
        return 220
    elif volt > 0.88*330 and volt > 1.12*330:
        return 330
    elif volt > 0.88*500 and volt < 1.12*500:
        return 500
    else:
        return False


def approxSquare(base, square):
    # Set the accuracy to .95
    if base**2 < square * 0.95 or base**2 > square * 1.05:
        return False
    return True


# Types of elements
elemTypeList = ["Generic", "VThetaBus", "PQBus", "PVBus", \
                "Line", "RawLine", "Transformer"]


# Types of errors
baseErrorList = ["IDError", "TypeError", "NameError", "RemoveError"]

genErrorList = ["BusVoltageError", "VoltageLevelError", \
                "GeneratorVoltageError", "PowerError"]

PQErrorList = ["BusIDError", "PowerError", "BusVoltageError", \
               "VoltageLevelError", "ReductionError"]

PVErrorList = ["BusIDError", "PowerError", "BusVoltageError", \
               "ReductionError"]

LineErrorList = ["LineIDError", "ParameterError", "LengthError", \
                 "VoltageLevelError", "ConnectError", "ReductionError"]

LineBuildErrorList = ["LineIDError", "MaterialError", "AreaError", \
                      "LineDivError","ParameterError", "3LineError", \
                      "LengthError", "VoltageLevelError","ConnectError", \
                      "ReductionError"]

TransErrorList = ["LineIDError", "ParameterError", "ConnectError"]

