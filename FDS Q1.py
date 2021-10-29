c = list(map(int, input('enter roll no. who play cricket :').split()))
b = list(map(int, input('enter roll no. who play badminton :').split()))
f = list(map(int, input('enter roll no. who play football :').split()))

it=[]
cb=[]
u=[]
f_o=[]
def union(c,b,f):
    for i in c:
        if i not in u:
            u.append(i)
    for j in b:
        if j not in u:
            u.append(j)
    for k in f:
        if k not in u:
            u.append(k)

union(c,b,f)


def intersection(c,b):
    #finding intersection between cricket and badminten
    intersection=0
    global it
    for i in c:
        for j in b:
            if i==j:
                intersection+=1
                it.append(i)
    print('there are {} student who play both criket and badminton'.format(intersection))
    print('student who play both criket and badminton',it)
def cricket_badminton(c,b):
    #finding student who play either cricket or badminton but not both
    global it
    global cb

    for i in c:
        if i not in cb:
            cb.append(i)
    for j in b:
        if j not in cb:
            cb.append(j)
    for k in cb:
        if k in it:
            cb.remove(k)


    print('student who play either cricket or badminton but not both:',end=' ')
    print(cb)



def football(c,b):
    # finding student who neither play cricket nor badminton
    for p in u:
        if p not in c and p not in b:
            f_o.append(p)
    print('student who neither play cricket nor badminton',f_o)

def c_f_notB(c,b,f):
    cfo=u
    for i in u:
        if i in c and i in f:
            cfo.append(i)
    for j in cfo:
        if j in b:
            cfo.remove(j)

    print('student who play cricket and football but not badminton are',cfo)


while True:
    print('************************MAIN MENU***************************')
    print('1.list of student who play both cricket and badminton\n2.list of student who play either cricket or badminton but not both\n3.no of student who play neither cricket nor badminton\n'
          '4.no of student who play cricket and football but not badminton ')
    ch=int(input('enter choice'))
    print('###################################################################')
    print('******************************************************************')

    if ch==1:
        intersection(c, b)
        break
    if ch==2:
        cricket_badminton(c, b)
        break
    if ch==3:
        football(c,b)
        break
    if ch==4:
        c_f_notB(c, b, f)
        break















