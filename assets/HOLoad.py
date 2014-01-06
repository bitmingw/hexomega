# This file is a part of hexomega software.
# It defines the class of generator


from HOElem import *
import HOData


class HOLoadPQ(HOElem):

    # Set a new PQ bus
    # Use complex power as an argument
    # S indict the power flow INTO the bus
    def __init__(self, elemID, busID, S):
        HOElem.__init__(self, elemID, "PQBus")

        self.busID = 0
        if isInt(busID) and busID != 1:
            self.busID = busID
        else:
            self.warning.append("BusIDError")

        self.S = complex(0+0j) 
        if isComplex(S):
            self.S = S
        else:
            self.warning.append("PowerError")

        self.U = complex(0+0j) # voltage of the bus
        self.VL = 0 # before reduction, used to calculate k
        self.y0 = complex(0+0j)


    def getBusID(self):
        return self.busID

    def setBusID(self, newID):
        if isInt(newID) and newID != 1:
            self.busID = newID
        else:
            self.warning.append("BusIDError")

    def getCPower(self):
        # return complex power
        return self.S

    def setCPower(self, newS):
        # The power flow INTO the bus
        if isComplex(newS):
            self.S = newS
        else:
            self.warning.append("PowerError")
    
    def getVoltage(self):
        # return complex voltage
        return self.U

    def setVoltage(self, newVolt):
        # Get this value after the calculation
        if isComplex(newVolt):
            self.U = newVolt
        else:
            self.warning.append("BusVoltageError")
        
    def getVoltageLevel(self):
        return self.VL

    def setVoltageLevelAuto(self):
        # Get this by check all connection to the bus
        # If they are not coherent report error
        isCoherent = True
        findVoltLevel = 0
        connectList = self.getConnect()
        for conn in connectList:
            for elem in HOData.HOLine:
                if elem.getLineID() == conn:
 
                    if findVoltLevel == 0: # init
                        findVoltLevel = elem.getVoltageLevel()
                        findVoltLevel = roundStdVolt(findVoltLevel)
                    else:
                        if isInSameLevel(findVoltLevel, \
                                         elem.getVoltageLevel()) == False:
                            isCoherent = False

        if isCoherent and findVoltLevel:
            self.VL = findVoltLevel
        else:
            self.warning.append("VoltageLevelError")

    def gety0(self):
        return self.y0

    def updatey0(self):
        # Self admittance to the ground, calculated by adding
        # half of admittance of all connected lines
        # or full admittance of transformer if connected to 1st side
        # Retrieve self.connect
        connectList = self.getConnect()
        for conn in connectList:
            for elem in HOData.HOLine:
                if elem.getLineID() == conn:
                    if elem.getType() == "Line":
                        self.y0 += elem.getY() / 2
                    elif elem.getType() == "Transformer" \
                         and elem.getEnd1() == conn:
                        self.y0 += elem.getY()

    def doReduction(self, givenLevel):
        # do voltage reduction for U (is enough)
        # the caller will manually update y0
        if isInt(givenLevel) and isInVoltStdList(givenLevel) and self.VL:
            self.U = self.U * givenLevel / self.VL
        else:
            self.warning.append("ReductionError")

    def reDoReduction(self, givenLevel):
        # Redo reduction for U (is enough)
        if isInt(givenLevel) and isInVoltStdList(givenLevel) and self.VL:
            self.U = self.U * self.VL / givenLevel
        else:
            self.warning.append("ReductionError")


class HOLoadPV(HOElem):

    # Set a new PV bus
    # Use active power as an argument
    # S indict the power flow INTO the node
    def __init__(self, elemID, busID, P, V):
        HOElem.__init__(self, elemID, "PVBus")

        self.busID = 0;
        if isInt(busID) and (busID != 1):
            self.busID = busID
        else:
            self.warning.append("BusIDError")

        self.S = complex(0+0j) 
        if isFloat(P):
            self.S = complex(P, 0)
        else:
            self.warning.append("PowerError")

        self.U = complex(0+0j) # voltage of the bus
        if isInt(V) and isInVoltStdList(V):
            self.U = complex(V, 0)
        else:
            self.warning.append("BusVoltageError")
        
        self.VL = 0 # before reduction, used to calculate k
        self.y0 = complex(0+0j)

        def getBusID(self):
            return self.busID

        def setBusID(self, newID):
            if isInt(newID) and newID != 1:
                self.busID = newID
            else:
                self.warning.append("BusIDError")

        def getCPower(self):
            # return complex power
            return self.S

        def setCPower(self, newS):
            if isComplex(newS) and newS.imag == 0:
                self.S = newS
            else:
                self.warning.append("PowerError")

        def getVoltage(self):
            # return complex voltage
            return self.U

        def setVoltage(self, newVoltage):
            # new voltage is complex U rather than real V
            if isComplex(newVoltage) and isInVoltStdList(abs(newVoltage)):
                self.U = newVoltage
            else:
                self.warning.append("BusVoltageError")
        
        def getVoltageLevel(self):
            return self.VL

        def setVoltageLevelAuto(self):
            # round to nearest voltage from U.real
            self.VL = int(self.U.real)

        def gety0(self):
            return self.y0

        def updatey0(self):
            # Self admittance to the ground, calculated by adding
            # half of admittance of all connected lines
            # or full admittance of transformer if connected to 1st side
            # Retrieve self.connect
            connectList = self.getConnect()
            for conn in connectList:
                for elem in HOData.HOLine:
                    if elem.getLineID() == conn:
                        if elem.getType() == "Line":
                            self.y0 += elem.getY() / 2
                        elif elem.getType() == "Transformer" \
                             and elem.getEnd1() == conn:
                            self.y0 += elem.getY()
        
        def doReduction(self, givenLevel):
            # do voltage reduction for U (is enough)
            # the caller will manually update y0
            if isInt(givenLevel) and self.VL:
                self.U = self.U * (givenLevel / self.VL)
            else:
                self.warning.append("ReductionError")

        def reDoReduction(self, givenLevel):
            # Redo reduction for U (is enough)
            if isInt(givenLevel and self.VL):
                self.U = self.U * (self.VL / givenLevel)
            else:
                self.warning.append("ReductionError")
