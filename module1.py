f = open ('Perepis.txt','r')
names = f.read().splitlines()

surname = [0 for i in range (31)]
name = [0 for i in range (31)]
patron =  [0 for i in range (31)]
date  =   [0 for i in range (31)]
k = 0
ms = []


for i in range(31):
        surname[i],name[i],patron[i],date[i] = names[i].split()
        if (int((date[i][6:])) >= 1978):
            ms.append(str(surname[i]+' '+date[i]))

            k = k+1

print('\n'.join(ms))
print()
print('число жителей - ', k)

a = 1961
b = 1979

print()
print()

for i in range(31):
        surname[i],name[i],patron[i],date[i] = names[i].split()
        if (int(date[i][6:])) in (list(range(a,b))):
            print (names[i])

f.close()

