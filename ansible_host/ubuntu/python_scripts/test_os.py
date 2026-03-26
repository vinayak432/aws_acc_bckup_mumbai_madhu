import os
#help(os)
#print(dir(os))
print(os.getcwd())
#os.chdir("/home/ubuntu/")
print(os.getcwd())
print(os.listdir())
os.makedirs("dir1",exist_ok=True)
print(os.listdir())
os.makedirs("/home/ubuntu/dir1",exist_ok=True)
print(os.listdir("/home/ubuntu/"))
if os.path.isfile("/home/ubuntu/python_scripts/test_os.py"):
    print("file exists")
else:
    print("file doesnot exist")

#to check directory exists in the curr_path or not
if os.path.exists("dir1"):
    print("directory exists")
else:
    print("directory doesnot exists")

for curr_pa,dirs,files in os.walk("/home"):
    print(curr_pa,dirs,files)

print(os.path.basename("/home/ubuntu/tmp/1,txt"))

print(os.path.basename("/root/opt"))
