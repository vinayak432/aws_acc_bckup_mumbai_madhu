import subprocess

commands=['ls -l', 'pwd', 'touch file1']

for cmd in commands:
    result=subprocess.run(cmd, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(result.stdout)
    print(result.stderr, end=' ')
