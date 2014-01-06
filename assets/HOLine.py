# This file is a part of hexomega software.
# It defines two classes of transmission line.
# HOLine is constructed by directly giving the r1, x1, g1, b1, etc.
# HOLineBuild is constructed by giving real line parameters.


from HOElem import *
import HOData

class HOLine(HOElem):

    # Set a new line
    # z1 = r1 + jx1, y1 = g1 + jb1
    # end1 and end2 are two ports of the line
    def __init__(self, elemID, lineID, z1, y1, length, end1, end2):
        HOElem.__init__(self, elemID, "Line")

        self.lineID = 0
        if isInt(lineID):
            self.lineID = lineID
        else:
            self.warning.append("LineIDError")

        self.z1 = complex(0+0j)
        if isComplex(z1):
            self.z1 = z1
        else:
            self.warning.append("ParameterError")

        self.y1 = None
        if isComplex(y1):
            self.y1 = y1
        else:
            self.warning.append("ParameterError")

        self.len = 0
        if isFloat(length) and length > 0:
            self.len = length
        else:
            self.warning.append("LengthError")

        if isInt(end1) and isInt(end2):
            self.connect.append(end1)
            self.connect.append(end2)
        else:
            self.warning.append("ConnectError")
        
        # For transmission line we do not need voltage info
        # However we still need voltage level to do reduction
        self.VL = None

        # Parameters for whole line
        self.Z = complex(0+0j)
        self.Y = None
        if len(self.warning) == 0:
            self.Z = self.z1 * self.len
            self.Y = self.y1 * self.len
        
        self.S = complex(0+0j) # power loss in line

    def getLineID(self):
        return self.lineID

    def setLineID(self, newID):
        if isInt(newID):
            self.lineID = newID
        else:
            self.warning.append("LineIDError")

    def getz1(self):
        return self.z1

    def setz1(self, newz1):
        if isComplex(newz1):
            self.z1 = newz1
        else:
            self.warning.append("ParameterError")

    def gety1(self):
        return self.y1

    def sety1(self, newy1):
        if isComplex(newy1) and newy1:
            self.y1 = newy1
        else:
            self.warning.append("ParameterError")

    def getLength(self):
        return self.len

    def setLength(self, newLength):
        if isFloat(newLength) and newLength > 0:
            self.len = newLength
        else:
            self.warning.append("LengthError")

    def getZ(self):
        return self.Z

    def getY(self):
        return self.Y

    def updateZY(self):
        # Calculate Z and Y by z1, y1 and len
        self.Z = self.z1 * self.len
        self.Y = self.y1 * self.len

    def getVoltageLevel(self):
        return self.VL

    def setVoltageLevelAuto(self):
        # Check the two buses connected and set to nearest standard voltage.
        # If the two buses are not accordingly, report error
        # If get voltage level from only one bus, set to that bus
        isCoherent = True
        findVoltLevel = 0
        for conn in self.getConnect():
            for elem in HOData.HOBus:
                if elem.getBusID() == conn:

                    if findVoltLevel == 0: #init, however if 1st VL=0 maybe 2nd one
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
    
    def checkConnect(self):
        # Check if connection is correct literally
        # however detailed check of bus should be done outside
        if self.getConnectN() == 2 and self.getConnect()[0] != self.getConnect()[1]:
            return True
        return False
        
    # Rewrite the method in base class
    def setConnect(self, end1, end2):
        if isInt(end1) and isInt(end2):
            self.connect = []
            self.connect.append(end1)
            self.connect.append(end2)
        else:
            self.warning.append("ConnectError")

    def doReduction(self, givenLevel):
        # do voltage reduction for Z and Y (is enough)
        if isInt(givenLevel) and isInVoltStdList(givenLevel) and self.VL:
            self.Z = self.Z * ((givenLevel/self.VL)**2)
            self.Y = self.Y / ((givenLevel/self.VL)**2)
        else:
            self.warning.append("ReductionError")

    def reDoReduction(self, givenLevel):
        # Redo reduction for Z and Y (is enough)
        if isInt(givenLevel) and isInVoltStdList(givenLevel) and self.VL:
            self.Z = self.Z * ((self.VL/givenLevel)**2)
            self.Y = self.Y / ((self.VL/givenLevel)**2)
        else:
            self.warning.append("ReductionError")

    def getPowerLoss(self):
        # Return power loss of the line
        return self.S

    def calcPowerLoss(self, y12con, y21con):
        # From the voltages of two ends, calculate the power flow
        # and then get the loss
        if (not isComplex(y12con)) or (not isComplex(y21con)):
            self.warning.append("ParameterError")
            return
        
        haveFound = False
        end1 = self.getConnect()[0]
        end2 = self.getConnect()[1]
        for elem1 in HOData.HOBus:
            for elem2 in HOData.HOBus:
                if elem1.getBusID() == end1 and elem2.getBusID() == end2:
                    haveFound = True

        if haveFound == True:
            U1 = eleml.getVoltage()
            U2 = elme2.getVoltage()
            U1con = elem1.getVoltage().conjugate()
            U2con = elem2.getVoltage().conjugate()
            y10con = elem1.gety0().conjugate()
            y20con = elem2.gety0().conjugate()

            S12 = U1 * (U1con*y10con + (U1con-U2con)*y12con)
            S21 = U2 * (U2con*y20con + (U2con-U1con)*y21con)
            self.S = S12 + S21

class HOLineBuild(HOLine, HOElem):

    # Set a new line by giving real line parameters
    # divR indicate the radius of the divided line
    # If n == 1 divR has no effect
    def __init__(self, elemID, lineID, material, area, r, n, divR,\
                 length, Dab, Dbc, Dac, end1, end2):
        HOElem.__init__(self, elemID, "RawLine")

        self.lineID = 0
        if isInt(lineID):
            self.lineID = lineID
        else:
            self.warning.append("LineIDError")
            
        
        # Determine the material
        self.material = ""
        if material in ["Al", "Cu"]:
            self.material = material
        else:
            self.warning.append("MaterialError")

        self.area = 0
        if isFloat(area) and area > 0:
            self.area = area
        else:
            self.warning.append("AreaError")

        self.radius = 0
        if isFloat(r) and r > 0 and approxSquare(r, self.area):
            self.radius = r
        else:
            self.warning.append("AreaError")
        
        # Set n, not support 5 values
        self.n = 0
        if n in [1, 2, 3, 4, 6]:
            self.n = n
        else:
            self.warning.append("LineDivError")

        # For n == 1 we do not care
        self.divR = 0
        if isFloat(divR) and divR >= 0:
            self.divR = divR
        else:
            self.warning.append("LineDivError")


        self.Dab = 0
        if isFloat(Dab) and Dab > 0:
            self.Dab = Dab
        else:
            self.warning.append("ParameterError")
        self.Dbc = 0
        if isFloat(Dbc) and Dbc > 0:
            self.Dbc = Dbc
        else:
            self.warning.append("ParameterError")
        self.Dac = 0
        if isFloat(Dac) and Dac > 0:
            self.Dac = Dac
        else:
            self.warning.append("ParameterError")

      
        # Determine z1 from real line parameters
        self.z1 = complex(0+0j)
        
        # Get r1
        if self.material == "Al":
            z1Real = 31.5 / self.area
        elif self.material == "Cu":
            z1Imag = 18.8 / self.area
        else:
            self.warning.append("ParameterError")
            
        # Get x1
        Dm = (self.Dab*self.Dbc*self.Dac) ** (1/3)

        req = None
        if self.radius > 0:
            if self.n == 1:
                req = self.radius;
            elif self.n == 2 and self.divR > 0:
                req = math.sqrt(self.radius * self.divR)
            elif self.n == 3 and self.divR > 0:
                req = (self.radius*self.divR*self.divR) ** (1/3)
            elif self.n == 4 and self.divR > 0:
                req = (self.radius * (self.divR**3) * math.sqrt(2)) ** (1/4)
            elif self.n == 6 and self.divR > 0:
                req = (self.radius * (self.divR**5) * 6) ** (1/6)

        if Dm > 0 and req > 0:
            z1Imag = 0.1445*math.log10(Dm/req) + 0.0157/n
        else:
            self.warning.append("ParameterError")
            

        # Determine y1 from real line parameters
        self.y1 = None
        if Dm > 0 and req > 0:
            self.y1 = complex(0+0j)
            y1Imag = 7.58 / math.log10(Dm/req) * (10**(-6))
            y1Real = 0
        else:
            self.warning.append("ParameterError")


        # Assign value to z1 and y1
        self.z1 = complex(z1Real, z1Imag)
        self.y1 = complex(y1Real, y1Imag)
        

        self.len = 0
        if isFloat(length) and length > 0:
            self.len = length
        else:
            self.warning.append("LengthError")

        if isInt(end1) and isInt(end2):
            self.connect.append(end1)
            self.connect.append(end2)
        else:
            self.warning.append("ConnectError")
        
        # For transmission line we do not need voltage info
        # However we still need voltage level to do reduction
        self.VL = None

        # Parameters for whole line
        self.Z = complex(0+0j)
        self.Y = None
        if len(self.warning) == 0:
            self.Z = self.z1 * self.len
            self.Y = self.y1 * self.len
        
        self.S = complex(0+0j) # power loss in line

    def getMaterial(self):
        return self.material

    def setMaterial(self, newMaterial):
        if newMaterial in ["Al", "Cu"]:
            self.material = newMaterial
        else:
            self.warning.append("MaterialError")

    def getArea(self):
        return self.area

    def setArea(self, newArea):
        if isFloat(newArea) and newArea > 0:
            self.area = newArea
            # automatically update radius
            if not approxSquare(self.radius, self.area):
                self.radius = math.sqrt(self.area)
        else:
            self.warning.append("AreaError")

    def getRadius(self):
        return self.radius

    def setRadius(self, newRadius):
        if isFloat(newRadius) and newRadius > 0:
            self.radius = newRadius
            # automatically update radius
            if not approxSquare(self.radius, self.area):
                self.area = self.radius ** 2
        else:
            self.warning.append("AreaError")

    def getDivN(self):
        return self.n

    def setDivN(self, newDivN):
        if newDivN in [1, 2, 3, 4, 6]:
            self.n = newDivN
        else:
            self.warning.append("LineDivError")

    def getDivR(self):
        return self.DivR

    def setDivR(self, newDivR):
        if isFloat(newDivR) and newDivR >= 0:
            self.DivR = newDivR
        else:
            self.warning.append("LineDivError")

    def getDab(self):
        return self.Dab

    def setDab(self, newDab):
        if isFloat(newDab) and newDab > 0:
            self.Dab = newDab
        else:
            self.warning.append("3LineError")

    def getDbc(self):
        return self.Dbc

    def setDbc(self, newDbc):
        if isFloat(newDbc) and newDbc > 0:
            self.Dbc = newDbc
        else:
            self.warning.append("3LineError")

    def getDac(self):
        return self.Dac

    def setDac(self, newDac):
        if isFloat(newDac) and newDac > 0:
            self.Dac = newDac
        else:
            self.warning.append("3LineError")
    
    
