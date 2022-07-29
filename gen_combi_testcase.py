import os
import subprocess, sys
import itertools
import combi_testware

args = ('-a', '-A', '-B', '-d', '-H', '--sort=size', '--sort=width', '--sort=extension', '--sort=none', '--hide=`*.a', '--ignore=*.a', '-L', '-R')
arg_combi_list = list(itertools.combinations(args ,2))

print('[')
for i, item in enumerate(arg_combi_list):
    ret = subprocess.run([
        "ls", 
        "Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed",
        item[0],
        item[1],
        ], capture_output=True)
    print('('+ str(arg_combi_list[i]) + ', ' + '('+str(ret.stdout)+')),')
print(']')

print(len(combi_testware.combi_testcase_list))
print(len(combi_testware.combi_expected_result))
