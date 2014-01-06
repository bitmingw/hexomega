# This file is a part of hexomga software.
# It defines the actions when a user triggers a UI event.


# The suffix S means the type is str

import sys
from tkinter import *

from HOGen import *
from HOLine import *
from HOTrans import *
from HOLoad import *

import HOData

# Call interface if a modification is required
import HODisp


def closeWindow(winName):
    # Search HOData.HOWin list and matching from end to begin
    HOData.HOWin.reverse()
    for elem in HOData.HOWin:
        if elem[1] == winName:
            elem[0].destroy()
            HOData.HOWin.remove(elem)
    HOData.HOWin.reverse()


def delLine(param1, param2 = None):
    # If only one parameter, is lineID
    # If two parameters, is two busID
    # Search the connected bus and remove the line info
    # And then remove the line
    if param2 == None:
        for elem in HOData.HOLine:
            if elem.getLineID() == param1:
                busConn = elem.getConnect() # Find the influenced bus
                for busLinked in busConn:
                    for busElem in HOData.HOBus:
                        if busElem.getBusID() == busLinked:
                            busElem.delConnect(busLinked) # Remove the info
                HOData.HOLine.remove(elem)

    else:
        for elem in HOData.HOLine:
            if elem.getConnect() == [param1, param2] or \
               elem.getConnect() == [param2, param1]:
                busConn = elem.getConnect() # Find the influenced bus
                for busLinked in busConn:
                    for busElem in HOData.HOBus:
                        if busElem.getBusID() == busLinked:
                            busElem.delConnect(busLinked) # Remove the info
                HOData.HOLine.remove(elem)            



def delBus(busID):
    # Search all the connected line, remove them
    # And then remove the bus
    # Call delLine() to accomplish the process
    for elem in HOData.HOBus:
        if elem.getBusID() == busID:
            lineConn = elem.getConnect() # Find the influenced line
            for lineLinked in lineConn:
                delLine(lineLinked)
            HOData.HOBus.remove(elem)
    


def HAddGen(elemIDS, busIDS, voltRealS, voltageLevelS, genVoltageS):
    # Try to convert these str to numerial
    try:
        elemID = int(elemIDS)
        busID = int(busIDS)
        voltReal = float(voltRealS)
        voltageLevel = int(voltageLevelS)
    except ValueError:
        invalidIn = messagebox.showerror('Input Error', 'Bad Input!')
        return False


    #### The handle of generatorVoltageS is not available now~

    
    # If it is revising mode
    if HOData.HOModInst != None \
       and HOData.HOModInst.getType() == 'VThetaBus':
        # First find the original class instance
        for elem in HOData.HOBus:
            if elem.getID() == HOData.HOModInst.getID():
                # Try to modify the duplicated instance
                HOData.HOModInst.clearError()
                HOData.HOModInst.setBusVoltage(complex(voltReal))
                HOData.HOModInst.setVoltageLevel(voltageLevel)
                # If no problem do the changes to original copy
                if len(HOData.HOModInst.getError()) == 0:
                    elem.clearError()
                    elem.setBusVoltage(complex(voltReal))
                    elem.setVoltageLevel(voltageLevel)
                    
                    HOData.HOModInst = None
                    HOData.HOModified = 1
                    closeWindow('addGen')
                    return True
                else:
                    invalidModify = messagebox.showerror('Error', \
                                                         'Modify Component Failure.')
                    return False
                
    else:
        # Else it is adding mode
        # Check elemID and if busID = 1 exist
        # If no problem set an instance of HOGen
        # If return no problem add the instance to list
        for elem in HOData.HOBus:
            if elemID == elem.getID():
                invalidID = messagebox.showerror('Fatal Error', \
                                                 'Component ID Error')
                return False
        for elem in HOData.HOLine:
            if elemID == elem.getID():
                invalidID = messagebox.showerror('Fatal Error', \
                                                 'Component ID Error')
                return False
        for elem in HOData.HOBus:
            if elem.getBusID() == 1:
                invalidGen = messagebox.showerror('Error', \
                                                  'You can add only one generator,' +
                                                  'please remove this.')
                return False

        newGen = HOGen(elemID, complex(voltReal), voltageLevel)
        if len(newGen.getError()) == 0:
            HOData.HOBus.append(newGen)
            HOData.HOElemID += 1
            HOData.HOBusID += 1
            HOData.HOModified = 1
            closeWindow('addGen')
            return True
        else:
            invalidInit = messagebox.showerror('Error', 'Initialize Component Failure.')
            return False
    


def HAddSolvedLine(elemIDS, lineIDS, r1S, x1S, g1S, b1S, lengthS, end1S, end2S):
    # First convert the parameters to float and then conbine to complex
    try:
        elemID = int(elemIDS)
        lineID = int(lineIDS)
        r1 = float(r1S)
        x1 = float(x1S)
        g1 = float(g1S)
        b1 = float(b1S)
        length = float(lengthS)
        end1 = int(end1S)
        end2 = int(end2S)
        z1 = complex(r1, x1)
        y1 = complex(g1, b1)
    except ValueError:
        invalidIn = messagebox.showerror('Input Error', 'Bad Input!')
        return False


    #### The checking of elemID, lineID and port is not available now~


    # If it is revising mode
    if HOData.HOModInst != None \
       and HOData.HOModInst.getType() == 'Line':
        # First find the original class instance
        for elem in HOData.HOLine:
            if elem.getID() == HOData.HOModInst.getID():
                # Try to modify the duplicated instance
                HOData.HOModInst.clearError()
                HOData.HOModInst.setz1(z1)
                HOData.HOModInst.sety1(y1)
                HOData.HOModInst.setLength(length)
                HOData.HOModInst.setConnect(end1, end2)
                if len(HOData.HOModInst.getError()) == 0:
                    elem.clearError()
                    elem.setLineID(lineID)
                    elem.setz1(z1)
                    elem.sety1(y1)
                    elem.setLength(length)
                    elem.setConnect(end1, end2)

                    HOData.HOModInst = None
                    HOData.HOModified = 1
                    closeWindow('addSLine')
                    return True
                else:
                    invalidModify = messagebox.showerror('Error', \
                                                         'Modify Component Failure.')
                    return False
                
    else:
        newSolvedLine = HOLine(elemID, lineID, z1, y1, length, end1, end2)
        if len(newSolvedLine.getError()) == 0:
            HOData.HOLine.append(newSolvedLine)
            HOData.HOElemID += 1
            HOData.HOLineID += 1
            HOData.HOModified = 1
            closeWindow('addSLine')
            return True
        else:
            invalidInit = messagebox.showerror('Error', 'Initialize Component Failure.')
            return False



def HAddUnsolvedLine(elemIDS, lineIDS, materialS, areaS, rS, nS, divRS, \
                     lengthS, DabS, DbcS, DacS, end1S, end2S):
    # Convert str to numerial
    try:
        elemID = int(elemIDS)
        lineID = int(lineIDS)
        material = str(materialS)
        area = float(areaS)
        r = float(rS)
        n = int(nS)
        divR = float(divRS)
        length = float(lengthS)
        Dab = float(DabS)
        Dbc = float(DbcS)
        Dac = float(DacS)
        end1 = int(end1S)
        end2 = int(end2S)
    except ValueError:
        invalidIn = messagebox.showerror('Input Error', 'Bad Input!')
        return False

    
    #### The checking of elemID, lineID and port is not available now~


    # If it is revising mode
    if HOData.HOModInst != None \
       and HOData.HOModInst.getType() == 'RawLine':
        # First find the original class instance
        for elem in HOData.HOLine:
            if elem.getID() == HOData.HOModInst.getID():
                # Try to modify the duplicated instance
                HOData.HOModInst.clearError()
                HOData.HOModInst.setMaterial(material)
                HOData.HOModInst.setArea(area)
                HOData.HOModInst.setRadius(r)
                HOData.HOModInst.setDivN(n)
                HOData.HOModInst.setDivR(divR)
                HOData.HOModInst.setLength(length)
                HOData.HOModInst.setDab(Dab)
                HOData.HOModInst.setDbc(Dbc)
                HOData.HOModInst.setDac(Dac)
                HOData.HOModInst.setConnect(end1, end2)
                if len(HOData.HOModInst.getError()) == 0:
                    elem.clearError()
                    elem.setMaterial(material)
                    elem.setArea(area)
                    elem.setRadius(r)
                    elem.setDivN(n)
                    elem.setDivR(divR)
                    elem.setLength(length)
                    elem.setDab(Dab)
                    elem.setDbc(Dbc)
                    elem.setDac(Dac)
                    elem.setConnect(end1, end2)
                    
                    HOData.HOModInst = None
                    HOData.HOModified = 1
                    closeWindow('addULine')
                    return True
                else:
                    invalidModify = messagebox.showerror('Error', \
                                                         'Modify Component Failure.')
                    return False
                
    else:
        newUnsolvedLine = HOLineBuild(elemID, lineID, material, area, r, n, divR, \
                                      length, Dab, Dbc, Dac, end1, end2)
        if len(newUnsolvedLine.getError()) == 0:
            HOData.HOLine.append(newUnsolvedLine)
            HOData.HOElemID += 1
            HOData.HOLineID += 1
            HOData.HOModified = 1
            closeWindow('addULine')
            return True
        else:
            invalidInit = messagebox.showerror('Error', 'Initialize Component Failure.')
            return False
    


def HAddTrans(elemIDS, lineIDS, SnS, UnS, U2S, PkS, UkS, P0S, I0S, end1S, end2S):
    # Convert str to numerial
    try:
        elemID = int(elemIDS)
        lineID = int(lineIDS)
        Sn = float(SnS)
        Un = float(UnS)
        U2 = float(U2S)
        Pk = float(PkS)
        Uk = float(UkS)
        P0 = float(P0S)
        I0 = float(I0S)
        end1 = int(end1S)
        end2 = int(end2S)
    except ValueError:
        invalidIn = messagebox.showerror('Input Error', 'Bad Input!')
        return False


    #### The checking of elemID, lineID and port is not available now~


    # If it is revising mode
    if HOData.HOModInst != None \
       and HOData.HOModInst.getType() == 'RawLine':
        # First find the original class instance
        for elem in HOData.HOLine:
            if elem.getID() == HOData.HOModInst.getID():
                # Try to modify the duplicated instance
                HOData.HOModInst.clearError()
                HOData.HOModInst.setSn(Sn)
                HOData.HOModInst.setUn(Un)
                HOData.HOModInst.setU2(U2)
                HOData.HOModInst.setPk(Pk)
                HOData.HOModInst.setUk(Uk)
                HOData.HOModInst.setP0(P0)
                HOData.HOModInst.setI0(I0)
                HOData.HOModInst.setConnect(end1, end2)
                if len(HOData.HOModInst.getError()) == 0:
                    elem.clearError()
                    elem.setSn(Sn)
                    elem.setUn(Un)
                    elem.setU2(U2)
                    elem.setPk(Pk)
                    elem.setUk(Uk)
                    elem.setP0(P0)
                    elem.setI0(I0)
                    elem.setConnect(end1, end2)

                    HOData.HOModInst = None
                    HOData.HOModified = 1
                    closeWindow('addTrans')
                    return True
                else:
                    invalidModify = messagebox.showerror('Error', \
                                                         'Modify Component Failure.')
                    return False

    else:                
        newTrans = HOTrans(elemID, lineID, Sn, Un, U2, Pk, Uk, P0, I0, end1, end2)
        if len(newTrans.getError()) == 0:
            HOData.HOLine.append(newTrans)
            HOData.HOElemID += 1
            HOData.HOLineID += 1
            HOData.HOModified = 1
            closeWindow('addTrans')
            return True
        else:
            invalidInit = messagebox.showerror('Error', 'Initialize Component Failure.')
            return False



def HAddLoad(elemIDS, busIDS, powerRealS, powerImagS):
    # Convert str to numerial
    try:
        elemID = int(elemIDS)
        busID = int(busIDS)
        powerReal = float(powerRealS)
        powerImag = float(powerImagS)
        powerS = complex(powerReal, powerImag)
    except ValueError:
        invalidIn = messagebox.showerror('Input Error', 'Bad Input!')
        return False


    #### The checking of elemID and busID is not available now~


    # If it is revising mode
    if HOData.HOModInst != None \
       and HOData.HOModInst.getType() == 'RawLine':
        # First find the original class instance
        for elem in HOData.HOBus:
            if elem.getID() == HOData.HOModInst.getID():
                # Try to modify the duplicated instance
                HOData.HOModInst.clearError()
                HOData.HOModInst.setCPower(powerS)
                if len(HOData.HOModInst.getError()) == 0:
                    elem.clearError()
                    elem.setCPower(powerS)
                    
                    HOData.HOModInst = None
                    HOData.HOModified = 1
                    closeWindow('addLoad')
                    return True
                else:
                    invalidModify = messagebox.showerror('Error', \
                                                         'Modify Component Failure.')
                    return False
                
    else:
        newLoad = HOLoadPQ(elemID, busID, powerS)
        if len(newLoad.getError()) == 0:
            HOData.HOBus.append(newLoad)
            HOData.HOElemID += 1
            HOData.HOBusID += 1
            HOData.HOModified = 1
            closeWindow('addLoad')
            return True
        else:
            invalidInit = messagebox.showerror('Error', 'Initialize Component Failure.')
            return False
    


def HAddCompensator(elemIDS, busIDS, powerRealS, voltRealS):
    # Convert str to numerial
    try:
        elemID = int(elemIDS)
        busID = int(busIDS)
        powerReal = float(powerRealS)
        voltReal = int(voltRealS)
    except ValueError:
        invalidIn = messagebox.showerror('Input Error', 'Bad Input!')
        return False


    #### The checking of elemID and busID is not available now~


    # If it is revising mode
    if HOData.HOModInst != None \
       and HOData.HOModInst.getType() == 'RawLine':
        # First find the original class instance
        for elem in HOData.HOBus:
            if elem.getID() == HOData.HOModInst.getID():
                # Try to modify the duplicated instance
                HOData.HOModInst.clearError()
                HOData.HOModInst.setCPower(complex(powerReal))
                HOData.HOModInst.setVoltage(complex(voltReal))
                if len(HOData.HOModInst.getError()) == 0:
                    elem.clearError()
                    elem.setCPower(complex(powerReal))
                    elem.setVoltage(complex(voltReal))

                    HOData.HOModInst = None
                    HOData.HOModified = 1
                    closeWindow('addComp')
                    return True
                else:
                    invalidModify = messagebox.showerror('Error', \
                                                         'Modify Component Failure.')
                    return False
                
    else:
        newCompensator = HOLoadPV(elemID, busID, complex(powerReal), complex(voltReal))
        if len(newCompensator.getError()) == 0:
            HOData.HOBus.append(newCompensator)
            HOData.HOElemID += 1
            HOData.HOBusID += 1
            HOData.HOModified = 1
            closeWindow('addComp')
            return True
        else:
            invalidInit = messagebox.showerror('Error', 'Initialize Component Failure.')
            return False



def HModElem(modChoiceS, param1, param2 = None):
    # Check modChoice and convert in different way
    try:
        if modChoiceS == 'BusBus':
            busID = int(param1)
        elif modChoiceS == 'LineLine':
            lineID = int(param1)
        elif modChoiceS == 'LineBus':
            lineBID1 = int(param1)
            lineBID2 = int(param2)
        else:
            raise ValueError
    except ValueError or TypeError:
        invalidIn = messagebox.showerror('Input Error', 'Bad Input!')
        return False

    # Try to find the element being modified
    # If find set HOModInst to the instance
    # If not raise error

    try:
        if modChoiceS == 'BusBus':
            for elem in HOData.HOBus:
                if elem.getBusID() == busID:
                    HOData.HOModInst = elem
                    
                    if elem.getType() == 'VThetaBus':
                        closeWindow('modElem')
                        HODisp.WAddGen()
                    elif elem.getType() == 'PQBus':
                        closeWindow('modElem')
                        HODisp.WAddLoad()
                    elif elem.getType() == 'PVBus':
                        closeWindow('modElem')
                        HODisp.WAddCompensator()
                    else:
                        raise ValueError
        
        elif modChoiceS == 'LineLine':
            for elem in HOData.HOLine:
                if elem.getLineID() == lineID:
                    HOData.HOModInst == elem
                    
                    if elem.getType() == 'Line':
                        closeWindow('modElem')
                        HODisp.WAddSolvedLine()
                    elif elem.getType() == 'RawLine':
                        closeWindow('modElem')
                        HODisp.WAddUnsolvedLine()
                    elif elem.getType() == 'Transformer':
                        closeWindow('modElem')
                        HODisp.WAddTrans()
                    else:
                        raise ValueError
        
        elif modChoiceS == 'LineBus':
            for elem in HOData.HOLine:
                if lineBID1 and lineBID2 in elem.getConnect():
                    HOData.HOModInst == elem

                    if elem.getType() == 'Line':
                        closeWindow('modElem')
                        HODisp.WAddSolvedLine()
                    elif elem.getType() == 'RawLine':
                        closeWindow('modElem')
                        HODisp.WAddUnsolvedLine()
                    elif elem.getType() == 'Transformer':
                        closeWindow('modElem')
                        HODisp.WAddTrans()
                    else:
                        raise ValueError
        
        else:
            raise ValueError
    except ValueError:
        invalidInit = messagebox.showerror('Error', 'Can not find component.')
        return False
        

    
def HRemoveElem(modChoiceS, param1, param2 = None):
    # Check modChioce and convert in different way
    try:
        if modChoiceS == 'BusBus':
            busID = int(param1)
        elif modChoiceS == 'LineLine':
            lineID = int(param1)
        elif modChoiceS == 'LineBus':
            lineBID1 = int(param1)
            lineBID2 = int(param2)
        else:
            raise ValueError
    except ValueError or TypeError:
        invalidIn = messagebox.showerror('Input Error', 'Bad Input!')
        return False

    # Try to find the element being removed
    # If find remove it and all its connection
    # If not raise error

    try:
        if modChoiceS == 'BusBus':
            for elem in HOData.HOBus:
                if elem.getBusID() == busID:
                    HOData.HOModInst = elem

                    if elem.getType() == 'VThetaBus':
                        closeWindow('removeElem')
                        delBus(busID)
                    elif elem.getType() == 'PQBus':
                        closeWindow('removeElem')
                        delBus(busID)
                    elif elem.getType() == 'PVBus':
                        closeWindow('removeElem')
                        delBus(busID)
                    else:
                        raise ValueError
                    
        elif modChoiceS == 'LineLine':
            for elem in HOData.HOLine:
                if elem.getLineID() == lineID:
                    HOData.HOModInst == elem
                    
                    if elem.getType() == 'Line':
                        closeWindow('removeElem')
                        delLine(lineID)
                    elif elem.getType() == 'RawLine':
                        closeWindow('removeElem')
                        delLine(lineID)
                    elif elem.getType() == 'Transformer':
                        closeWindow('removeElem')
                        delLine(lineID)
                    else:
                        raise ValueError
                    
        elif modChoiceS == 'LineBus':
            for elem in HOData.HOLine:
                if lineBID1 in elem.getConnect() and lineBID2 in elem.getConnect():
                    HOData.HOModInst == elem
                    
                    if elem.getType() == 'Line':
                        closeWindow('removeElem')
                        delLine(lineBID1, lineBID2)
                    elif elem.getType() == 'RawLine':
                        closeWindow('removeElem')
                        delLine(lineBID1, lineBID2)
                    elif elem.getType() == 'Transformer':
                        closeWindow('removeElem')
                        delLine(lineBID1, lineBID2)
                    else:
                        raise ValueError
        else:
            raise ValueError
    except ValueError:
        invalidInit = messagebox.showerror('Error', 'Can not find component.')
        return False

    
