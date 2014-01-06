# This file is a part of hexomega software.
# It define the class of tranformer.


from HOElem import *


class HOTrans(HOElem):

    # Set a new transformer
    # end1 and end2 are two ports of the transformer
    def __init__(self, elemID, lineID, Sn, Un, U2, Pk, Uk, P0, I0, end1, end2):
        HOElem.__init__(self, elemID, "Transformer")

        self.lineID = 0
        if isInt(lineID):
            self.lineID = lineID
        else:
            self.warning.append("LineIDError")


        self.Sn = 0
        if isFloat(Sn) and Sn > 0:
            self.Sn = Sn
        else:
            self.warning.append("ParameterError")


        # The voltage on the 1st side
        # is the original voltage level of the transformer
        self.Un = 0
        if isFloat(Un) and isInVoltTransList(Un):
            self.Un = Un
        else:
            self.warning.append("ParameterError")


        # The voltage on the 2nd side, we only deal with 2-winding transformer
        self.U2 = 0
        if isFloat(U2) and isInVoltTransList(U2):
            self.U2 = U2
        else:
            self.warning.append("ParameterError")


        self.Pk = 0
        if isFloat(Pk) and Pk > 0:
            self.Pk = Pk
        else:
            self.warning.append("ParameterError")


        # The value of %, max is 100
        self.Uk = 0
        if isFloat(Uk) and Uk > 0 and Uk < 100:
            self.Uk = Uk
        else:
            self.warning.append("ParameterError")


        self.P0 = 0
        if isFloat(P0) and P0 > 0:
            self.P0 = P0
        else:
            self.warning.append("ParameterError")


        # The value of %, max is 100
        self.I0 = 0
        if isFloat(I0) and I0 > 0 and I0 < 100:
            self.I0 = I0
        else:
            self.warning.append("ParameterError")


        # The two ports should be in specific order
        # NOTICE self.connect[0] is Un and self.connect[1] is U2
        if isInt(end1) and isInt(end2):
            self.connect.append(end1)
            self.connect.append(end2)
        else:
            self.warning.append("ConnectError")


        # After get all the descriptions, calculate
        # parameters on the 1st side
        self.Z = complex(0+0j)
        self.Y = None
        # None of these values are 0
        if self.Sn and self.Un and self.Pk and self.Uk \
           and self.P0 and self.I0:
            ZReal = self.Pk*(self.Un**2) / (1000 * (self.Sn**2))
            ZImag = self.Uk*(self.Un**2) / (100*self.Sn)
            self.Z = (ZReal, ZImag)
            
            YReal = self.P0 / (1000*(self.Un**2))
            # IMPORTANT! in transformer Y = G - jB
            YImag = -(self.I0*self.Sn / (100*(self.Un**2)))
            self.Y = (YReal, YImag)

        self.S = complex(0+0j) # Power loss in transformer

    def getLineID(self):
        return self.lineID

    def setLineID(self, newLineID):
        if isInt(newID):
            self.lineID = newLineID
        else:
            self.warning.append("LineIDError")

    def getSn(self):
        return self.Sn

    def setSn(self, newSn):
        if isFloat(newSn) and newSn > 0:
            self.Sn = newSn
        else:
            self.warning.append("ParameterError")

    def getUn(self):
        return self.Un

    def setUn(self, newUn):
        if isFloat(newUn) and newUn > 0:
            self.Un = newUn
        else:
            self.warning.append("ParameterError")

    def getU2(self):
        return self.U2

    def setU2(self, newU2):
        if isFloat(newU2) and newU2 > 0:
            self.U2 = newU2
        else:
            self.warning.append("ParameterError")

    def getPk(self):
        return self.Pk

    def setPk(self, newPk):
        if isFloat(newPk) and newPk > 0:
            self.Pk = newPk
        else:
            self.warning.append("ParameterError")

    def getUk(self):
        return self.Uk

    def setUk(self, newUk):
        # percentage, max is 100
        if isFloat(newUk) and newUk > 0 and newUk < 100:
            self.Uk = newUk
        else:
            self.warning.append("ParameterError")

    def getP0(self):
        return self.P0

    def setP0(self, newP0):
        if isFloat(newP0) and newP0 > 0:
            self.P0 = newP0
        else:
            self.warning.append("ParameterError")

    def getI0(self):
        return self.I0

    def setI0(self, newI0):
        # percentage, max is 100
        if isFloat(newI0) and newI0 > 0 and newI0 < 100:
            self.I0 = newI0
        else:
            self.warning.append("ParameterError")
    
    def getEnd1(self):
        return self.getConnect()[0]

    def getEnd2(self):
        return self.getConnect()[1]
        
    def getZ(self):
        return self.Z

    def getY(self):
        return self.Y

    def updateZY(self):
        # Calculate Z and Y by the parameters
        
        # None of these values are 0
        if self.Sn and self.Un and self.Pk and self.Uk \
           and self.P0 and self.I0:
            ZReal = self.Pk*(self.Un**2) / (1000 * (self.Sn**2))
            ZImag = self.Uk*(self.Un**2) / (100*self.Sn)
            self.Z = (ZReal, ZImag)
            
            YReal = self.P0 / (1000*(self.Un**2))
            # IMPORTANT! in transformer Y = G - jB
            YImag = -(self.I0*self.Sn / (100*(self.Un**2)))
            self.Y = (YReal, YImag)

    def getVoltageLevel(self):
        # The same as Un, only to add another interface
        return self.Un

    def setVoltageLevel(self, newVoltLevel):
        # Call setUn is enough
        self.setUn(newVoltLevel)

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
        # The voltage level of transformer is given by Un
        # Use Gamma type so there is only one admittance in Un side
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
        end1 = self.getEnd1()
        end2 = self.getEnd2()
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

