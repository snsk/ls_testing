import os
import subprocess, sys
import combi_testware


new_dir_path = 'Functional_SpecConfirmance_Arguments_Combination_WhichFilesAreListed'
if new_dir_path in os.getcwd(): #this "given" will call many times in this feature.
    pass
else:
    os.chdir('./'+new_dir_path+'/')

ret = combi_testware.run_ls_command(combi_testware.combi_testcase_list[2])
ret2 = combi_testware.combi_expected_result[2]

print(ret)
print(ret2)

exit()

# The file is mainly tested to confirm the expected results.

os.chdir("Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed")
ret = subprocess.run([
    "ls", "-R"
    ], capture_output=True)
print(ret.stdout)