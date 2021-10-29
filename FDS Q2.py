m=list(map(int,input('enter marks').split()))
#average
sum=0
for i in m:
    sum+=i

average=sum/len(m)

#higest and lowest
h=0
for i in m:
    if i>h:
        h=i
print('higest marks:',h)


l = m[0]
for i in m:
    if i<l:
        if i!=-1:
            l = i
print('lowest marks:',l)


# absent
count=0
for i in m:
    if i==-1:
        count+=1
print('there are {} student who are absent'.format(count))

#higest frequency
max = 0
e = m[0]
for i in m:
    freq = m.count(i)
    if freq > max:
        max = freq
        e = i
print('higest frequency marks:',e,end='------->>>')
print('it is appered {} times'.format(m.count(e)))