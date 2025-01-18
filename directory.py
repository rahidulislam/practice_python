import os
cwd = os.getcwd()
print(cwd)
os.chdir('./practice_python/class/')
cwd = os.getcwd()
print(cwd)
dir = os.path.join('/media/rahidulislam/Personal/Work/practice_python/practice_python','class')
print(dir)
if os.path.exists(dir) or os.path.isdir(dir):
    print(f"The {dir} is a directory")

dir2 = os.path.join('/media/rahidulislam/Personal/Work/practice_python/practice_python', 'python_directory')
if not os.path.exists(dir2):
    os.mkdir(dir2)
    print(f"The {dir2} is created")

oldpath = os.path.join('/media/rahidulislam/Personal/Work/practice_python/practice_python', 'python_directory')
newpath = os.path.join('/media/rahidulislam/Personal/Work/practice_python/practice_python', 'python_directory2')
if os.path.exists(oldpath) and not os.path.exists(newpath):
    os.rename(oldpath, newpath)
    print(f"The {newpath} is renamed")

dir3 = os.path.join('/media/rahidulislam/Personal/Work/practice_python/practice_python', 'python_directory2')
if os.path.exists(dir3):
    os.rmdir(dir3)
    print(f"The {dir3} is removed")

path = '/media/rahidulislam/Personal/Work/practice_python/'
for root, dirs, files in os.walk(path):
    print(f"{root} has {len(files)} files")

csv_files =[]
for dirpath,dirnames,filenames in os.walk(path):
    for filename in filenames:
        if filename.endswith('.csv'):
            csv_files.append(os.path.join(dirpath,filename))

for csv_file in csv_files:
    print(csv_file)