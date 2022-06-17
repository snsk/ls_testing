import os
import subprocess, sys
from hamcrest import assert_that, equal_to

# Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed Test Case Imprement

new_dir_path = 'Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed'

if not os.path.exists(new_dir_path):
    os.makedirs(new_dir_path)

file_list = ['aaa', 'bbbb', 'ccccc', 'dddddd~', '.eeeeeee']

for file_name in file_list:
    f = open('./'+new_dir_path+'/'+file_name, 'w')
    f.close()

if not os.path.exists('./'+new_dir_path+'/fff/'):
    os.makedirs('./'+new_dir_path+'/fff/')

if not os.path.exists('./'+new_dir_path+'/ggg_sl'):
    os.symlink('aaa', './'+new_dir_path+'/ggg_sl')

if not os.path.exists('./'+new_dir_path+'/hhh_16'):
    subprocess.run(["fallocate", "-l", "16", "./"+new_dir_path+"/"+"hhh_16"], capture_output=True)

if not os.path.exists('./'+new_dir_path+'/hhh_32'):
    subprocess.run(["fallocate", "-l", "32", "./"+new_dir_path+"/"+"hhh_32"], capture_output=True)

expected_normal_output = b'aaa\nbbb\nccc\nd\x07d\neee\n'