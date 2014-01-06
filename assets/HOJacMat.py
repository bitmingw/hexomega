from numpy import matrix

# integer Size; integer nPQ, Matrix G; Matrix B; Array U

def JacMat(Size, nPQ, G, B, U):
    # Method Of Every Entry Of Jacbean Matrix
    
    f = U.real
    e = U.imag
    JacMat = zeros(Size, Size)
    
    def Hij(B, G, e, f):
        return -B*e+Gf

    def Nij(B, G, e, f):
        return G*e+Bf

    def Jij(B, G, e, f):
        return -B*f-G*e

    def Lij(B, G, e, f):
        return -B*e+Gf

    def Rij():
        return 0

    def Sij():
        return 0

    def Aii(GM, BM, eA, fA, i):
        aii = 0
        for j in range(1, len(eA)):
            aii = aii + G[i][j]*e[j]-B[i][j]*f[j]
        return aii

    def Bii(GM, BM, eA, fA, i):
        bii = 0
        for j in range(1, len(eA)):
            bii = bii + G[i][j]*f[j]+B[i][j]*e[j]
        return bii

    if isSquareM(B)==True and isSquareM(G)==True and len(B) == len(G) == G.dim == B.dim:

        # Build Jacbean Matrix
        for m in range(0, Size, 2): #H
            for n in range(0, Size, 2):
                if m==n:
                    JacMat[m][n] = Hii(B[m][m], G[m][m], e[m], f[m])
                else:
                    JacMat[m][n] = Hij(B[m][n], G[m][n], e[m], f[m])

        for m in range(0, Size, 2): #N
            for n in range(1, Size, 2):
                if m==n:
                    JacMat[m][n] = Nii(B[m][m], G[m][m], e[m], f[m])
                else:
                    JacMat[m][n] = Nij(B[m][n], G[m][n], e[m], f[m])

        for m in range(1, Size, 2): #J
            for n in range(0, nPQ*2, 2):
                if m==n:
                    JacMat[m][n] = Jii(B[m][m], G[m][m], e[m], f[m])
                else:
                    JacMat[m][n] = Jij(B[m][n], G[m][n], e[m], f[m])

        for m in range(1, Size, 2): #L
            for n in range(1, nPQ*2, 2):
                if m==n:
                    JacMat[m][n] = Lii(B[m][m], G[m][m], e[m], f[m])
                else:
                    JacMat[m][n] = Lij(B[m][n], G[m][n], e[m], f[m])

        for m in range(1, Size, 2): #R
            for n in range(1, nPQ*2, 2):
                if m==n:
                    JacMat[m][n] = Rii(f[m])
                else:
                    JacMat[m][n] = Rij()

        for m in range(1, Size, 2): #S
            for n in range(nPQ*2+1, Size, 2):
                if m==n:
                    JacMat[m][n] = Sii(e[m])
                else:
                    JacMat[m][n] = Sij()
                    
        print JacMat
        return JacMat

    else:
        print "Parameter Unmatched"
        return False

    










