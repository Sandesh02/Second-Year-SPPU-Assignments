#for 3*3 matrix
print('enter elements of matrix one')
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
print('enter elements of second matrix')
d=list(map(int,input().split()))
e=list(map(int,input().split()))
f=list(map(int,input().split()))
m1=[a,b,c]
m2=[d,e,f]
m3=[[0,0,0],[0,0,0],[0,0,0]]
def addition(m1,m2):
    for i in range(3):
        for j in range(3):
            m3[i][j]=m1[i][j]+m2[i][j]
    print('addition matrix')
    print(m3)
addition(m1,m2)

def substraction(m1,m2):
    for i in range(3):
        for j in range(3):
            m3[i][j]=m1[i][j]-m2[i][j]
    print('subtraction matrix')
    print(m3)
substraction(m1,m2)

def transpose(m1):
    for i in range(3):
        for j in range(3):
            m3[i][j]=m1[j][i]
    print('transpose of m1')
    print(m3)
transpose(m1)