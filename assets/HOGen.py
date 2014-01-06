# This file is a part of hexomega software.
# It defines the class of generator


from HOElem import *
import HOData


class HOGen(HOElem):

    # Set a new generator
    # Here voltage is a complex number about the bus
    def __init__(self, elemID, busVolt, voltLevel, genVolt = "default"):
        HOElem.__init__(self, elemID, "VThetaBus")
        
        self.busID = 1 # Assume only one generator, will check it outside
        
        self.U = 0 # bus voltage
        if isComplex(busVolt) and isInVoltStdList(abs(busVolt)):
            self.U = busVolt
        else:
            self.warning.append("BusVoltageError")

        self.VL = 0 # voltage level of reduction
        if isInt(voltLevel) and isInVoltStdList(voltLevel):
            self.VL = voltLevel
        else:
            self.warning.append("VoltageLevelError")

        self.genVolt = 0 # voltage of generator, quite useless
        if (isFloat(genVolt) or isStr(genVolt)) \
           and isInVoltGenList(genVolt):
            self.genVolt = genVolt
        else:
            self.warning.append("GeneratorVoltageError")

        self.S = complex(0+0j) # Power flow OUT OF the generator, need to be calculated.

        # Self admittance to the ground, calculated by adding
        # half of admittance of all connected lines
        self.y0 = complex(0+0j)

    def getBusID(self):
        return self.busID

    def getBusVoltage(self):
        return self.U

    def setBusVoltage(self, newBusVolt):
        if isComplex(newBusVolt) and isInVoltStdList(abs(newBusVolt)):
            self.U = newBusVolt
        else:
            self.warning.append("BusVoltageError")

    def getVoltageLevel(self):
        return self.VL

    def setVoltageLevel(self, newVoltLevel):
        # That is reduction voltage
        if isInt(newVoltLevel) and isInVoltStdList(newVoltLevel):
            self.VL = newVoltLevel
        else:
            self.warning.append("VoltageLevelError")

        
    def getGenVoltage(self):
        return self.genVolt

    def setGenVoltage(self, newGenVolt):
        if (isFloat(newGenVolt) or isStr(newGenVolt)) \
           and isInVoltGenList(genVolt):
            self.genVolt = newGenVolt
        else:
            self.warning.append("GeneratorVoltageError")
        
    def getCPower(self):
        # return complex power
        return self.S

    def setCPower(self, newS):
        # get after all the calculation is done
        if isComplex(newS):
            self.S = newS
        else:
            self.warning.append("PowerError")

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
                             


    
