# all operations are for 3*3 matrix
#name: sandesh santosh pabitwar #comp1 #prn:f20111040
print('enter elements of matrix one')
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
print('enter elements of second matrix')
d = list(map(int, input().split()))
e = list(map(int, input().split()))
f = list(map(int, input().split()))
m1 = [a, b, c]
m2 = [d, e, f]
m3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # empty matrix to hold output


def addition(m1, m2):
    for i in range(3):
        for j in range(3):
            m3[i][j] = m1[i][j] + m2[i][j]

    print('addition matrix')
    print(m3)


addition(m1, m2)


def substraction(m1, m2):
    for i in range(3):
        for j in range(3):
            m3[i][j] = m1[i][j] - m2[i][j]

    print('subtraction matrix')
    print(m3)
substraction(m1, m2)


def transpose(m1):
    for i in range(3):
        for j in range(3):
            m3[i][j] = m1[j][i]

    print('transpose of m1')
    print(m3)


transpose(m1)


def multiplication(m1, m2):
    # iterating by row of m1
    for i in range(3):

        # iterating by column by m2
        for j in range(3):

            # iterating by rows of m2
            for k in range(3):
                m3[i][j] += m1[i][k] * m2[k][j]
    print('multiplication of two matrix is:')
    print(m3)

multiplication(m1, m2)
