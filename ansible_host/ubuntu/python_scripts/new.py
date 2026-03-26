a1=[10, 20, 'Hello']
print(a1)
print(a1[2])
print(a1[-1])
print(a1[1])
print(a1[0:2])
print(a1[0])

a1.append(15)
print(a1)

a1.append(12.8)

a1.append('all')
print(a1)

a1.append([18,'good',25.8])
print(a1)

print(a1[6][2])

a1.pop()
print(a1)

a1.pop(2)
print(a1)

a1.insert(2,'python')
print(a1)

a1.insert(4,15.9)
print(a1)

a1.remove(20)
print(a1)


a2=[90,20,40,10,50]
print(a2)

#a2.sort()
#print(a2)

#a2.reverse()
#print(a2)

a3=a2
print(a3)
print(a2)

a3[1]=100
print(a2)
print(a3)
print("\n")
a4=a2[:]
print(a2)
print(a4)

a4[1]=300
print(a2)
print(a4)

a1.extend(a4)
print(a1)

a2.append(a4)
print(a2)

a1.clear()
print(a1)

if 20 in a2:
    print("found")
else:
    print("not found")

print("sequence")
for i in a2:
   print(i)
