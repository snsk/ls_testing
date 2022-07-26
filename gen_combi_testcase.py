import os
import subprocess, sys
import itertools

# The file is mainly tested to confirm the expected results.

args = ('-a', '-A', '-B', '-d', '-H', '--sort=size', '--sort=width', '--sort=extension', '--sort=none', '--hide=`*.a', '--ignore=*.a', '-L', '-R')
arg_combi_list = list(itertools.combinations(args ,2))
print(arg_combi_list)

exit()

for i, item in enumerate(arg_combi_list):
    print(str(i)+':'+ item[0]+', '+item[1])
    ret = subprocess.run([
        "ls", 
        "Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed",
        item[0],
        item[1],
        ], capture_output=True)
    print(ret.stdout)