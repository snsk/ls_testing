import os

# Functional_SpecConfirmance_BasicBehavior

new_dir_path = 'Functional_SpecConfirmance_BasicBehavior'

if not os.path.exists(new_dir_path):
    os.makedirs(new_dir_path)

file_list = ['aaa', 'bbb', 'ccc']

for file_name in file_list:
    f = open('./Functional_SpecConfirmance_BasicBehavior/'+file_name, 'w')
    f.close()
