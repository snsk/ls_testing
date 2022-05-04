import os

file_list = ['aaa', 'bbb', 'ccc']

for file_name in file_list:
    f = open(file_name, 'w')
    f.close()