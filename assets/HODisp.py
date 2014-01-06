# This file is a part of hexomega software.
# It defines most of the user interface.


from tkinter import *
import HOData

# The events are handled here
from HOAction import *


def WReset():
    if HOData.HOModified == 0:
        HOData.HOReset()
        # Draw with no parameters
    else:
        wReset = messagebox.askokcancel(title = 'Reset', \
                                       message = 'Are you sure to reset?')
        if wReset > 0:
            HOData.HOReset()
            # Draw with no parameters



def WOpen():
    # Return the file's handler, with mode 'r'
    HOData.HOOpenHandler = filedialog.askopenfile()



def WSave():
    # Return the file's handler, with mode 'w'
    HOData.HOSaveHandler = filedialog.asksaveasfile()




def WAddGen():
    # Layout
    # row 0-24 column 0-7
    # elemID (3, 1-2, fix)
    # busID (6, 1-2, fix)
    # busVoltage _ + _ j (9, 1-6, 2nd fix)
    # generatorVoltage (12, 1-3)
    # reductionVoltage (15, 1-3)
    # OK (20-21, 2)
    # Cancel (20-21, 5)
    
    addGen = Tk()
    HOData.HOWin.append([addGen, 'addGen'])
    addGen.geometry(HOData.WGeometry)
    addGen.title('Add a Generator')


    addGen.update_idletasks() # update info
    # get cell size
    cellWidth = addGen.winfo_width() // HOData.WColumnSegN
    cellHeight = addGen.winfo_height() // HOData.WRowSegN
    # set grid
    sepColumn0 = Canvas(addGen, height = cellHeight, width = cellWidth)
    sepColumn0.grid(row = 0, column = 0)
    sepColumn1 = Canvas(addGen, height = cellHeight, width = cellWidth)
    sepColumn1.grid(row = 0, column = 1)
    sepColumn2 = Canvas(addGen, height = cellHeight, width = cellWidth)
    sepColumn2.grid(row = 0, column = 2)
    sepColumn3 = Canvas(addGen, height = cellHeight, width = cellWidth)
    sepColumn3.grid(row = 0, column = 3)
    sepColumn4 = Canvas(addGen, height = cellHeight, width = cellWidth)
    sepColumn4.grid(row = 0, column = 4)
    sepColumn5 = Canvas(addGen, height = cellHeight, width = cellWidth)
    sepColumn5.grid(row = 0, column = 5)
    sepColumn6 = Canvas(addGen, height = cellHeight, width = cellWidth)
    sepColumn6.grid(row = 0, column = 6)
    sepColumn7 = Canvas(addGen, height = cellHeight, width = cellWidth)
    sepColumn7.grid(row = 0, column = 7)


    # add blank lines and elements in the grid
    sepRow1 = Canvas(addGen, height = cellHeight, width = cellWidth)
    sepRow1.grid(row = 1, column = 0)
    sepRow2 = Canvas(addGen, height = cellHeight, width = cellWidth)
    sepRow2.grid(row = 2, column = 0)
    
    elemIDL = Label(addGen, text = 'Component ID')
    elemIDL.grid(row = 3, column = 1)
    addGenElemID = StringVar(addGen, str(HOData.HOElemID))
    elemID = Entry(addGen, textvariable = addGenElemID, \
                   width = HOData.WWidth, state = DISABLED)
    elemID.grid(row = 3, column = 2)


    sepRow4 = Canvas(addGen, height = cellHeight, width = cellWidth)
    sepRow4.grid(row = 4, column = 0)
    sepRow5 = Canvas(addGen, height = cellHeight, width = cellWidth)
    sepRow5.grid(row = 5, column = 0)
    
    busIDL = Label(addGen, text = 'Bus ID')
    busIDL.grid(row = 6, column = 1)
    addGenBusID = StringVar(addGen, '1')
    busID = Entry(addGen, textvariable = addGenBusID, \
                  width = HOData.WWidth, state = DISABLED)
    busID.grid(row = 6, column = 2)


    sepRow7 = Canvas(addGen, height = cellHeight, width = cellWidth)
    sepRow7.grid(row = 7, column = 0)
    sepRow8 = Canvas(addGen, height = cellHeight, width = cellWidth)
    sepRow8.grid(row = 8, column = 0)
    
    busVoltL = Label(addGen, text = 'Bus Volt')
    busVoltL.grid(row = 9, column = 1)
    addGenBusVoltReal = StringVar(addGen)
    busVoltReal = Entry(addGen, textvariable = addGenBusVoltReal, \
                        width = HOData.WWidth)
    busVoltReal.grid(row = 9, column = 2)
    busVoltLAdd = Label(addGen, text = '+')
    busVoltLAdd.grid(row = 9, column = 3)
    addGenBusVoltImag = StringVar(addGen, '0')
    busVoltImag = Entry(addGen, textvariable = addGenBusVoltImag, \
                        width = HOData.WWidth, state = DISABLED)
    busVoltImag.grid(row = 9, column = 4)
    busVoltLj = Label(addGen, text = 'j')
    busVoltLj.grid(row = 9, column = 5)
    busVoltLKV = Label(addGen, text = 'KV')
    busVoltLKV.grid(row = 9, column = 6)
    

    sepRow10 = Canvas(addGen, height = cellHeight, width = cellWidth)
    sepRow10.grid(row = 10, column = 0)
    sepRow11 = Canvas(addGen, height = cellHeight, width = cellWidth)
    sepRow11.grid(row = 11, column = 0)

    genVoltL = Label(addGen, text = 'Generator Volt')
    genVoltL.grid(row = 12, column = 1)
    addGenGenVolt = StringVar(addGen, 'default')
    genVolt = Entry(addGen, textvariable = addGenGenVolt, \
                    width = HOData.WWidth)
    genVolt.grid(row = 12, column = 2)
    genVoltLKV = Label(addGen, text = 'KV')
    genVoltLKV.grid(row = 12, column = 3)


    sepRow13 = Canvas(addGen, height = cellHeight, width = cellWidth)
    sepRow13.grid(row = 13, column = 0)
    sepRow14 = Canvas(addGen, height = cellHeight, width = cellWidth)
    sepRow14.grid(row = 14, column = 0)    

    redVoltL = Label(addGen, text = 'Reduction Volt')
    redVoltL.grid(row = 15, column = 1)
    addGenRedVolt = StringVar(addGen)
    redVolt = Entry(addGen, textvariable = addGenRedVolt, \
                    width = HOData.WWidth)
    redVolt.grid(row = 15, column = 2)
    redVoltLKV = Label(addGen, text = 'KV')
    redVoltLKV.grid(row = 15, column = 3)


    sepRow16 = Canvas(addGen, height = cellHeight, width = cellWidth)
    sepRow16.grid(row = 16, column = 0)
    sepRow17 = Canvas(addGen, height = cellHeight, width = cellWidth)
    sepRow17.grid(row = 17, column = 0)
    sepRow18 = Canvas(addGen, height = cellHeight, width = cellWidth)
    sepRow18.grid(row = 18, column = 0)
    sepRow19 = Canvas(addGen, height = cellHeight, width = cellWidth)
    sepRow19.grid(row = 19, column = 0)  


    # If the interface is called to modify an existing element
    if HOData.HOModInst != None \
       and HOData.HOModInst.getType() == 'VThetaBus':
        addGen.title('Modify a Generator')
        addGenElemID.set(str(HOData.HOModInst.getID()))
        addGenBusID.set(str(HOData.HOModInst.getBusID()))
        addGenBusVoltReal.set(str(HOData.HOModInst.getBusVoltage().real))
        addGenGenVolt.set(str(HOData.HOModInst.getGenVoltage()))
        addGenRedVolt.set(str(HOData.HOModInst.getVoltageLevel()))

    addGenOK = Button(addGen, text = 'OK', \
                      width = HOData.WWidth, \
                      command = lambda: HAddGen(elemID.get(), \
                                               busID.get(), \
                                               busVoltReal.get(), \
                                               redVolt.get(), \
                                               genVolt.get()))
    addGenOK.grid(row = 20, column = 2, rowspan = 2)

    
    addGenCancel = Button(addGen, text = 'Cancel', \
                          width = HOData.WWidth, \
                          command = lambda: addGen.destroy())
    addGenCancel.grid(row = 20, column = 5, rowspan = 2)


    addGen.mainloop()



def WAddSolvedLine():
    # Layout
    # row 0-24 colunm 0-7
    # elemID (4, 1-2, fix)
    # lineID (6, 1-2, fix)
    # r1 (4, 4-6)
    # x1 (6, 4-6)
    # g1 (8, 4-6)
    # b1 (10, 4-6)
    # lenght (12, 4-6)
    # end1 (14, 4-5)
    # end2 (14, 4-5)
    # OK (20-21, 2)
    # Cancel (20-21, 5)

    addSLine = Tk()
    HOData.HOWin.append([addSLine, 'addSLine'])
    addSLine.geometry(HOData.WGeometry)
    addSLine.title('Add a Solved Line')


    addSLine.update_idletasks() # update info
    # get cell size
    cellWidth = addSLine.winfo_width() // HOData.WColumnSegN
    cellHeight = addSLine.winfo_height() // HOData.WRowSegN
    # set grid
    sepColumn0 = Canvas(addSLine, height = cellHeight, width = cellWidth)
    sepColumn0.grid(row = 0, column = 0)
    sepColumn1 = Canvas(addSLine, height = cellHeight, width = cellWidth)
    sepColumn1.grid(row = 0, column = 1)
    sepColumn2 = Canvas(addSLine, height = cellHeight, width = cellWidth)
    sepColumn2.grid(row = 0, column = 2)
    sepColumn3 = Canvas(addSLine, height = cellHeight, width = cellWidth)
    sepColumn3.grid(row = 0, column = 3)
    sepColumn4 = Canvas(addSLine, height = cellHeight, width = cellWidth)
    sepColumn4.grid(row = 0, column = 4)
    sepColumn5 = Canvas(addSLine, height = cellHeight, width = cellWidth)
    sepColumn5.grid(row = 0, column = 5)
    sepColumn6 = Canvas(addSLine, height = cellHeight, width = cellWidth)
    sepColumn6.grid(row = 0, column = 6)
    sepColumn7 = Canvas(addSLine, height = cellHeight, width = cellWidth)
    sepColumn7.grid(row = 0, column = 7)


    # add blank lines and elements in the grid
    sepRow1 = Canvas(addSLine, height = cellHeight, width = cellWidth)
    sepRow1.grid(row = 1, column = 0)
    sepRow2 = Canvas(addSLine, height = cellHeight, width = cellWidth)
    sepRow2.grid(row = 2, column = 0)
    sepRow3 = Canvas(addSLine, height = cellHeight, width = cellWidth)
    sepRow3.grid(row = 3, column = 0)

    elemIDL = Label(addSLine, text = 'Component ID')
    elemIDL.grid(row = 4, column = 1)
    addSolvedLineElemID = StringVar(addSLine, str(HOData.HOElemID))
    elemID = Entry(addSLine, textvariable = addSolvedLineElemID, \
                   width = HOData.WWidth, state = DISABLED)
    elemID.grid(row = 4, column = 2)

    sepRow5 = Canvas(addSLine, height = cellHeight, width = cellWidth)
    sepRow5.grid(row = 5, column = 0)

    lineIDL = Label(addSLine, text = 'Line ID')
    lineIDL.grid(row = 6, column = 1)
    addSolvedLineID = StringVar(addSLine, str(HOData.HOLineID))
    lineID = Entry(addSLine, textvariable = addSolvedLineID, \
                  width = HOData.WWidth, state = DISABLED)
    lineID.grid(row = 6, column = 2)


    liner1L = Label(addSLine, text = 'r1')
    liner1L.grid(row = 4, column = 4)
    addSolvedLiner1 = StringVar(addSLine)
    liner1 = Entry(addSLine, textvariable = addSolvedLiner1, \
                   width = HOData.WWidth)
    liner1.grid(row = 4, column = 5)
    liner1OmegaKM = Label(addSLine, text = 'Omega / km')
    liner1OmegaKM.grid(row = 4, column = 6)


    linex1L = Label(addSLine, text = 'x1')
    linex1L.grid(row = 6, column = 4)
    addSolvedLinex1 = StringVar(addSLine)
    linex1 = Entry(addSLine, textvariable = addSolvedLinex1, \
                   width = HOData.WWidth)
    linex1.grid(row = 6, column = 5)
    linex1OmegaKM = Label(addSLine, text = 'Omega / km')
    linex1OmegaKM.grid(row = 6, column = 6)


    sepRow7 = Canvas(addSLine, height = cellHeight, width = cellWidth)
    sepRow7.grid(row = 7, column = 0)

    lineg1L = Label(addSLine, text = 'g1')
    lineg1L.grid(row = 8, column = 4)
    addSolvedLineg1 = StringVar(addSLine)
    lineg1 = Entry(addSLine, textvariable = addSolvedLineg1, \
                   width = HOData.WWidth)
    lineg1.grid(row = 8, column = 5)
    lineg1SKM = Label(addSLine, text = 'S / km')
    lineg1SKM.grid(row = 8, column = 6)


    sepRow9 = Canvas(addSLine, height = cellHeight, width = cellWidth)
    sepRow9.grid(row = 9, column = 0)    

    lineb1L = Label(addSLine, text = 'b1')
    lineb1L.grid(row = 10, column = 4)
    addSolvedLineb1 = StringVar(addSLine)
    lineb1 = Entry(addSLine, textvariable = addSolvedLineb1, \
                   width = HOData.WWidth)
    lineb1.grid(row = 10, column = 5)
    lineb1SKM = Label(addSLine, text = 'S / km')
    lineb1SKM.grid(row = 10, column = 6)


    sepRow11 = Canvas(addSLine, height = cellHeight, width = cellWidth)
    sepRow11.grid(row = 11, column = 0)

    lineLenL = Label(addSLine, text = 'Line Length')
    lineLenL.grid(row = 12, column = 4)
    addSolvedLineLen = StringVar(addSLine)
    lineLen = Entry(addSLine, textvariable = addSolvedLineLen, \
                    width = HOData.WWidth)
    lineLen.grid(row = 12, column = 5)
    lineLenKM = Label(addSLine, text = 'km')
    lineLenKM.grid(row = 12, column = 6)
    

    sepRow13 = Canvas(addSLine, height = cellHeight, width = cellWidth)
    sepRow13.grid(row = 13, column = 0)

    lineEnd1L = Label(addSLine, text = '1st Port') # busID
    lineEnd1L.grid(row = 14, column = 4)
    addSolvedLineEnd1 = StringVar(addSLine)
    lineEnd1 = Entry(addSLine, textvariable = addSolvedLineEnd1, \
                     width = HOData.WWidth)
    lineEnd1.grid(row = 14, column = 5)
    

    sepRow15 = Canvas(addSLine, height = cellHeight, width = cellWidth)
    sepRow15.grid(row = 15, column = 0)

    lineEnd2L = Label(addSLine, text = '2nd Port') # busID
    lineEnd2L.grid(row = 16, column = 4)
    addSolvedLineEnd2 = StringVar(addSLine)
    lineEnd2 = Entry(addSLine, textvariable = addSolvedLineEnd2, \
                     width = HOData.WWidth)
    lineEnd2.grid(row = 16, column = 5)


    sepRow17 = Canvas(addSLine, height = cellHeight, width = cellWidth)
    sepRow17.grid(row = 17, column = 0)
    sepRow18 = Canvas(addSLine, height = cellHeight, width = cellWidth)
    sepRow18.grid(row = 18, column = 0)
    sepRow19 = Canvas(addSLine, height = cellHeight, width = cellWidth)
    sepRow19.grid(row = 19, column = 0)


    # If the interface is called to modify an existing element
    if HOData.HOModInst != None \
       and HOData.HOModInst.getType() == 'Line':
        addSLine.title('Modify a Solved Line')
        addSolvedLineElemID.set(str(HOData.HOModInst.getID()))
        addSolvedLineID.set(str(HOData.HOModInst.getLineID()))
        addSolvedLiner1.set(str(HOData.HOModInst.getz1().real))
        addSolvedLinex1.set(str(HOData.HOModInst.getz1().imag))
        addSolvedLineg1.set(str(HOData.HOModInst.gety1().real))
        addSolvedLineb1.set(str(HOData.HOModInst.gety1().imag))
        addSolvedLineLen.set(str(HOData.HOModInst.getLength()))
        addSolvedLineEnd1.set(str(HOData.HOModInst.getConnect()[0]))
        addSolvedLineEnd2.set(str(HOData.HOModInst.getConnect()[1]))
    
    addSLineOK = Button(addSLine, text = 'OK', \
                      width = HOData.WWidth, \
                        command = lambda: HAddSolvedLine(elemID.get(), \
                                                         lineID.get(), \
                                                         liner1.get(), \
                                                         linex1.get(), \
                                                         lineg1.get(), \
                                                         lineb1.get(), \
                                                         lineLen.get(), \
                                                         lineEnd1.get(), \
                                                         lineEnd2.get()))
    addSLineOK.grid(row = 20, column = 2, rowspan = 2)
    
    
    addSLineCancel = Button(addSLine, text = 'Cancel', \
                          width = HOData.WWidth, \
                            command = lambda: addSLine.destroy())
    addSLineCancel.grid(row = 20, column = 5, rowspan = 2)
    

    addSLine.mainloop()



def WAddUnsolvedLine():
    # Layout
    # row 0-24 column 0-7
    # elemID (3, 1-2, fix)
    # lineID (5, 1-2, fix)
    # material (7-8, 1-2, radiobutton)
    # area (10, 1-3)
    # radius (12, 1-3)
    # n (3, 4-5)
    # divR (5, 4-6)
    # length(7, 4-6)
    # Dab (9, 4-6)
    # Dbc (11, 4-6)
    # Dac (13, 4-6)
    # end1 (15, 4-5)
    # end2 (17, 4-5)
    # OK (20-21, 2)
    # Cancel (20-21, 5)

    addULine = Tk()
    HOData.HOWin.append([addULine, 'addULine'])
    addULine.geometry(HOData.WGeometry)
    addULine.title('Add a Unsolved Line')


    addULine.update_idletasks() # update info
    # get cell size
    cellWidth = addULine.winfo_width() // HOData.WColumnSegN
    cellHeight = addULine.winfo_height() // HOData.WRowSegN
    # set grid
    sepColumn0 = Canvas(addULine, height = cellHeight, width = cellWidth)
    sepColumn0.grid(row = 0, column = 0)
    sepColumn1 = Canvas(addULine, height = cellHeight, width = cellWidth)
    sepColumn1.grid(row = 0, column = 1)
    sepColumn2 = Canvas(addULine, height = cellHeight, width = cellWidth)
    sepColumn2.grid(row = 0, column = 2)
    sepColumn3 = Canvas(addULine, height = cellHeight, width = cellWidth)
    sepColumn3.grid(row = 0, column = 3)
    sepColumn4 = Canvas(addULine, height = cellHeight, width = cellWidth)
    sepColumn4.grid(row = 0, column = 4)
    sepColumn5 = Canvas(addULine, height = cellHeight, width = cellWidth)
    sepColumn5.grid(row = 0, column = 5)
    sepColumn6 = Canvas(addULine, height = cellHeight, width = cellWidth)
    sepColumn6.grid(row = 0, column = 6)
    sepColumn7 = Canvas(addULine, height = cellHeight, width = cellWidth)
    sepColumn7.grid(row = 0, column = 7)


    # add blank lines and elements in the grid
    sepRow1 = Canvas(addULine, height = cellHeight, width = cellWidth)
    sepRow1.grid(row = 1, column = 0)
    sepRow2 = Canvas(addULine, height = cellHeight, width = cellWidth)
    sepRow2.grid(row = 2, column = 0)

    elemIDL = Label(addULine, text = 'Component ID')
    elemIDL.grid(row = 3, column = 1)
    addUnsolvedLineElemID = StringVar(addULine, str(HOData.HOElemID))
    elemID = Entry(addULine, textvariable = addUnsolvedLineElemID, \
                   width = HOData.WWidth, state = DISABLED)
    elemID.grid(row = 3, column = 2)


    sepRow4 = Canvas(addULine, height = cellHeight, width = cellWidth)
    sepRow4.grid(row = 4, column = 0)

    lineIDL = Label(addULine, text = 'Line ID')
    lineIDL.grid(row = 5, column = 1)
    addUnsolvedLineID = StringVar(addULine, str(HOData.HOLineID))
    lineID = Entry(addULine, textvariable = addUnsolvedLineID, \
                  width = HOData.WWidth, state = DISABLED)
    lineID.grid(row = 5, column = 2)


    sepRow6 = Canvas(addULine, height = cellHeight, width = cellWidth)
    sepRow6.grid(row = 6, column = 0)

    lineMaterialL = Label(addULine, text = 'Material')
    lineMaterialL.grid(row = 7, column = 1)
    lineMaterial = StringVar(addULine, "")
    lineMaterialAl = Radiobutton(addULine, text = 'Al', value = 'Al', \
                                 variable = lineMaterial)
    lineMaterialAl.grid(row = 7, column = 2)
    lineMaterialCu = Radiobutton(addULine, text = 'Cu', value = 'Cu', \
                                 variable = lineMaterial)
    lineMaterialCu.grid(row = 8, column = 2)


    sepRow9 = Canvas(addULine, height = cellHeight, width = cellWidth)
    sepRow9.grid(row = 9, column = 0)

    lineAreaL = Label(addULine, text = 'Area')
    lineAreaL.grid(row = 10, column = 1)
    addUnsolvedLineArea = StringVar(addULine)
    lineArea = Entry(addULine, textvariable = addUnsolvedLineArea, \
                     width = HOData.WWidth)
    lineArea.grid(row = 10, column = 2)
    lineMM2 = Label(addULine, text = 'mm^2')
    lineMM2.grid(row = 10, column = 3)


    sepRow11 = Canvas(addULine, height = cellHeight, width = cellWidth)
    sepRow11.grid(row = 11, column = 0)

    lineRadiusL = Label(addULine, text = 'Radius')
    lineRadiusL.grid(row = 12, column = 1)
    addUnsolvedLineRadius = StringVar(addULine)
    lineRadius = Entry(addULine, textvariable = addUnsolvedLineRadius, \
                       width = HOData.WWidth)
    lineRadius.grid(row = 12, column = 2)
    lineRMM = Label(addULine, text = 'mm')
    lineRMM.grid(row = 12, column = 3)


    lineNL = Label(addULine, text = 'N Lines')
    lineNL.grid(row = 3, column = 4)
    addUnsolvedLineN = StringVar(addULine, '1')
    lineN = Entry(addULine, textvariable = addUnsolvedLineN, \
                  width = HOData.WWidth)
    lineN.grid(row = 3, column = 5)


    lineDivRL = Label(addULine, text = 'Div Radius')
    lineDivRL.grid(row = 5, column = 4)
    addUnsolvedLineDivR = StringVar(addULine)
    lineDivR = Entry(addULine, textvariable = addUnsolvedLineDivR, \
                     width = HOData.WWidth)
    lineDivR.grid(row = 5, column = 5)
    lineDMM = Label(addULine, text = 'mm')
    lineDMM.grid(row = 5, column = 6)


    lineLenL = Label(addULine, text = 'Line Length')
    lineLenL.grid(row = 7, column = 4)
    addUnsolvedLineLen = StringVar(addULine)
    lineLen = Entry(addULine, textvariable = addUnsolvedLineLen, \
                    width = HOData.WWidth)
    lineLen.grid(row = 7, column = 5)
    lineLenKM = Label(addULine, text = 'km')
    lineLenKM.grid(row = 7, column = 6)


    lineDabL = Label(addULine, text = 'Dab')
    lineDabL.grid(row = 9, column = 4)
    addUnsolvedLineDab = StringVar(addULine)
    lineDab = Entry(addULine, textvariable = addUnsolvedLineDab, \
                    width = HOData.WWidth)
    lineDab.grid(row = 9, column = 5)
    lineDabM = Label(addULine, text = 'm')
    lineDabM.grid(row = 9, column = 6)


    lineDbcL = Label(addULine, text = 'Dbc')
    lineDbcL.grid(row = 11, column = 4)
    addUnsolvedLineDbc = StringVar(addULine)
    lineDbc = Entry(addULine, textvariable = addUnsolvedLineDbc, \
                    width = HOData.WWidth)
    lineDbc.grid(row = 11, column = 5)
    lineDbcM = Label(addULine, text = 'm')
    lineDbcM.grid(row = 11, column = 6)   


    lineDacL = Label(addULine, text = 'Dac')
    lineDacL.grid(row = 13, column = 4)
    addUnsolvedLineDac = StringVar(addULine)
    lineDac = Entry(addULine, textvariable = addUnsolvedLineDac, \
                    width = HOData.WWidth)
    lineDac.grid(row = 13, column = 5)
    lineDacM = Label(addULine, text = 'm')
    lineDacM.grid(row = 13, column = 6)


    sepRow14 = Canvas(addULine, height = cellHeight, width = cellWidth)
    sepRow14.grid(row = 14, column = 0)

    lineEnd1L = Label(addULine, text = '1st Port') # busID
    lineEnd1L.grid(row = 15, column = 4)
    addUnsolvedLineEnd1 = StringVar(addULine)
    lineEnd1 = Entry(addULine, textvariable = addUnsolvedLineEnd1, \
                     width = HOData.WWidth)
    lineEnd1.grid(row = 15, column = 5)
    

    sepRow16 = Canvas(addULine, height = cellHeight, width = cellWidth)
    sepRow16.grid(row = 16, column = 0)

    lineEnd2L = Label(addULine, text = '2nd Port') # busID
    lineEnd2L.grid(row = 17, column = 4)
    addUnsolvedLineEnd2 = StringVar(addULine)
    lineEnd2 = Entry(addULine, textvariable = addUnsolvedLineEnd2, \
                     width = HOData.WWidth)
    lineEnd2.grid(row = 17, column = 5)


    sepRow18 = Canvas(addULine, height = cellHeight, width = cellWidth)
    sepRow18.grid(row = 18, column = 0)
    sepRow19 = Canvas(addULine, height = cellHeight, width = cellWidth)
    sepRow19.grid(row = 19, column = 0)


    # If the interface is called to modify an existing element
    if HOData.HOModInst != None \
       and HOData.HOModInst.getType() == 'RawLine':
        addULine.title('Modify a Unsolved Line')
        addUnsolvedLineElemID.set(str(HOData.HOModInst.getID()))
        addUnsolvedLineID.set(str(HOData.HOModInst.getLineID()))
        lineMaterial.set(HOData.HOModInst.getMaterial)
        addUnsolvedLineArea.set(str(HOData.HOModInst.getArea()))
        addUnsolvedLineRadius.set(str(HOData.HOModInst.getRadius()))
        addUnsolvedLineN.set(str(HOData.HOModInst.getDivN()))
        addUnsolvedLineDivR.set(str(HOData.HOModInst.getDivR()))
        addUnsolvedLineLen.set(str(HOData.HOModInst.getLength()))
        addUnsolvedLineDab.set(str(HOData.HOModInst.getDab()))
        addUnsolvedLineDbc.set(str(HOData.HOModInst.getDbc()))
        addUnsolvedLineDac.set(str(HOData.HOModInst.getDac()))
        addUnsolvedLineEnd1.set(str(HOData.HOModInst.getConnect()[0]))
        addUnsolvedLineEnd2.set(str(HOData.HOModInst.getConnect()[1]))
        
    addULineOK = Button(addULine, text = 'OK', \
                      width = HOData.WWidth, \
                        command = lambda: HAddUnsolvedLine(elemID.get(), \
                                                           lineID.get(), \
                                                           lineMaterial.get(), \
                                                           lineArea.get(), \
                                                           lineRadius.get(), \
                                                           lineN.get(), \
                                                           lineDivR.get(), \
                                                           lineLen.get(), \
                                                           lineDab.get(), \
                                                           lineDbc.get(), \
                                                           lineDac.get(), \
                                                           lineEnd1.get(), \
                                                           lineEnd2.get()))
    addULineOK.grid(row = 20, column = 2, rowspan = 2)


    addULineCancel = Button(addULine, text = 'Cancel', \
                          width = HOData.WWidth, \
                            command = lambda: addULine.destroy())
    addULineCancel.grid(row = 20, column = 5, rowspan = 2)
   

    addULine.mainloop()



def WAddTrans():
    # Layout
    # row 0-24 column 0-7
    # elemID (2, 1-2)
    # lineID (4, 1-2)
    # Sn (2, 4-6)
    # Un (4, 4-6)
    # U2 (6, 4-6)
    # Pk (8, 4-6)
    # Uk (10, 4-6)
    # P0 (12, 4-6)
    # I0 (14, 4-6)
    # end1 (16, 4-5)
    # end2 (18, 4-5)
    # OK (21-22, 2)
    # Cancel (21-22, 5)

    addTrans = Tk()
    HOData.HOWin.append([addTrans, 'addTrans'])
    addTrans.geometry(HOData.WGeometry)
    addTrans.title('Add a Transformer')


    addTrans.update_idletasks() # update info
    # get cell size
    cellWidth = addTrans.winfo_width() // HOData.WColumnSegN
    cellHeight = addTrans.winfo_height() // HOData.WRowSegN
    # set grid
    sepColumn0 = Canvas(addTrans, height = cellHeight, width = cellWidth)
    sepColumn0.grid(row = 0, column = 0)
    sepColumn1 = Canvas(addTrans, height = cellHeight, width = cellWidth)
    sepColumn1.grid(row = 0, column = 1)
    sepColumn2 = Canvas(addTrans, height = cellHeight, width = cellWidth)
    sepColumn2.grid(row = 0, column = 2)
    sepColumn3 = Canvas(addTrans, height = cellHeight, width = cellWidth)
    sepColumn3.grid(row = 0, column = 3)
    sepColumn4 = Canvas(addTrans, height = cellHeight, width = cellWidth)
    sepColumn4.grid(row = 0, column = 4)
    sepColumn5 = Canvas(addTrans, height = cellHeight, width = cellWidth)
    sepColumn5.grid(row = 0, column = 5)
    sepColumn6 = Canvas(addTrans, height = cellHeight, width = cellWidth)
    sepColumn6.grid(row = 0, column = 6)
    sepColumn7 = Canvas(addTrans, height = cellHeight, width = cellWidth)
    sepColumn7.grid(row = 0, column = 7)


    # add blank lines and elements in the grid
    sepRow1 = Canvas(addTrans, height = cellHeight, width = cellWidth)
    sepRow1.grid(row = 1, column = 0)

    elemIDL = Label(addTrans, text = 'Component ID')
    elemIDL.grid(row = 2, column = 1)
    addTransElemID = StringVar(addTrans, str(HOData.HOElemID))
    elemID = Entry(addTrans, textvariable = addTransElemID, \
                   width = HOData.WWidth, state = DISABLED)
    elemID.grid(row = 2, column = 2)

    sepRow3 = Canvas(addTrans, height = cellHeight, width = cellWidth)
    sepRow3.grid(row = 3, column = 0)

    lineIDL = Label(addTrans, text = 'Line ID')
    lineIDL.grid(row = 4, column = 1)
    addTransID = StringVar(addTrans, str(HOData.HOLineID))
    lineID = Entry(addTrans, textvariable = addTransID, \
                  width = HOData.WWidth, state = DISABLED)
    lineID.grid(row = 4, column = 2)


    transSnL = Label(addTrans, text = 'Sn')
    transSnL.grid(row = 2, column = 4)
    addTransSn = StringVar(addTrans)
    transSn = Entry(addTrans, textvariable = addTransSn, \
                    width = HOData.WWidth)
    transSn.grid(row = 2, column = 5)
    transSnMVA = Label(addTrans, text = 'MVA')
    transSnMVA.grid(row = 2, column = 6)


    transUnL = Label(addTrans, text = 'Un')
    transUnL.grid(row = 4, column = 4)
    addTransUn = StringVar(addTrans)
    transUn = Entry(addTrans, textvariable = addTransUn, \
                    width = HOData.WWidth)
    transUn.grid(row = 4, column = 5)
    transUnKV = Label(addTrans, text = 'KV')
    transUnKV.grid(row = 4, column = 6)


    sepRow5 = Canvas(addTrans, height = cellHeight, width = cellWidth)
    sepRow5.grid(row = 5, column = 0)

    transU2L = Label(addTrans, text = 'U2')
    transU2L.grid(row = 6, column = 4)
    addTransU2 = StringVar(addTrans)
    transU2 = Entry(addTrans, textvariable = addTransU2, \
                    width = HOData.WWidth)
    transU2.grid(row = 6, column = 5)
    transUnKV = Label(addTrans, text = 'KV')
    transUnKV.grid(row = 6, column = 6)


    sepRow7 = Canvas(addTrans, height = cellHeight, width = cellWidth)
    sepRow7.grid(row = 7, column = 0)

    transPkL = Label(addTrans, text = 'Pk')
    transPkL.grid(row = 8, column = 4)
    addTransPk = StringVar(addTrans)
    transPk = Entry(addTrans, textvariable = addTransPk, \
                    width = HOData.WWidth)
    transPk.grid(row = 8, column = 5)
    transPkKW = Label(addTrans, text = 'KW')
    transPkKW.grid(row = 8, column = 6)


    sepRow9 = Canvas(addTrans, height = cellHeight, width = cellWidth)
    sepRow9.grid(row = 9, column = 0)

    transUkL = Label(addTrans, text = 'Uk')
    transUkL.grid(row = 10, column = 4)
    addTransUk = StringVar(addTrans)
    transUk = Entry(addTrans, textvariable = addTransUk, \
                    width = HOData.WWidth)
    transUk.grid(row = 10, column = 5)
    transUkPerc = Label(addTrans, text = '%')
    transUkPerc.grid(row = 10, column = 6)


    sepRow11 = Canvas(addTrans, height = cellHeight, width = cellWidth)
    sepRow11.grid(row = 11, column = 0)

    transP0L = Label(addTrans, text = 'P0')
    transP0L.grid(row = 12, column = 4)
    addTransP0 = StringVar(addTrans)
    transP0 = Entry(addTrans, textvariable = addTransP0, \
                    width = HOData.WWidth)
    transP0.grid(row = 12, column = 5)
    transP0KW = Label(addTrans, text = 'KW')
    transP0KW.grid(row = 12, column = 6)


    sepRow13 = Canvas(addTrans, height = cellHeight, width = cellWidth)
    sepRow13.grid(row = 13, column = 0)

    transI0L = Label(addTrans, text = 'I0')
    transI0L.grid(row = 14, column = 4)
    addTransI0 = StringVar(addTrans)
    transI0 = Entry(addTrans, textvariable = addTransI0, \
                    width = HOData.WWidth)
    transI0.grid(row = 14, column = 5)
    transI0Perc = Label(addTrans, text = '%')
    transI0Perc.grid(row = 14, column = 6)


    sepRow15 = Canvas(addTrans, height = cellHeight, width = cellWidth)
    sepRow15.grid(row = 15, column = 0)
    
    transEnd1L = Label(addTrans, text = '1st Port') # busID
    transEnd1L.grid(row = 16, column = 4)
    addTransEnd1 = StringVar(addTrans)
    transEnd1 = Entry(addTrans, textvariable = addTransEnd1, \
                     width = HOData.WWidth)
    transEnd1.grid(row = 16, column = 5)

    sepRow17 = Canvas(addTrans, height = cellHeight, width = cellWidth)
    sepRow17.grid(row = 17, column = 0)

    transEnd2L = Label(addTrans, text = '2nd Port') # busID
    transEnd2L.grid(row = 18, column = 4)
    addTransEnd2 = StringVar(addTrans)
    transEnd2 = Entry(addTrans, textvariable = addTransEnd2, \
                     width = HOData.WWidth)
    transEnd2.grid(row = 18, column = 5)


    sepRow19 = Canvas(addTrans, height = cellHeight, width = cellWidth)
    sepRow19.grid(row = 19, column = 0)
    sepRow20 = Canvas(addTrans, height = cellHeight, width = cellWidth)
    sepRow20.grid(row = 20, column = 0)


    # If the interface is called to modify an existing element
    if HOData.HOModInst != None \
       and HOData.HOModInst.getType() == 'Transformer':
        addTrans.title('Modify a Transformer')
        addTransElemID.set(str(HOData.HOModInst.getID()))
        addTransID.set(str(HOData.HOModInst.getLineID()))
        addTransSn.set(str(HOData.HOModInst.getSn()))
        addTransUn.set(str(HOData.HOModInst.getUn()))
        addTransU2.set(str(HOData.HOModInst.getU2()))
        addTransPk.set(str(HOData.HOModInst.getPk()))
        addTransUk.set(str(HOData.HOModInst.getUk()))
        addTransP0.set(str(HOData.HOModInst.getP0()))
        addTransI0.set(str(HOData.HOModInst.getI0()))
        addTransEnd1.set(str(HOData.HOModInst.getEnd1()))
        addTransEnd2.set(str(HOData.HOModInst.getEnd2()))
        
    addTransOK = Button(addTrans, text = 'OK', \
                      width = HOData.WWidth, \
                            command = lambda: HAddTrans(elemID.get(), \
                                                        lineID.get(), \
                                                        transSn.get(), \
                                                        transUn.get(), \
                                                        transU2.get(), \
                                                        transPk.get(), \
                                                        transUk.get(), \
                                                        transP0.get(), \
                                                        transI0.get(), \
                                                        transEnd1.get(), \
                                                        transEnd2.get()))
    addTransOK.grid(row = 21, column = 2, rowspan = 2)


    addTransCancel = Button(addTrans, text = 'Cancel', \
                          width = HOData.WWidth, \
                            command = lambda: addTrans.destroy())
    addTransCancel.grid(row = 21, column = 5, rowspan = 2)
   

    addTrans.mainloop()



def WAddLoad():
    # Layout
    # row 0-24 column 0-7
    # elemID (6, 1-2)
    # busID (10, 1-2)
    # complexPower _ + _ j (14, 1-6)
    # OK (19-20, 2)
    # Cancel (19-20, 5)

    addLoad = Tk()
    HOData.HOWin.append([addLoad, 'addLoad'])
    addLoad.geometry(HOData.WGeometry)
    addLoad.title('Add a Load')


    addLoad.update_idletasks() # update info
    # get cell size
    cellWidth = addLoad.winfo_width() // HOData.WColumnSegN
    cellHeight = addLoad.winfo_height() // HOData.WRowSegN
    # set grid
    sepColumn0 = Canvas(addLoad, height = cellHeight, width = cellWidth)
    sepColumn0.grid(row = 0, column = 0)
    sepColumn1 = Canvas(addLoad, height = cellHeight, width = cellWidth)
    sepColumn1.grid(row = 0, column = 1)
    sepColumn2 = Canvas(addLoad, height = cellHeight, width = cellWidth)
    sepColumn2.grid(row = 0, column = 2)
    sepColumn3 = Canvas(addLoad, height = cellHeight, width = cellWidth)
    sepColumn3.grid(row = 0, column = 3)
    sepColumn4 = Canvas(addLoad, height = cellHeight, width = cellWidth)
    sepColumn4.grid(row = 0, column = 4)
    sepColumn5 = Canvas(addLoad, height = cellHeight, width = cellWidth)
    sepColumn5.grid(row = 0, column = 5)
    sepColumn6 = Canvas(addLoad, height = cellHeight, width = cellWidth)
    sepColumn6.grid(row = 0, column = 6)
    sepColumn7 = Canvas(addLoad, height = cellHeight, width = cellWidth)
    sepColumn7.grid(row = 0, column = 7)


    # add blank lines and elements in the grid
    sepRow1 = Canvas(addLoad, height = cellHeight, width = cellWidth)
    sepRow1.grid(row = 1, column = 0)
    sepRow2 = Canvas(addLoad, height = cellHeight, width = cellWidth)
    sepRow2.grid(row = 2, column = 0)
    sepRow3 = Canvas(addLoad, height = cellHeight, width = cellWidth)
    sepRow3.grid(row = 3, column = 0)
    sepRow4 = Canvas(addLoad, height = cellHeight, width = cellWidth)
    sepRow4.grid(row = 4, column = 0)
    sepRow5 = Canvas(addLoad, height = cellHeight, width = cellWidth)
    sepRow5.grid(row = 5, column = 0)

    elemIDL = Label(addLoad, text = 'Component ID')
    elemIDL.grid(row = 6, column = 1)
    addLoadElemID = StringVar(addLoad, str(HOData.HOElemID))
    elemID = Entry(addLoad, textvariable = addLoadElemID, \
                   width = HOData.WWidth, state = DISABLED)
    elemID.grid(row = 6, column = 2)


    sepRow7 = Canvas(addLoad, height = cellHeight, width = cellWidth)
    sepRow7.grid(row = 7, column = 0)
    sepRow8 = Canvas(addLoad, height = cellHeight, width = cellWidth)
    sepRow8.grid(row = 8, column = 0)
    sepRow9 = Canvas(addLoad, height = cellHeight, width = cellWidth)
    sepRow9.grid(row = 9, column = 0)

    busIDL = Label(addLoad, text = 'Bus ID')
    busIDL.grid(row = 10, column = 1)
    addLoadBusID = StringVar(addLoad, str(HOData.HOBusID))
    busID = Entry(addLoad, textvariable = addLoadBusID, \
                  width = HOData.WWidth, state = DISABLED)
    busID.grid(row = 10, column = 2)


    sepRow11 = Canvas(addLoad, height = cellHeight, width = cellWidth)
    sepRow11.grid(row = 11, column = 0)
    sepRow12 = Canvas(addLoad, height = cellHeight, width = cellWidth)
    sepRow12.grid(row = 12, column = 0)
    sepRow13 = Canvas(addLoad, height = cellHeight, width = cellWidth)
    sepRow13.grid(row = 13, column = 0)
    
    busPowerL = Label(addLoad, text = 'Bus Power')
    busPowerL.grid(row = 14, column = 1)
    addLoadBusPowerReal = StringVar(addLoad)
    busPowerReal = Entry(addLoad, textvariable = addLoadBusPowerReal, \
                        width = HOData.WWidth)
    busPowerReal.grid(row = 14, column = 2)
    busPowerLAdd = Label(addLoad, text = '+')
    busPowerLAdd.grid(row = 14, column = 3)
    addLoadBusPowerImag = StringVar(addLoad)
    busPowerImag = Entry(addLoad, textvariable = addLoadBusPowerImag, \
                        width = HOData.WWidth)
    busPowerImag.grid(row = 14, column = 4)
    busPowerLj = Label(addLoad, text = 'j')
    busPowerLj.grid(row = 14, column = 5)
    busPowerLKW = Label(addLoad, text = 'KW')
    busPowerLKW.grid(row = 14, column = 6)

   
    sepRow15 = Canvas(addLoad, height = cellHeight, width = cellWidth)
    sepRow15.grid(row = 15, column = 0)
    sepRow16 = Canvas(addLoad, height = cellHeight, width = cellWidth)
    sepRow16.grid(row = 16, column = 0)
    sepRow17 = Canvas(addLoad, height = cellHeight, width = cellWidth)
    sepRow17.grid(row = 17, column = 0)
    sepRow18 = Canvas(addLoad, height = cellHeight, width = cellWidth)
    sepRow18.grid(row = 18, column = 0)


    # If the interface is called to modify an existing element
    if HOData.HOModInst != None \
       and HOData.HOModInst.getType() == 'PQBus':
        addLoad.title('Modify a Load')
        addLoadElemID.set(str(HOData.HOModInst.getID()))
        addLoadBusID.set(str(HOData.HOModInst.getBusID()))
        addLoadBusPowerReal.set(str(HOData.HOModInst.getCPower().real))
        addLoadBusPowerImag.set(str(HOData.HOModInst.getCPower().imag))
        
    addLoadOK = Button(addLoad, text = 'OK', \
                      width = HOData.WWidth, \
                       command = lambda: HAddLoad(elemID.get(), \
                                                  busID.get(), \
                                                  busPowerReal.get(), \
                                                  busPowerImag.get()))
    addLoadOK.grid(row = 19, column = 2, rowspan = 2)

    
    addLoadCancel = Button(addLoad, text = 'Cancel', \
                          width = HOData.WWidth, \
                           command = lambda: addLoad.destroy())
    addLoadCancel.grid(row = 19, column = 5, rowspan = 2)


    addLoad.mainloop()



def WAddCompensator():
    # Layout
    # row 0-24 column 0-7
    # elemID (4, 1-2)
    # busID (8, 1-2)
    # P (12, 1-3)
    # V (16, 1-3)
    # OK (19-20, 2)
    # Cancel (19-20, 5)
    
    addComp = Tk()
    HOData.HOWin.append([addComp, 'addComp'])
    addComp.geometry(HOData.WGeometry)
    addComp.title('Add a Compensator')


    addComp.update_idletasks() # update info
    # get cell size
    cellWidth = addComp.winfo_width() // HOData.WColumnSegN
    cellHeight = addComp.winfo_height() // HOData.WRowSegN
    # set grid
    sepColumn0 = Canvas(addComp, height = cellHeight, width = cellWidth)
    sepColumn0.grid(row = 0, column = 0)
    sepColumn1 = Canvas(addComp, height = cellHeight, width = cellWidth)
    sepColumn1.grid(row = 0, column = 1)
    sepColumn2 = Canvas(addComp, height = cellHeight, width = cellWidth)
    sepColumn2.grid(row = 0, column = 2)
    sepColumn3 = Canvas(addComp, height = cellHeight, width = cellWidth)
    sepColumn3.grid(row = 0, column = 3)
    sepColumn4 = Canvas(addComp, height = cellHeight, width = cellWidth)
    sepColumn4.grid(row = 0, column = 4)
    sepColumn5 = Canvas(addComp, height = cellHeight, width = cellWidth)
    sepColumn5.grid(row = 0, column = 5)
    sepColumn6 = Canvas(addComp, height = cellHeight, width = cellWidth)
    sepColumn6.grid(row = 0, column = 6)
    sepColumn7 = Canvas(addComp, height = cellHeight, width = cellWidth)
    sepColumn7.grid(row = 0, column = 7)


    # add blank lines and elements in the grid
    sepRow1 = Canvas(addComp, height = cellHeight, width = cellWidth)
    sepRow1.grid(row = 1, column = 0)
    sepRow2 = Canvas(addComp, height = cellHeight, width = cellWidth)
    sepRow2.grid(row = 2, column = 0)
    sepRow3 = Canvas(addComp, height = cellHeight, width = cellWidth)
    sepRow3.grid(row = 3, column = 0)

    elemIDL = Label(addComp, text = 'Component ID')
    elemIDL.grid(row = 4, column = 1)
    addCompElemID = StringVar(addComp, str(HOData.HOElemID))
    elemID = Entry(addComp, textvariable = addCompElemID, \
                   width = HOData.WWidth, state = DISABLED)
    elemID.grid(row = 4, column = 2)


    sepRow5 = Canvas(addComp, height = cellHeight, width = cellWidth)
    sepRow5.grid(row = 5, column = 0)
    sepRow6 = Canvas(addComp, height = cellHeight, width = cellWidth)
    sepRow6.grid(row = 6, column = 0)
    sepRow7 = Canvas(addComp, height = cellHeight, width = cellWidth)
    sepRow7.grid(row = 7, column = 0)

    busIDL = Label(addComp, text = 'Bus ID')
    busIDL.grid(row = 8, column = 1)
    addCompBusID = StringVar(addComp, str(HOData.HOBusID))
    busID = Entry(addComp, textvariable = addCompBusID, \
                  width = HOData.WWidth, state = DISABLED)
    busID.grid(row = 8, column = 2)


    sepRow9 = Canvas(addComp, height = cellHeight, width = cellWidth)
    sepRow9.grid(row = 9, column = 0)
    sepRow10 = Canvas(addComp, height = cellHeight, width = cellWidth)
    sepRow10.grid(row = 10, column = 0)
    sepRow11 = Canvas(addComp, height = cellHeight, width = cellWidth)
    sepRow11.grid(row = 11, column = 0)

    busPowerL = Label(addComp, text = 'Active Power')
    busPowerL.grid(row = 12, column = 1)
    addCompBusPower = StringVar(addComp)
    busPower = Entry(addComp, textvariable = addCompBusPower, \
                     width = HOData.WWidth)
    busPower.grid(row = 12, column = 2)
    busPowerKW = Label(addComp, text = 'KW')
    busPowerKW.grid(row = 12, column = 3)
    

    sepRow13 = Canvas(addComp, height = cellHeight, width = cellWidth)
    sepRow13.grid(row = 13, column = 0)
    sepRow14 = Canvas(addComp, height = cellHeight, width = cellWidth)
    sepRow14.grid(row = 14, column = 0)
    sepRow15 = Canvas(addComp, height = cellHeight, width = cellWidth)
    sepRow15.grid(row = 15, column = 0)

    busVoltRealL = Label(addComp, text = 'Volt Real')
    busVoltRealL.grid(row = 16, column = 1)
    addCompBusVoltReal = StringVar(addComp)
    busVoltReal = Entry(addComp, textvariable = addCompBusVoltReal, \
                        width = HOData.WWidth)
    busVoltReal.grid(row = 16, column = 2)
    busVoltKV = Label(addComp, text = 'KV')
    busVoltKV.grid(row = 16, column = 3)

 
    sepRow17 = Canvas(addComp, height = cellHeight, width = cellWidth)
    sepRow17.grid(row = 17, column = 0)
    sepRow18 = Canvas(addComp, height = cellHeight, width = cellWidth)
    sepRow18.grid(row = 18, column = 0)
    sepRow19 = Canvas(addComp, height = cellHeight, width = cellWidth)
    sepRow19.grid(row = 19, column = 0)


    # If the interface is called to modify an existing element
    if HOData.HOModInst != None \
       and HOData.HOModInst.getType() == 'PVBus':
        addComp.title('Add a Compensator')
        addCompElemID.set(str(HOData.HOModInst.getID()))
        addCompBusID.set(str(HOData.HOModInst.getBusID()))
        addCompBusPower.set(str(HOData.HOModInst.getCPower().real))
        addCompBusVoltReal.set(str(HOData.HOModInst.getVoltage().real))
        
    addCompOK = Button(addComp, text = 'OK', \
                      width = HOData.WWidth, \
                       command = lambda: HAddCompensator(elemID.get(), \
                                                 busID.get(), \
                                                 busPower.get(), \
                                                 busVoltReal.get()))
    addCompOK.grid(row = 20, column = 2, rowspan = 2)

    
    addCompCancel = Button(addComp, text = 'Cancel', \
                          width = HOData.WWidth, \
                           command = lambda: addComp.destroy())
    addCompCancel.grid(row = 20, column = 5, rowspan = 2)


    addComp.mainloop()



def WModElem():
    # Tk chooses the element to modify
    # Then open the specific function to load
    # and modify the parameters
    # Use global variables to load the data

    # Layout
    # row 0-24 column 0-7
    # Prompt for RadioButton (4, 1-2)
    # RadioButton (5-7, 1-2)
    # removeBus LabelFrame (12-15, 1-2, last row is blank)
    # removeLine LabelFrame (12-15, 4-5, last row is blank)
    # OK (19-20, 2)
    # Cancel(19-20, 5)
    
    modElem = Tk()
    HOData.HOWin.append([modElem, 'modElem'])
    modElem.geometry(HOData.WGeometry)
    modElem.title('Modify a component')


    modElem.update_idletasks() # update info
    # get cell size
    cellWidth = modElem.winfo_width() // HOData.WColumnSegN
    cellHeight = modElem.winfo_height() // HOData.WRowSegN
    # set grid
    sepColumn0 = Canvas(modElem, height = cellHeight, width = cellWidth)
    sepColumn0.grid(row = 0, column = 0)
    sepColumn1 = Canvas(modElem, height = cellHeight, width = cellWidth)
    sepColumn1.grid(row = 0, column = 1)
    sepColumn2 = Canvas(modElem, height = cellHeight, width = cellWidth)
    sepColumn2.grid(row = 0, column = 2)
    sepColumn3 = Canvas(modElem, height = cellHeight, width = cellWidth)
    sepColumn3.grid(row = 0, column = 3)
    sepColumn4 = Canvas(modElem, height = cellHeight, width = cellWidth)
    sepColumn4.grid(row = 0, column = 4)
    sepColumn5 = Canvas(modElem, height = cellHeight, width = cellWidth)
    sepColumn5.grid(row = 0, column = 5)
    sepColumn6 = Canvas(modElem, height = cellHeight, width = cellWidth)
    sepColumn6.grid(row = 0, column = 6)
    sepColumn7 = Canvas(modElem, height = cellHeight, width = cellWidth)
    sepColumn7.grid(row = 0, column = 7)


    # add blank lines and elements in the grid
    sepRow1 = Canvas(modElem, height = cellHeight, width = cellWidth)
    sepRow1.grid(row = 1, column = 0)
    sepRow2 = Canvas(modElem, height = cellHeight, width = cellWidth)
    sepRow2.grid(row = 2, column = 0)
    sepRow3 = Canvas(modElem, height = cellHeight, width = cellWidth)
    sepRow3.grid(row = 3, column = 0)

    modChoiceL = Label(modElem, text = 'Choose How to Modify')
    modChoiceL.grid(row = 4, column = 1, columnspan = 2)
    modChoice = StringVar(modElem, "")
    modBusBusR = Radiobutton(modElem, text = 'Modify bus by busID', \
                            value = 'BusBus', variable = modChoice)
    modBusBusR.grid(row = 5, column = 1, columnspan = 2)
    modLineLineR = Radiobutton(modElem, text = 'Modify line by lineID', \
                              value = 'LineLine', variable = modChoice)
    modLineLineR.grid(row = 6, column = 1, columnspan = 2)
    modLineBusR = Radiobutton(modElem, text = 'Modify line by busID', \
                             value = 'LineBus', variable = modChoice)
    modLineBusR.grid(row = 7, column = 1, columnspan = 2)


    sepRow8 = Canvas(modElem, height = cellHeight, width = cellWidth)
    sepRow8.grid(row = 8, column = 0)
    sepRow9 = Canvas(modElem, height = cellHeight, width = cellWidth)
    sepRow9.grid(row = 9, column = 0)
    sepRow10 = Canvas(modElem, height = cellHeight, width = cellWidth)
    sepRow10.grid(row = 10, column = 0)
    sepRow11 = Canvas(modElem, height = cellHeight, width = cellWidth)
    sepRow11.grid(row = 11, column = 0)

    # Define a small Frame to hold 1 busID   
    modBusPanel = LabelFrame(modElem, text = 'Modify a Bus', \
                             height = cellHeight*4, width = cellWidth*2)
    modBusPanel.grid(row = 12, column = 1, rowspan = 4, columnspan = 2)
    modBusPanel.grid_propagate(0) # Force change grid size

    # Get small Frame size
    modBusPanel.update_idletasks()
    modBusHeight = modBusPanel.winfo_height()
    modBusWidth = modBusPanel.winfo_width()

    # Since the grid can be multiplexing
    # Just separate the small Frame into 3 * 2 case
    # However to achieve better result, choose 4 * 2
    modBusCellHeight = modBusHeight // 4
    modBusCellWidth = modBusWidth // 2
    
    # Separate the small frame by .grid() method
    # First define column
    sepBusColumn0 = Canvas(modBusPanel, height = modBusCellHeight, \
                           width = modBusCellWidth)
    sepBusColumn0.grid(row = 0, column = 0)
    sepBusColumn1 = Canvas(modBusPanel, height = modBusCellHeight, \
                           width = modBusCellWidth)
    sepBusColumn1.grid(row = 0, column = 1)
       
    # Then add 'BusID' Label in (1, 0) and Entry in (1, 1)
    modBusIDL = Label(modBusPanel, text = 'Bus ID')
    modBusIDL.grid(row = 1, column = 0)
    modBusBusID = StringVar(modBusPanel)
    # Set conditions to disable
    modBusID = Entry(modBusPanel, textvariable = modBusBusID, \
                        width = HOData.WWidth//2) # Shorten width here
    modBusID.grid(row = 1, column = 1)


    # Define a small Frame to hold 2 busID and 1 lineID
    modLinePanel = LabelFrame(modElem, text = 'Modify a Line', \
                              height = cellHeight*4, width = cellWidth*2)
    modLinePanel.grid(row = 12, column = 4, rowspan = 4, columnspan = 2)
    modLinePanel.grid_propagate(0) # Force change grid size

    # Get small Frame size
    modLinePanel.update_idletasks()
    modLineHeight = modLinePanel.winfo_height()
    modLineWidth = modLinePanel.winfo_width()

    # Since the grid can be multiplexing
    # Just separate the small Frame into 3 * 2 case
    # However to achieve better result, choose 4 * 2
    modLineCellHeight = modLineHeight // 4
    modLineCellWidth = modLineWidth // 2
    
    # Separate the small frame by .grid() method
    # First define column
    sepLineColumn0 = Canvas(modLinePanel, height = modLineCellHeight, \
                           width = modLineCellWidth)
    sepLineColumn0.grid(row = 0, column = 0)
    sepLineColumn1 = Canvas(modLinePanel, height = modLineCellHeight, \
                           width = modLineCellWidth)
    sepLineColumn1.grid(row = 0, column = 1)

    # Then add 1 lineID
    modLineIDL = Label(modLinePanel, text = 'Line ID')
    modLineIDL.grid(row = 0, column = 0)
    modLineLineID = StringVar(modLinePanel)
    # Set conditions to disable
    modLineID = Entry(modLinePanel, textvariable = modLineLineID, \
                      width = HOData.WWidth//2) # Shorten width here
    modLineID.grid(row = 0, column = 1)

    # Finally add 2 busID
    modLineBID1L = Label(modLinePanel, text = 'Bus ID 1')
    modLineBID1L.grid(row = 1, column = 0)
    modLineBusID1 = StringVar(modLinePanel)
    # Set conditions to disable
    modLineBID1 = Entry(modLinePanel, textvariable = modLineBusID1, \
                        width = HOData.WWidth//2) # Shorten width here
    modLineBID1.grid(row = 1, column = 1)

    modLineBID2L = Label(modLinePanel, text = 'Bus ID 2')
    modLineBID2L.grid(row = 2, column = 0)
    modLineBusID2 = StringVar(modLinePanel)
    # Set conditions to disable
    modLineBID2 = Entry(modLinePanel, textvariable = modLineBusID2, \
                        width = HOData.WWidth//2) # Shorten width here
    modLineBID2.grid(row = 2, column = 1)


    sepRow16 = Canvas(modElem, height = cellHeight, width = cellWidth)
    sepRow16.grid(row = 16, column = 0)
    sepRow17 = Canvas(modElem, height = cellHeight, width = cellWidth)
    sepRow17.grid(row = 17, column = 0)
    sepRow18 = Canvas(modElem, height = cellHeight, width = cellWidth)
    sepRow18.grid(row = 18, column = 0)


    # Change the states of Entrys according to the Radiobuttons
    # Currently use def in def to pass parameters to command option
    # Have to pass the list of Entrys as the function's parameter
    entryList = [modBusID, modLineID, modLineBID1, modLineBID2]
    def modSet(modChoice, entryList):
        if modChoice.get() == 'BusBus':
            entryList[0].config(state = NORMAL)
            entryList[1].config(state = DISABLED)
            entryList[2].config(state = DISABLED)
            entryList[3].config(state = DISABLED)
        elif modChoice.get() == 'LineLine':
            entryList[0].config(state = DISABLED)
            entryList[1].config(state = NORMAL)
            entryList[2].config(state = DISABLED)
            entryList[3].config(state = DISABLED)
        elif modChoice.get() == 'LineBus':
            entryList[0].config(state = DISABLED)
            entryList[1].config(state = DISABLED)
            entryList[2].config(state = NORMAL)
            entryList[3].config(state = NORMAL)
        else:
            entryList[0].config(state = NORMAL)
            entryList[1].config(state = NORMAL)
            entryList[2].config(state = NORMAL)
            entryList[3].config(state = NORMAL)
    
    # Update the states of Entrys if events happen
    modBusBusR.config(command = lambda: modSet(modChoice, entryList))
    modLineLineR.config(command = lambda: modSet(modChoice, entryList))
    modLineBusR.config(command = lambda: modSet(modChoice, entryList))

    # Define the event of OK button
    def modHandle(modChoice, entryList):
        if modChoice.get() == 'BusBus':
            HModElem(modChoice.get(), modBusID.get())
            return
        elif modChoice.get() == 'LineLine':
            HMOdElem(modChoice.get(), modLineID.get())
            return
        elif modChoice.get() == 'LineBus':
            HModElem(modChoice.get(), modLineBID1.get(), modLineBID2.get())
            return
        else:
            pass # Do nothing

    
    modElemOK = Button(modElem, text = 'OK', \
                      width = HOData.WWidth, \
                       command = lambda: modHandle(modChoice, entryList))
    modElemOK.grid(row = 19, column = 2, rowspan = 2)

    
    modElemCancel = Button(modElem, text = 'Cancel', \
                          width = HOData.WWidth, \
                           command = lambda: modElem.destroy())
    modElemCancel.grid(row = 19, column = 5, rowspan = 2)

    
    modElem.mainloop()



def WRemoveElem():
    # Tk chooses the element to remove
    # Then find the element in array to distroy
    # Use global variables to load the data

    # Layout is the same as WModElem()
    # row 0-24 column 0-7
    # Prompt for RadioButton (4, 1-2)
    # RadioButton (5-7, 1-2)
    # removeBus LabelFrame (12-15, 1-2, last row is blank)
    # removeLine LabelFrame (12-15, 4-5, last row is blank)
    # OK (19-20, 2)
    # Cancel(19-20, 5)
    
    removeElem = Tk()
    HOData.HOWin.append([removeElem, 'removeElem'])
    removeElem.geometry(HOData.WGeometry)
    removeElem.title('Remove a component')


    removeElem.update_idletasks() # update info
    # get cell size
    cellWidth = removeElem.winfo_width() // HOData.WColumnSegN
    cellHeight = removeElem.winfo_height() // HOData.WRowSegN
    # set grid
    sepColumn0 = Canvas(removeElem, height = cellHeight, width = cellWidth)
    sepColumn0.grid(row = 0, column = 0)
    sepColumn1 = Canvas(removeElem, height = cellHeight, width = cellWidth)
    sepColumn1.grid(row = 0, column = 1)
    sepColumn2 = Canvas(removeElem, height = cellHeight, width = cellWidth)
    sepColumn2.grid(row = 0, column = 2)
    sepColumn3 = Canvas(removeElem, height = cellHeight, width = cellWidth)
    sepColumn3.grid(row = 0, column = 3)
    sepColumn4 = Canvas(removeElem, height = cellHeight, width = cellWidth)
    sepColumn4.grid(row = 0, column = 4)
    sepColumn5 = Canvas(removeElem, height = cellHeight, width = cellWidth)
    sepColumn5.grid(row = 0, column = 5)
    sepColumn6 = Canvas(removeElem, height = cellHeight, width = cellWidth)
    sepColumn6.grid(row = 0, column = 6)
    sepColumn7 = Canvas(removeElem, height = cellHeight, width = cellWidth)
    sepColumn7.grid(row = 0, column = 7)


    # add blank lines and elements in the grid
    sepRow1 = Canvas(removeElem, height = cellHeight, width = cellWidth)
    sepRow1.grid(row = 1, column = 0)
    sepRow2 = Canvas(removeElem, height = cellHeight, width = cellWidth)
    sepRow2.grid(row = 2, column = 0)
    sepRow3 = Canvas(removeElem, height = cellHeight, width = cellWidth)
    sepRow3.grid(row = 3, column = 0)

    removeChoiceL = Label(removeElem, text = 'Choose How to Remove')
    removeChoiceL.grid(row = 4, column = 1, columnspan = 2)
    removeChoice = StringVar(removeElem, "")
    removeBusBusR = Radiobutton(removeElem, text = 'Remove bus by busID', \
                            value = 'BusBus', variable = removeChoice)
    removeBusBusR.grid(row = 5, column = 1, columnspan = 2)
    removeLineLineR = Radiobutton(removeElem, text = 'Remove line by lineID', \
                              value = 'LineLine', variable = removeChoice)
    removeLineLineR.grid(row = 6, column = 1, columnspan = 2)
    removeLineBusR = Radiobutton(removeElem, text = 'Remove line by busID', \
                             value = 'LineBus', variable = removeChoice)
    removeLineBusR.grid(row = 7, column = 1, columnspan = 2)
    # .invoke() here


    sepRow8 = Canvas(removeElem, height = cellHeight, width = cellWidth)
    sepRow8.grid(row = 8, column = 0)
    sepRow9 = Canvas(removeElem, height = cellHeight, width = cellWidth)
    sepRow9.grid(row = 9, column = 0)
    sepRow10 = Canvas(removeElem, height = cellHeight, width = cellWidth)
    sepRow10.grid(row = 10, column = 0)
    sepRow11 = Canvas(removeElem, height = cellHeight, width = cellWidth)
    sepRow11.grid(row = 11, column = 0)

    # Define a small Frame to hold 1 busID   
    removeBusPanel = LabelFrame(removeElem, text = 'Remove a Bus', \
                             height = cellHeight*4, width = cellWidth*2)
    removeBusPanel.grid(row = 12, column = 1, rowspan = 4, columnspan = 2)
    removeBusPanel.grid_propagate(0) # Force change grid size

    # Get small Frame size
    removeBusPanel.update_idletasks()
    removeBusHeight = removeBusPanel.winfo_height()
    removeBusWidth = removeBusPanel.winfo_width()

    # Since the grid can be multiplexing
    # Just separate the small Frame into 3 * 2 case
    # However to achieve better result, choose 4 * 2
    removeBusCellHeight = removeBusHeight // 4
    removeBusCellWidth = removeBusWidth // 2
    
    # Separate the small frame by .grid() method
    # First define column
    sepBusColumn0 = Canvas(removeBusPanel, height = removeBusCellHeight, \
                           width = removeBusCellWidth)
    sepBusColumn0.grid(row = 0, column = 0)
    sepBusColumn1 = Canvas(removeBusPanel, height = removeBusCellHeight, \
                           width = removeBusCellWidth)
    sepBusColumn1.grid(row = 0, column = 1)
       
    # Then add 'BusID' Label in (1, 0) and Entry in (1, 1)
    removeBusIDL = Label(removeBusPanel, text = 'Bus ID')
    removeBusIDL.grid(row = 1, column = 0)
    removeBusBusID = StringVar(removeBusPanel)
    # Set conditions to disable
    removeBusID = Entry(removeBusPanel, textvariable = removeBusBusID, \
                        width = HOData.WWidth//2) # Shorten width here
    removeBusID.grid(row = 1, column = 1)


    # Define a small Frame to hold 2 busID and 1 lineID
    removeLinePanel = LabelFrame(removeElem, text = 'Remove a Line', \
                              height = cellHeight*4, width = cellWidth*2)
    removeLinePanel.grid(row = 12, column = 4, rowspan = 4, columnspan = 2)
    removeLinePanel.grid_propagate(0) # Force change grid size

    # Get small Frame size
    removeLinePanel.update_idletasks()
    removeLineHeight = removeLinePanel.winfo_height()
    removeLineWidth = removeLinePanel.winfo_width()

    # Since the grid can be multiplexing
    # Just separate the small Frame into 3 * 2 case
    # However to achieve better result, choose 4 * 2
    removeLineCellHeight = removeLineHeight // 4
    removeLineCellWidth = removeLineWidth // 2
    
    # Separate the small frame by .grid() method
    # First define column
    sepLineColumn0 = Canvas(removeLinePanel, height = removeLineCellHeight, \
                           width = removeLineCellWidth)
    sepLineColumn0.grid(row = 0, column = 0)
    sepLineColumn1 = Canvas(removeLinePanel, height = removeLineCellHeight, \
                           width = removeLineCellWidth)
    sepLineColumn1.grid(row = 0, column = 1)

    # Then add 1 lineID
    removeLineIDL = Label(removeLinePanel, text = 'Line ID')
    removeLineIDL.grid(row = 0, column = 0)
    removeLineLineID = StringVar(removeLinePanel)
    # Set conditions to disable
    removeLineID = Entry(removeLinePanel, textvariable = removeLineLineID, \
                      width = HOData.WWidth//2) # Shorten width here
    removeLineID.grid(row = 0, column = 1)

    # Finally add 2 busID
    removeLineBID1L = Label(removeLinePanel, text = 'Bus ID 1')
    removeLineBID1L.grid(row = 1, column = 0)
    removeLineBusID1 = StringVar(removeLinePanel)
    # Set conditions to disable
    removeLineBID1 = Entry(removeLinePanel, textvariable = removeLineBusID1, \
                        width = HOData.WWidth//2) # Shorten width here
    removeLineBID1.grid(row = 1, column = 1)

    removeLineBID2L = Label(removeLinePanel, text = 'Bus ID 2')
    removeLineBID2L.grid(row = 2, column = 0)
    removeLineBusID2 = StringVar(removeLinePanel)
    # Set conditions to disable
    removeLineBID2 = Entry(removeLinePanel, textvariable = removeLineBusID2, \
                        width = HOData.WWidth//2) # Shorten width here
    removeLineBID2.grid(row = 2, column = 1)


    sepRow16 = Canvas(removeElem, height = cellHeight, width = cellWidth)
    sepRow16.grid(row = 16, column = 0)
    sepRow17 = Canvas(removeElem, height = cellHeight, width = cellWidth)
    sepRow17.grid(row = 17, column = 0)
    sepRow18 = Canvas(removeElem, height = cellHeight, width = cellWidth)
    sepRow18.grid(row = 18, column = 0)


    # Change the states of Entrys according to the Radiobuttons
    # Currently use def in def to pass parameters to command option
    # Have to pass the list of Entrys as the function's parameter
    entryList = [removeBusID, removeLineID, removeLineBID1, removeLineBID2]
    def removeSet(removeChoice, entryList):
        if removeChoice.get() == 'BusBus':
            entryList[0].config(state = NORMAL)
            entryList[1].config(state = DISABLED)
            entryList[2].config(state = DISABLED)
            entryList[3].config(state = DISABLED)
        elif removeChoice.get() == 'LineLine':
            entryList[0].config(state = DISABLED)
            entryList[1].config(state = NORMAL)
            entryList[2].config(state = DISABLED)
            entryList[3].config(state = DISABLED)
        elif removeChoice.get() == 'LineBus':
            entryList[0].config(state = DISABLED)
            entryList[1].config(state = DISABLED)
            entryList[2].config(state = NORMAL)
            entryList[3].config(state = NORMAL)
        else:
            entryList[0].config(state = NORMAL)
            entryList[1].config(state = NORMAL)
            entryList[2].config(state = NORMAL)
            entryList[3].config(state = NORMAL)
    
    # Update the states of Entrys if events happen
    removeBusBusR.config(command = lambda: removeSet(removeChoice, entryList))
    removeLineLineR.config(command = lambda: removeSet(removeChoice, entryList))
    removeLineBusR.config(command = lambda: removeSet(removeChoice, entryList))

    # Define the event of OK button
    def removeHandle(removeChoice, entryList):
        if removeChoice.get() == 'BusBus':
            HRemoveElem(removeChoice.get(), removeBusID.get())
            return
        elif removeChoice.get() == 'LineLine':
            HRemoveElem(removeChoice.get(), removeLineID.get())
            return
        elif removeChoice.get() == 'LineBus':
            HRemoveElem(removeChoice.get(), removeLineBID1.get(), removeLineBID2.get())
            return
        else:
            pass # Do nothing

        
    removeElemOK = Button(removeElem, text = 'OK', \
                      width = HOData.WWidth, \
                          command = lambda: removeHandle(removeChoice, entryList))
    removeElemOK.grid(row = 19, column = 2, rowspan = 2)

    
    removeElemCancel = Button(removeElem, text = 'Cancel', \
                          width = HOData.WWidth, \
                              command = lambda: removeElem.destroy())
    removeElemCancel.grid(row = 19, column = 5, rowspan = 2)


    removeElem.mainloop()



def WSaveData():
    # Return the file's handler, with mode 'w'
    # However we should check if if there is result data!
    HOData.HOSaveDataHandler = filedialog.asksaveasfile()



def WAbout():
    # Tk text box give about info
    pass

def WLicense():
    # Tk text box give license info
    pass
