import randomfiletree
import hierarchy_fuzzing as hf
import random
import string
import shutil
import os
import time

workdir = './tmp'
round = 100
print('workdir:' + os.getcwd())

for i in range(round):

    randomfiletree.core.iterative_gaussian_tree(
        workdir,
        nfiles=100,
        nfolders=10,
        maxdepth=100,
        filename = hf.TestEnvironmentGenerator.gen_random_file_name
    )
    hf.HierarchyFuzzing.run_ls_command(workdir)
    os.chdir('..')
    shutil.rmtree(workdir)
