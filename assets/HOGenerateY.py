from numpy import *

#def HOGenerateY():

def initY():
    return matrix(zeros(shape=(1,1)), dtype = complex)

def addBus(Y, ID, yArray):
    bound = ID + 1
    if ID == 0:
        Y[0,0] = yArray[0]
    else:
        #Expand Dimision
        column = zeros(shape = (Y.shape[0], 1))
        row = zeros(shape = (1, Y.shape[1]+1))
        Y = hstack((Y, column))
        Y = vstack((Y, row))

        for i in range(0, bound):
            if(i == ID):
                Y[ID,ID] = yArray[i]
            elif(i != ID):
                Y[ID,i] = -yArray[i]
                Y[i,ID] = -yArray[i]
            else:
                print "Error: Size Not Match in Building Y (BUS)"
                
            Y[i,i] = Y[i,i] + yArray[i]
    print Y
    return Y

def addLine(Y, size, busID1, busID2, y12):
    for i in range(0, size):
        for j in range(0, size):
            if(i==j):
                Y[i,j] = Y[i,j] + y12
            elif(i!=j):
                Y[i,j] = Y[i,j] - y12
            else:
                print "Error: Size Not Match in Building Y (LINE)"
    return Y
    
##Y1 = matrix([[6.2500 + 1j, -5.000 + 1j, -1.250 + 1j, 1.0000 + 1j],
##             [-5.000 + 1j, 10.834 + 1j, -1.667 + 1j, -1.667 + 1j],
##             [-1.250 + 1j, -1.667 + 1j, 12.917 + 1j, -10.00 + 1j],
##             [0.0000 + 1j, -1.667 + 1j, 10.000 + 1j, 12.917 + 1j]])
##
##print Y1

