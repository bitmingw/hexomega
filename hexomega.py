#!/usr/bin/env python3


#### Some info here...

from tkinter import *

# import files in subfolder
import sys
import os
subpath = os.getcwd() + os.sep + 'assets'
sys.path.append(subpath)
import HOData
from HODisp import *


# Some UI function are defined here for convenience
def WExit():
    # Kill the program
    # Ask user if they want to quit without saving data
    # If true remove all the data
    if HOData.HOModified == 0:
        HOData.HOReset()
        hexomega.destroy()
        sys.exit(0)
    else:
        wExit = messagebox.askokcancel(title = 'Exit', \
                                       message = 'Are you sure to reset?')
        if wExit > 0:
            HOData.HOReset()
            hexomega.destroy()
            sys.exit(0)


            
# Construct GUI, use mainloop() to maintain
# Define master window here
hexomega = Tk()

# Get the screen info

HOData.ScrTotalW = hexomega.winfo_screenwidth()
HOData.ScrTotalH = hexomega.winfo_screenheight()
HOData.WSegWL = HOData.ScrTotalW // 6
HOData.WSegWS = HOData.ScrTotalW // 4
HOData.WSegH = HOData.ScrTotalH // 6

# If the screen is wider, use narrow setting
# Otherwise use normal setting
# Store the setting so other windows can use that
if (HOData.ScrTotalW / HOData.ScrTotalH) >= 1.6:
    HOData.WSegW = HOData.WSegWS
    hexomega.geometry(str(HOData.WSegW*2)+'x'+str(HOData.WSegH*4)+'+' \
                      +str(HOData.WSegW)+'+'+str(HOData.WSegH))
    
    hexomega.update_idletasks() # update info
    HOData.WGeometry = hexomega.winfo_geometry()
else:
    HOData.WSegW = HOData.WSegWL
    hexomega.geometry(str(HOData.WSegW*4)+'x'+str(HOData.WSegH*4)+'+' \
                      +str(HOData.WSegW)+'+'+str(HOData.WSegH))
    
    hexomega.update_idletasks() # update info
    HOData.WGeometry = hexomega.winfo_geometry()

hexomega.title('Hexomega - Power System Analysis')



# Define menu here
menubar = Menu()

fileMenu = Menu(menubar)
fileMenu.add_command(label = 'Reset', command = WReset)
fileMenu.add_command(label = 'Open', command = WOpen)
fileMenu.add_command(label = 'Save', command = WSave)
fileMenu.add_command(label = 'Exit', command = WExit)
menubar.add_cascade(label = 'File', menu = fileMenu)

editMenu = Menu(menubar)
editMenu.add_command(label = 'Add Generator', command = WAddGen)
editMenu.add_command(label = 'Add Solved Line', command = WAddSolvedLine)
editMenu.add_command(label = 'Add Unsolved Line', command = WAddUnsolvedLine)
editMenu.add_command(label = 'Add Transformer', command = WAddTrans)
editMenu.add_command(label = 'Add Load', command = WAddLoad)
editMenu.add_command(label = 'Add Compensator', command = WAddCompensator)
editMenu.add_separator()
editMenu.add_command(label = 'Modify Component', command = WModElem)
editMenu.add_separator()
editMenu.add_command(label = 'Remove Component', command = WRemoveElem)
menubar.add_cascade(label = 'Edit', menu = editMenu)

runMenu = Menu(menubar)
runMenu.add_command(label = 'Calculate System')
runMenu.add_command(label = 'Save Data', command = WSaveData)
menubar.add_cascade(label = 'Run', menu = runMenu)

aboutMenu = Menu(menubar)
aboutMenu.add_command(label = 'About Hexomega', command = WAbout)
aboutMenu.add_command(label = 'License', command = WLicense)
menubar.add_cascade(label = 'About', menu = aboutMenu)

# Draw menu on the window
hexomega.config(menu = menubar)

    
# Draw the window and waiting for events
hexomega.mainloop()

    
