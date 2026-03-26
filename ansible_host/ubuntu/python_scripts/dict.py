d1={}
print(d1)

d1={"name":'vinayak','id':369368,'place':"BNG"}
print(d1)
print(d1["id"])
print(d1["name"])
print(d1["place"])

d1.update({"skills":["linux","jenkins","ansible","git"]})
print(d1)

print(d1["skills"][2])
print(d1["skills"][3])
print(d1["skills"][0])

d1.update({"loc":{"workplace":"Bengaluru","native":"dvg"}})
print(d1)

print(d1["loc"]["native"])

print("keys and values")
for k, v in d1.items():
    print(k, v)

print("***keys")
for w in d1.keys():
    print(w)

print("*****values")
for i in d1.values():
    print(i)

if "vinayak" in d1.values():
    print("found")
else:
    print("not found")

if "vinayak" in d1:
    print("found")
else:
    print("not found")

print(d1)
d1.popitem()
print(d1)

print(d1)
d1.pop("id")
print(d1)

#copying
d2=d1
print(d2)
