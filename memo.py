import os
import subprocess, sys
import combi_testware
import string
import random
import math

char_array = list(string.printable)
char_array.remove('/')

filename_length_seed = math.floor(random.random()*255)
file_count_seed = math.floor(random.random()*10000)

def gen_random_file_name():
    filename = ''
    for i in range(filename_length_seed):
        filename = filename + random.choice(char_array)
    return filename

print(gen_random_file_name())

new_dir_path = 'HierarchyFuzzing'

if not os.path.exists(new_dir_path):
    os.makedirs(new_dir_path)

for i in range(file_count_seed):
    f = open('./'+new_dir_path+'/'+gen_random_file_name(), 'w')
    f.close()

print(str(file_count_seed) + 'files generated.')

exit()

# generate combination test case and expected result

new_dir_path =  'Functional_SpecConfirmance_Arguments_Combination_WhichFilesAreListed'
if new_dir_path in os.getcwd(): #this "given" will call many times in this feature.
    pass
else:
    os.chdir('./'+new_dir_path+'/')

ret = subprocess.run([
    "ls", "-R"
    ], capture_output=True)
print(ret.stdout)


ret = combi_testware.run_ls_command(combi_testware.combi_testcase_list[0])
ret2 = combi_testware.combi_expected_result[0]

print(ret)
print(ret2)

exit()

# The file is mainly tested to confirm the expected results.

