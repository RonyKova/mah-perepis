with open ('Perepis.txt','r') as f:
    names = f.read().splitlines()

k = 0

for i in names:
        surname,name,patron,date = i.split()
        if (int((date[6:])) >= 1978):
            print(str(surname+' '+date ))
            k = k+1

print()
print('число жителей - ', k)

a = 1961
b = 1979

print()
print()

for i in names:
        surname,name,patron,date = i.split()
        if (int(date[6:])) in (list(range(a,b))):
            print (i)





