import math

A = [[2, -2], [3, -5]]
B = [[-2, 0], [0, 2]]
C = [[-1, 2, 0], [2, 0, 3]]
E = [[2, -1], [math.pi, math.log(2, 10)], [-2, 3]]
F = [[1, 2, 3], [2, 3, 4], [3, 5, 7]]
I = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

def create_matrix(row, col):
    return [[0 for _ in range(col)] for _ in range(row)]

def is_same_size(a, b):
    return len(a) == len(b) and len(a[0]) == len(b[0])

def add(a, b):
    if not is_same_size(a, b):
        return
    row = len(a)
    col = len(a[0])
    
    result = create_matrix(row, col)
    for i in range(row):
        for j in range(col):
            result[i][j] = a[i][j] + b[i][j]
    return result

def scale(a, scaler):
    row = len(a)
    col = len(a[0])

    result = create_matrix(row, col)

    for i in range(row):
        for j in range(col):
            result[i][j] = a[i][j] * scaler
    return result


def mul(a, b):
    a_row = len(a)
    a_col = len(a[0])
    b_row = len(b)
    b_col = len(b[0])

    if a_col != b_row: return
    result = create_matrix(a_row, b_col)

    for i in range(a_row):
        for j in range(b_col):
            sum = 0
            for k in range(b_row):
                sum += a[i][k] * b[k][j]
            result[i][j] = sum
    return result

def transpose(a):
    m = len(a)
    n = len(a[0])
    result = create_matrix(n, m)

    for i in range(m):
        for j in range(n):
            result[j][i] = a[i][j]
    
    return result

def det(a):
    if len(a) == 2:
        return (a[0][0] * a[1][1]) - (a[0][1] * a[1][0])
    elif len(a) == 3:
        m1 = [[a[1][1], a[1][2]], [a[2][1], a[2][2]]]
        m2 = [[a[1][0], a[1][2]], [a[2][0], a[2][2]]]
        m3 = [[a[1][0], a[1][1]], [a[2][0], a[2][1]]]
        return a[0][0] * det(m1) - a[0][1] * det(m2) + a[0][2] * det(m3)

def is_invertible(a): 
    return True if det(a) else False
  
def invert(a): 
    d = det(a)
    if(not d): return

    result = create_matrix(len(a), len(a[0]))
    result[0][0] = a[1][1] / d
    result[1][1] = a[0][0] / d
    result[0][1] = a[0][1] * (-1) / d
    result[1][0] = a[1][0] * (-1) / d

    return result       

### a
##a(1) A+3B
print("a(1) A+3B:\n", add(A, scale(B, 3)), "\n")

##a(2) C-B*ET
print("a(2) C-B*ET:\n", add(C, scale(mul(B, transpose(E)), -1)), "\n")

##a(3) AT
print("a(3) AT:\n" ,transpose(A), "\n")

###b
##b(1) M=A*B, N=B*A, Is M equal to N?
m = mul(A, B)
n = mul(B, A)
print("Is M equal to N?\n", m == n, "\n")

###c. Calculate P = CT*BT and Q = (B*C)T. Is P equal to Q?
p = mul(transpose(C), transpose(B))
q = transpose(mul(B, C))
print("Is P equal to Q?\n", p == q, "\n")

###d. Calculate the inverses of A and F, if the corresponding matrix is invertible.
if is_invertible(A):
    A_inverse = invert(A)
    print("Inverse of a:\n", A_inverse, "\n")
else:
    print("A is not invertible\n")

if is_invertible(F):
    F_inverse = invert(F) 
    print("Inverse of f:\n", F_inverse, "\n")
else:
    print("F is not invertible\n")

###e. Write a program to determines if matrix is a diagonal matrix. Use it to test the matrices A, B, F, I.
def is_diagonal(a):
    row = len(a)
    col = len(a[0])

    for i in range(row):
        for j in range(col):
            if i == j and not a[i][j]: return False
            if i != j and a[i][j]: return False
    return True

print("A is diagonal?\n", is_diagonal(A), "\n")
print("B is diagonal?\n", is_diagonal(B), "\n")
print("F is diagonal?\n", is_diagonal(F), "\n")
print("I is diagonal?\n", is_diagonal(I), "\n")


###f. Write a program to determines if matrix is a symmetric matrix. Use it to test
# the matrices A, B, F, I.
def is_symmetric(a):
    row = len(a)
    col = len(a[0])

    if row != col: return False

    for i in range(row): 
        for j in range(i, col):
            if i == j: continue
            if a[i][j] != a[j][i]: return False

    return True

print("A is symmetric?\n", is_symmetric(A), "\n")
print("B is symmetric?\n", is_symmetric(B), "\n")
print("F is symmetric?\n", is_symmetric(F), "\n")
print("I is symmetric?\n", is_symmetric(I), "\n")
