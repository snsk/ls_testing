import os
import subprocess

# Functional_SpecConfirmance_Arguments_Combination_WhichFilesAreListed test data generated

new_dir_path = 'Functional_SpecConfirmance_Arguments_Combination_WhichFilesAreListed'

if not os.path.exists(new_dir_path):
    os.makedirs(new_dir_path)

file_list = ['aaa.a', 'bbbb.a', 'ccccc.b', 'dddddd.b~', '.eeeeeee.b']

for file_name in file_list:
    f = open('./'+new_dir_path+'/'+file_name, 'w')
    f.close()

if not os.path.exists('./'+new_dir_path+'/fff/'):
    os.makedirs('./'+new_dir_path+'/fff/')

if not os.path.exists('./'+new_dir_path+'/ggg_sl_f'):
    os.symlink('aaa.a', './'+new_dir_path+'/ggg_sl_f')

if not os.path.exists('./'+new_dir_path+'/ggg_sl_d/'):
    os.makedirs('./'+new_dir_path+'/ggg_sl_d/')

if not os.path.exists('./'+new_dir_path+'/ggg_sl_d'):
    os.symlink('fff', './'+new_dir_path+'/ggg_sl_d')

if not os.path.exists('./'+new_dir_path+'/hhh_16'):
    subprocess.run(["fallocate", "-l", "16", "./"+new_dir_path+"/"+"hhh_16"], capture_output=True)

if not os.path.exists('./'+new_dir_path+'/hhh_32'):
    subprocess.run(["fallocate", "-l", "32", "./"+new_dir_path+"/"+"hhh_32"], capture_output=True)

expected_normal_output = b'aaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl_f\nggg_sl_d\nhhh_16\nhhh_32\n'