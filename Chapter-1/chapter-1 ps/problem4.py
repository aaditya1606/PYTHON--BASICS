# listing directory with the help of os modules
import os
directory_path='/'
contents=os.listdir(directory_path)
for items in contents:
    print(items)