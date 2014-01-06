# This file is a part of hexomega software.
# It defines and maintains the global data.


# For max flexibility, this file is designed to be read
# and write by other parts directly.
# Due to the limitation of Python, we need to use
# import HOData
# rather than
# from HOData import *
# So the other module must add "HOData." prefix
# if they want to use this file

# Store the current available ID
HOElemID = 1
HOBusID = 2 # 1 is reserved to Generator
HOLineID = 1

# Screen width and height, update in the main routine
ScrTotalW = 0
ScrTotalH = 0

# Define the boundary to the screen edge, update in the main routine
WSegWL = 0 # Large width
WSegWS = 0 # Small width
WSegW = 0 # Width used
WSegH = 0 # Height
WGeometry = "" # Window setting str

# Define the grid of the interface
WRowSegN = 25
WColumnSegN = 8

# The width of Entry
WWidth = 10

# file handlers
HOOpenHandler = None
HOSaveHandler = None
HOSaveDataHandler = None

# Saving flag, if there is any changes, set to 1
# if model saved, reset to 0
HOModified = 0

# Used by HModElem, stored the class instance being modified
HOModInst = None

# Used to register child window so they could be killed later
# Each time append a list [Tk(), name]
# New windows are add in the end so search should be from end to begin
HOWin = []

#### Set if the warning of voltage is ignored
#### Not available now~
HOVoltWarning = 1


# The network array, every class instance is stored here
HOBus = []
HOLine = []

# When network are saved in the two list below
# and they will be loaded when opened
HOBusSave = []
HOLineSave = []

# The storage instruction is listed as follows:

# class HOGen
# Store in HOBusSave[]
# [type, elemID, busID = 1, busVoltReal, voltageLevel, generatorVoltage]

# class HOLine
# Store in HOLineSave[]
# [type, elemID, lineID, z1, y1, length, end1, end2]

# class HOLineBuild
# Store in HOLineSave[]
# [type, elemID, lineID, material, area, radius, n, divR, length, \
# Dab, Dbc, Dac, end1, end2]

# class HOTrans
# Store in HOLineSave[]
# [type, elemID, lineID, Sn, Un, U2, Pk, Uk, P0, I0, end1, end2]

# class HOLoadPQ
# Store in HOBusSave[]
# [type, elemID, busID, S]

# class HOLoadPV
# Store in HOBusSave[]
# [type, elem, busID, P, V]



# A function to reset all these data
def HOReset():
    HOOpenHandler = None
    HOSaveHandler = None
    HOSaveDataHandler = None
    HOBus = []
    HOLine = []


