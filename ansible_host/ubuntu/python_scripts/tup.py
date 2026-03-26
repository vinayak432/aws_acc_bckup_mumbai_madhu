t1=(15, 20, 25, "welcome")
print(t1)
print(t1[0])
print(t1[-1])
print(t1[-3])
print(t1)
# to concatenate 30
t1=t1+(30,)
print(t1)

# to concatenate 20
t1=t1+(20,)
print(t1)

#to count 20 and disp index of 20
print(t1.count(20))
print(t1.index(20))

#convert tuple into list
t1=list(t1)
print(t1)

#insert element to list t1 and convert into tuple
t1.insert(1,15)
print(t1)

t1=tuple(t1)
print(t1)
