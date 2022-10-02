
# Rebecca Smith
from collections import namedtuple

V3 = namedtuple('Point3', ['x', 'y', 'z'])

def matriz(m1, m2):
    result=[]
    for i in range(len(m1)):
        row = []
        for j in range(len(m2[0])):
            row.append(0)

        for j in range(len(m2[0])):
            for k in range(len(m2)):
                row[j] += ((m1[i][k] * m2[k][j]).real)
        
        result.append(row)
    
    
    return result

def cruz(X,Y):
    x = X[1]*Y[2] - Y[1]*X[2]
    y = X[2]*Y[0] - Y[2]*X[0]
    z = X[0]*Y[1] - Y[0]*X[1]
    # lista=[x.real,y.real,z.real]
    return V3((x.real),(y.real),(z.real))


def matrizporvector(matriz,vector):
    result = []
    for i in range(len(matriz)): #this loops through columns of the matrix
        total = 0
        for j in range(len(vector)): #this loops through vector coordinates & rows of matrix
            total += ((vector[j] * matriz[i][j]).real)
        result.append(total)
    return result

def transposeMatrix(m):
    return map(list,zip(*m))

def dot(a,b):
    return sum(x*y for x, y in zip(a, b))
    
def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def determinante(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*determinante(getMatrixMinor(m,0,c))
    return determinant

def inversa(m):
    determinant = determinante(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * determinante(minor))
        cofactors.append(cofactorRow)
    cofactors = list(transposeMatrix(cofactors))
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors

def subtract(v1,v2):
    result = [i-j for i, j in zip(v1,v2)]
    return result

def add(v1,v2):
    result = [i+j for i, j in zip(v1,v2)]
    return result

def multiply(v1,v2):
    result = [i*j for i, j in zip(v1,v2)]
    return result

def magnitud(v):
    b=0
    a=0
    for i in v:
        a=i**2
        b+=a
    b=b**0.5
    return b

def normal(v):
    final=[]
    h=magnitud(v)
    for i in v:
        l=i/h
        final.append(l)
    return final

def listas(l1,l2):
    Result = []
    for i1, i2 in zip(l1, l2):
        Result.append(i1*i2)
    return Result