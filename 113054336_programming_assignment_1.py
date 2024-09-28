import math

a = [[2, -2], [3, -5]]
b = [[-2, 0], [0, 2]]
c = [[-1, 2, 0], [2, 0, 3]]
e = [[2, -1], [math.pi, math.log(2, 10)], [-2, 3]]
f = [[1, 2, 3], [2, 3, 4], [3, 5, 7]]
i = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

def create_matrix(row, col):
    return [[0 for _ in range(col)] for _ in range(row)]

def add(a, b):
    result = create_matrix(len(a), len(b))
    for i in range(0, len(a)):
        for j in range(0, len(a[0])):
            result[i][j] = a[i][j] + b[i][j]
    return result

def scale(a, scaler):
    result = create_matrix(len(a), len(a[0]))
    for i in range(0, len(a)):
        for j in range(0, len(a[0])):
            result[i][j] = a[i][j] * scaler

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

def is_diagonal(a):
    for i in range(0, len(a)):
        for j in range(0, len(a[0])):
            if i == j and not a[i][j]: return False
            if i != j and a[i][j]: return False
    return True

print(is_diagonal(b))

def is_symmetric(a):
    if len(a) != len(a[0]): return False

    for i in range(len(a)): ## TODO: check logic
        for j in range(i, len(a[0])):
            if i == j: continue
            if a[i][j] != a[j][i]: return False

    return True



