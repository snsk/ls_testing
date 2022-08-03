import os
import subprocess, sys
import combi_testware
import string

char_array = list(string.printable)
char_array.remove('/')
print(char_array)

def gen_random_file_name():
    pass

exit()

# generate combination test case and expected result

new_dir_path = 'Functional_SpecConfirmance_Arguments_Combination_WhichFilesAreListed'
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

