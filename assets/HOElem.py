# This file is a part of hexomega software.
# It defines the base element class in power system network.


import math
from HOAsserts import *


class HOElem():
    def __init__(self, elemID, elemType, elemName = ""):
        self.warning = [] # store error infomation
        
        self.ID = 0
        if isInt(elemID):
            self.ID = elemID
        else:
            self.warning.append("IDError")
        
        self.type = ""
        if elemType in elemTypeList:
            self.type = elemType
        else:
            self.warning.append("TypeError")

        self.name = ""
        if isStr(elemName):
            self.name = elemName
        else:
            self.warning.append("NameError")
        
        # The connection are defined as the index of the other array
        # For element in Bus array is the index of Line array
        # For element in Line array is the index of Bus array
        self.connect = []

    def getError(self):
        return self.warning

    def clearError(self):
        self.warning = []
        
    def getID(self):
        return self.ID

    def setID(self, newID):
        if isInt(newID):
            self.ID = newID
        else:
            self.warning.append("IDError")
        
    def getType(self):
        return self.type

    def getName(self):
        return self.name

    def setName(self, newName):
        if isStr(newName):
            self.name = newName
        else:
            self.warning.append("NameError")

    def getConnect(self):
        return self.connect

    def getConnectN(self):
        return len(self.connect)

    # discard
    def setConnect(self, elemID):
        if isInt(elemID):
            self.connect.append(elemID)
        else:
            self.warning.append("IDError")

    # reused as delConnectLine or delConnectBus
    def delConnect(self, elemID):
        if elemID in self.connect:
            self.connect.remove(elemID)
        else:
            self.warning.append("RemoveError")
    
        
