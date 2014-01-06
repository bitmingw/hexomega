#This is part of HexOmega Project, calculate Jacobian Matrix in algorithm
#Created in Unknown Time
#Major updated in 20:55 Dec 10th 2013
#Last updated in 23:57 Dec 13th 2013
#Basic Test passed, which means it return the right FORMAT but value not promissed

### Notice for developer, the problem of SINGULAR MATRIX still remain
### UNSOLVED; it is possible due to the inproper test case
###

from numpy import *
from HOAsserts import *

# integer Size; integer nPQ, Matrix G; Matrix B; Array U
#

def getJacMat(size, nPQ, G, B, f, e):
    """Method Of Every Entry Of Jacbean Matrix;
    Interger size, nPQ, Matrix G, B, Array f, e"""
    #f = U.real
    #e = U.imag

    HNJL = zeros(shape = (2, 2))
    HNRS = zeros(shape = (2, 2))

    #Function of Every Entry
    def Hij(B, G, e, f):
        return -B*e+G*f

    def Nij(B, G, e, f):
        return G*e+B*f

    def Jij(B, G, e, f):
        return -B*f-G*e

    def Lij(B, G, e, f):
        return -B*e+G*f

    def Rij():
        return 0

    def Sij():
        return 0

    #abbr MPS
    def GetMinursPartSum(GM, BM, eA, fA, i):
        aii = 0
        for j in range(0, size):
            if i==j:
                continue
            else:
                aii = aii + G[i,j]*e[j]-B[i,j]*f[j]
        return aii

    #abbr PPS
    def GetPlusPartSum(GM, BM, eA, fA, i):
        bii = 0
        for j in range(0, size):
            if i==j:
                continue
            else:
                bii = bii + G[i,j]*f[j]+B[i,j]*e[j]
        return bii

    def Hii(G, f, PPS):
        return 2*G*f+PPS

    def Nii(G, e, MPS):
        return 2*G*e+MPS

    def Jii(B, f, MPS):
        return -2*B*f+MPS

    def Lii(B, e, PPS):
        return -2*B*e-PPS

    def Rii(f):
        return 2*f

    def Sii(e):
        return 2*e

    H = 0; N = 0; J = 0; L = 0; R = 0; S = 0

    #First loop to get every entry of PQ bus
    for n in range(0, nPQ):
        for m in range(0, size):
            if m==n:
                H = Hii(G[m,n], f[m], GetPlusPartSum(G, B, e, f, m))
                N = Nii(G[m,n], e[m], GetMinursPartSum(G, B, e, f, m))
                J = Jii(B[m,n], f[m], GetMinursPartSum(G, B, e, f, m))
                L = Lii(B[m,n], e[m], GetPlusPartSum(G, B, e, f, m))
            elif m!=n:
                H = Hij(B[m,n], G[m,n], e[m], f[m])
                N = Nij(B[m,n], G[m,n], e[m], f[m])
                J = Jij(B[m,n], G[m,n], e[m], f[m])
                L = Lij(B[m,n], G[m,n], e[m], f[m])
            else:
                print "Jacbean Matrix Error In PQ"

            HNJL[0][0] = H; #print H, m, n; print "H"
            HNJL[0][1] = N; #print N, m, n; print "N"
            HNJL[1][0] = J; #print J, m, n; print "J"
            HNJL[1][1] = L; #print L, m, n; print "L"

            if m==0:
                JacRow = HNJL
            else:
                JacRow = hstack((JacRow,HNJL))

        if n==0:
            JacMat = JacRow
        else:
            JacMat = vstack((JacMat, JacRow))

    #Second loop to get every entry of PV bus
    for n in range(nPQ, size):
        for m in range(0, size):
            if m==n:
                H = Hii(G[m,n], f[m], GetPlusPartSum(G, B, e, f, m))
                N = Nii(G[m,n], e[m], GetMinursPartSum(G, B, e, f, m))
                R = Rii(f[m])
                S = Sii(e[m])
            elif m!=n:
                H = Hij(B[m,n], G[m,n], e[m], f[m])
                N = Nij(B[m,n], G[m,n], e[m], f[m])
                R = Rij()
                S = Sij()
            else:
                print "Jacbean Matrix Error In PV"

            HNRS[0][0] = H; #print H, m, n; print "H"
            HNRS[0][1] = N; #print N, m, n; print "N"
            HNRS[1][0] = R; #print R, m, n; print "R"
            HNRS[1][1] = S; #print S, m, n; print "S"

            if m==0:
                JacRow = HNRS
            else:
                JacRow = hstack((JacRow,HNRS))

        JacMat = vstack((JacMat, JacRow))

    #print JacMat
    return JacMat

def getDeltaPQPU(size, G, B, f, e, P, Q, U):

    def GetPSP(GM, BM, eA, fA, i):
        PSP = 0
        for j in range(0, size):
            PSP = PSP + e[i]*(G[i,j]*e[j]-B[i,j]*f[j])\
                  + f[i]*(G[i,j]*f[j]+B[i,j]*e[j])
        return PSP

    def GetPSQ(GM, BM, eA, fA, i):
        PSQ = 0
        for j in range(0, size):
            PSQ = PSQ + f[i]*(G[i,j]*e[j]-B[i,j]*f[j])\
                  - e[i]*(G[i,j]*f[j]+B[i,j]*e[j])
        return PSQ

    def GetUsq(e,f):
        return pow(e,2)+pow(f,2)

    def GetDeltaP(G, B, e, f, P):
        deltaP = zeros(shape=len(P))
        for i in range(0, len(P)):
            deltaP[i] = P[i] - GetPSP(G, B, e, f, i)
        return deltaP

    def GetDeltaQ(G, B, e, f, Q):
        deltaQ = zeros(shape=len(Q))
        for i in range(0, len(Q)):
            deltaQ[i] = Q[i] - GetPSQ(G, B, e, f, i)
        return deltaQ

    def GetDeltaU(G, B, e, f, U):
        deltaU = zeros(shape=len(U))
        for i in range(0, len(U)):
            deltaU = pow(abs(U[i]),2) - GetUsq(e[i],f[i])
            #print "deltaU="
            #print deltaU
        return deltaU

    """Notice PQ is always in front of PU"""
    if (len(P)==len(Q)+len(U)):
        deltaPQPU = zeros(shape = 2*size)
        #print len(deltaPQPU)
        deltaP = GetDeltaP(G, B, e, f, P)
        #print GetDeltaQ(G, B, e, f, Q)
        #print GetDeltaU(G, B, e, f, U)
        deltaQU = hstack((GetDeltaQ(G, B, e, f, Q), GetDeltaU(G, B, e, f, U)))
        #print "deltaQU"
        #print deltaQU
        #print len(deltaQU)
        #print size
        for k in range(0, size):
            #print k
            #print 2*k+1
            deltaPQPU[k] = deltaP[k]
            deltaPQPU[2*k+1] = deltaQU[k]

##        for k in range(1, size, 2):
##            if k < 2*len(Q):
##                print k
##                print len(Q)
##                print PQPU.shape
##                print PQPU
##                PQPU[2*k+1] = Q[k] - GetPSQ(G, B, e, f, k)
##            elif k >= 2*len(Q):
##                PQPU[i+1+len(Q)] = pow(U[i],2) - GetUsq(e[i],f[i])
##            else:
##                print "Error in Get P Q P U Array"
    else:
        print len(P), len(Q), len(U)
        print "Argument Error: P == Q + U should be saitisfied"

    return deltaPQPU

def getIniFE(f, e, size):
    FE = zeros(shape = 2*size)
    for i in range(0,size,2):
        FE[i] = f[i]
        FE[i+1] = e[i]
    return FE

def getIniPQPU(size, P, Q, U):
    PQPU = zeros(shape = 2*size)
    QU = hstack((Q, U))
    for k in range(0, size):
        #print k
        #print 2*k+1
        PQPU[k] = P[k]
        #print QU[k]
        PQPU[2*k+1] = QU[k]
    return PQPU

def getInvJac(JacMat):
    JacMat = matrix(JacMat)
    if linalg.det(JacMat) == 0:
        print "Singular Matrix, No Inverse"
        #print JacMat
    else:
        return JacMat.getI()

def getDeltaFE(InvJac, DeltaPQPU):
    print """Get Delta f and Delta e in Array"""
    print DeltaPQPU
    print InvJac
    return matrix(InvJac)*matrix(rowToColumn(DeltaPQPU))

##def getDeltaPQPU(Jac, DeltaFE):
##    return Jac*DeltaFE

def endLoop(DeltaFE, eps):
    counter = 0
    for i in range(0, len(DeltaFE)):
        if(DeltaFE[i]<eps):
            counter += 1
    if(counter >= len(DeltaFE)):
        return True
    return False

def upDateFE(DeltaFE, FE, size):
    summation = zeros(shape = 2*size)
    for i in range(0, len(FE)):
        summation[i] = FE[i] + DeltaFE[i,0]
    return summation

def upDatePQPU(DeltaPQPU, PQPU, size):
    summation = zeros(shape = 2*size)
    print PQPU
    for i in range(0, len(PQPU)):
        summation[i] = PQPU[i] + DeltaPQPU[i]
    return summation

def FEtoF(FE):
    """Separate f from FE vector"""
    f = zeros(shape = len(FE)/2)
    for i in range(0, len(FE)/2):
        f[i] = FE[2*i]
    return f

def FEtoE(FE):
    """Separate e from FE vector"""
    e = zeros(shape = len(FE)/2)
    for i in range(0, len(FE)/2):
        e[i] = FE[2*i+1]
    return e

def Recursion(size, nPQ, G, B, f, e, P, Q, U, eps):


    PQPU = getIniPQPU(size, P, Q, U)
    #print "PQPU"
    #print PQPU
    FE = getIniFE(f, e, size)

    while True:
        JacMat = getJacMat(size, nPQ, G, B, f, e)
        InvJac = getInvJac(JacMat)
        DeltaPQPU = getDeltaPQPU(size, G, B, f, e, P, Q, U)
        DeltaFE = getDeltaFE(InvJac, DeltaPQPU)
        print "DeltaFE"
        print DeltaFE
        FE = upDateFE(DeltaFE,FE,size)
        PQPU = upDatePQPU(DeltaPQPU,PQPU,size)
        f = FEtoF(FE)
        e = FEtoE(FE)
        if endLoop(DeltaFE, eps):
            return FE





#Test From Textbook ISBN 978-7-5083-5542-9 Page_135 eg4-3
G = matrix([[6.2500, -5.000, -1.250, 1.0000, 0.0000],
             [-5.000, 10.834, -1.667, -1.667, -2.500],
             [-1.250, -1.667, 12.917, -10.00, 1.0000],
             [0.0000, -1.667, 10.000, 12.917, -1.250],
             [1.0000, -2.500, 0.0000, -1.250, 3.7500]])

B = matrix([[-18.75, 15.000, -3.750, 0.0000, 0.0000],
             [15.000, -32.50, 5.0000, 5.0000, 7.5000],
             [3.7500, 5.0000, -38.75, 30.000, 0.0000],
             [1.0000, 5.0000, 30.000, -38.75, 3.7500],
             [0.0000, 7.5000, 0.0000, 3.7500, 11.250]])

U = [1.06+0.1j, 1.00+0.1j, 1.00+0.1j, 1.00+0.1j, 1.00+0.1j]
f = [1.06, 1, 1, 1, 1 ]
e = [0, 0, 0, 0, 0]
P = [1.3, 0.2, -0.45, -0.40, -0.60]
Q = [0.24, 0.2, -0.45, -0.4 -0.6]
U2 = [1.06+0.1j]



G1 = matrix([[6.2500, -5.000, -1.250, 1.0000],
             [-5.000, 10.834, -1.667, -1.667],
             [-1.250, -1.667, 12.917, -10.00],
             [0.0000, -1.667, 10.000, 12.917]])

B1 = matrix([[-18.75, 15.000, -3.750, 1.0000],
             [15.000, -32.50, 5.0000, 5.0000],
             [3.7500, 5.0000, -38.75, 30.000],
             [1.0000, 5.0000, 30.000, -38.75]])

U = [1.06+0.1j, 1, 1, 1]
f1 = [1.06, 1, 1, 1]
e1 = [0, 0, 0, 0]
P1 = [1.3, 0.2, -0.45, -0.40]
Q1 = [0.24, 0.2]
U1 = [1.06+0.1j, 1]

print Recursion(5, 4, G, B, f, e, P, Q, U2, 0.1)
#print Recursion(4, 2, G1, B1, f1, e1, P1, Q1, U1, 0.01)
#print Recursion(5, 5, G, B, f, e, P, Q, U, 0.01)




