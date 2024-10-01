import math

a = [[2, -2], [3, -5]]
b = [[-2, 0], [0, 2]]
c = [[-1, 2, 0], [2, 0, 3]]
e = [[2, -1], [math.pi, math.log(2, 10)], [-2, 3]]
f = [[1, 2, 3], [2, 3, 4], [3, 5, 7]]
i = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

def create_matrix(row, col):
    return [[0 for _ in range(col)] for _ in range(row)]

def is_same_size(a, b):
    return len(a) == len(b) and len(a[0]) == len(b[0])

def add(a, b):
    if not is_same_size(a, b):
        return
    
    result = create_matrix(len(a), len(a[0]))
    for i in range(0, len(a)):
        for j in range(0, len(a[0])):
            result[i][j] = a[i][j] + b[i][j]
    return result

def scale(a, scaler):
    result = create_matrix(len(a), len(a[0]))
    for i in range(0, len(a)):
        for j in range(0, len(a[0])):
            result[i][j] = a[i][j] * scaler
    return result


def mul(a, b):
    a_row = len(a)
    a_col = len(a[0])
    b_row = len(b)
    b_col = len(b[0])

    result = create_matrix(a_row, b_col)

    if a_col != b_row: return

    for i in range(0, a_row):
        for j in range(0, b_col):
            sum = 0
            for k in range(0, b_row):
                sum += a[i][k] + b[k][j]
            result[i][j] = sum ##TODO: verify logic
    return result

def transpose(a):
    m = len(a)
    n = len(a[0])
    result = create_matrix(n, m)

    for i in range(0, m):
        for j in range(0, n):
            result[j][i] = a[i][j]
    
    return result

def det(a):
    return (a[0][0] * a[1][1]) - (a[0][1] * a[1][0])

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
print("A+3B:\n", add(a, scale(b, 3)))

##a(2) C-B*ET
print("C-B*ET:\n", add(c, scale(mul(b, transpose(e)), -1)))

##a(3) AT
print("AT:\n" ,transpose(a))

###b
##b(1) M=A*B, N=B*A, Is M equal to N?
m = mul(a, b)
n = mul(b, a)
print("Is M equal to N?\n", m == n)

###c. Calculate P = CT*BT and Q = (B*C)T. Is P equal to Q?
p = mul(transpose(c), transpose(b))
q = transpose(mul(b, c))
print("Is P equal to Q?\n", p == q)

###d. Calculate the inverses of A and F, if the corresponding matrix is invertible.
a_inverse = invert(a)
f_inverse = invert(f) ##TODO: is f invertible???
print("Inverse of a:\n", a_inverse)
print("Inverse of f:\n", f_inverse)

###e. Write a program to determines if matrix is a diagonal matrix. Use it to test the matrices A, B, F, I.
def is_diagonal(a):
    for i in range(0, len(a)):
        for j in range(0, len(a[0])):
            if i == j and not a[i][j]: return False
            if i != j and a[i][j]: return False
    return True

print("A is diagonal?\n", is_diagonal(a))
print("B is diagonal?\n", is_diagonal(b))
print("F is diagonal?\n", is_diagonal(f))
print("I is diagonal?\n", is_diagonal(i))


###f. Write a program to determines if matrix is a symmetric matrix. Use it to test
# the matrices A, B, F, I.
def is_symmetric(a):
    if len(a) != len(a[0]): return False

    for i in range(len(a)): ## TODO: check logic
        for j in range(i, len(a[0])):
            if i == j: continue
            if a[i][j] != a[j][i]: return False

    return True

print("A is symmetric?\n", is_symmetric(a))
print("B is symmetric?\n", is_symmetric(b))
print("F is symmetric?\n", is_symmetric(f))
print("I is symmetric?\n", is_symmetric(i))
