with open("1.txt", 'r') as gh:
    content=gh.read()
    print(content)
    print(type(content))

with open("1.txt", 'r') as fh:
    for line in fh:
        print(line)
        print(type(line))

with open("1.txt", 'r') as fh:
    content=fh.readlines()
    print(content)
