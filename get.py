######### code to get list of directory ##############

import os

path = 'path'

files = os.listdir(path)
count =0
for f in files:
    count = count +1
    print(count)
#print(count)