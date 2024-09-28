import math

a = [[2, -2], [3, -5]]
b = [[-2, 0], [0, 2]]
c = [[-1, 2, 0], [2, 0, 3]]
e = [[2, -1], [math.pi, math.log(2)], [-2, 3]]
f = [[1, 2, 3], [2, 3, 4], [3, 5, 7]]
i = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

def add(a, b, result):
    for i in range(0, len(a)):
        for j in range(0, len(a[0])):
            result[i][j] = a[i][j] + b[i][j]

def scale(a, scaler, result):
    for i in range(0, len(a)):
        for j in range(0, len(a[0])):
            result[i][j] = a[i][j] * scaler

def mul(a, b, result):
    a_row = len(a)
    a_col = len(a[0])
    b_row = len(b)
    b_col = len(b[0])

    if a_col != b_row: return

    for i in range(0, a_row):
        for j in range(0, b_col):
            sum = 0
            for k in range(0, b_row):
                sum += a[i][k] + b[k][j]
            result[i][j] = sum
            


c = [[0] * 2, [0] * 2]
print(c)
add(a, b, c)
print(c)
