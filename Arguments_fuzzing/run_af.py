import arguments_fuzzing as af
import random
import shutil
import os
import time

workdir = './tmp'
round = 100
error_count = 0
print('workdir:' + os.getcwd())
start = time.time()

def elapsed_time_str(seconds):
    seconds = int(seconds + 0.5)
    h = seconds // 3600 
    m = (seconds - h * 3600) // 60
    s = seconds - h * 3600 - m * 60
    return f"{h:02}:{m:02}:{s:02}"

for i in range(round):

    randomfiletree.core.iterative_gaussian_tree(
        workdir,
        nfiles=random.random()*1000,
        nfolders=random.random()*1000,    
        maxdepth=random.random()*100,
        filename = hf.TestEnvironmentGenerator.gen_random_file_name
    )
    if hf.HierarchyFuzzing.run_ls_command(workdir) != 0:
        error_count = error_count+1
    os.chdir('..')
    shutil.rmtree(workdir)
    print("\r"  + "test run count: "+ str(i+1) 
                + " elapsed time:" + elapsed_time_str(time.time() - start)
                + " error count: "+ str(error_count)
               ,end="")

print("\nerror count: "+str(error_count))