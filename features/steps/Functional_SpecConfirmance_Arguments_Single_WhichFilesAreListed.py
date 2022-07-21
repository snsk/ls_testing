import os
import subprocess, sys
from hamcrest import assert_that, equal_to

# Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed Test Case Imprement

new_dir_path = 'Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed'

if not os.path.exists(new_dir_path):
    os.makedirs(new_dir_path)

file_list = ['aaa.a', 'bbbb.a', 'ccccc.b', 'dddddd.b~', '.eeeeeee.b']

for file_name in file_list:
    f = open('./'+new_dir_path+'/'+file_name, 'w')
    f.close()

if not os.path.exists('./'+new_dir_path+'/fff/'):
    os.makedirs('./'+new_dir_path+'/fff/')

if not os.path.exists('./'+new_dir_path+'/ggg_sl'):
    os.symlink('aaa.a', './'+new_dir_path+'/ggg_sl')

if not os.path.exists('./'+new_dir_path+'/hhh_16'):
    subprocess.run(["fallocate", "-l", "16", "./"+new_dir_path+"/"+"hhh_16"], capture_output=True)

if not os.path.exists('./'+new_dir_path+'/hhh_32'):
    subprocess.run(["fallocate", "-l", "32", "./"+new_dir_path+"/"+"hhh_32"], capture_output=True)

expected_normal_output = b'aaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl\nhhh_16\nhhh_32\n'


@given(u'with Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed directory.')
def step_impl(context):
    if new_dir_path in os.getcwd(): #this "given" will call many times in this feature.
        pass
    else:
        os.chdir('./'+new_dir_path+'/')
        print(os.getcwd())

@when(u'the ls command is invoked with -a option.')
def step_impl(context):
    context.res_hyphen_a = subprocess.run(["ls", "-a"], capture_output=True)

@then(u'do not ignore file names that start with dot.')
def step_impl(context):
    assert_that(context.res_hyphen_a.stdout, equal_to(b'.\n..\n.eeeeeee.b\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl\nhhh_16\nhhh_32\n'))

@when(u'the ls command is invoked with -a and -A option.')
def step_impl(context):
    context.res_hyphen_a_A = subprocess.run(["ls", "-a", "-A"], capture_output=True)

@then(u'ignore cause -a option.')
def step_impl(context):
    assert_that(context.res_hyphen_a_A.stdout, equal_to(b'.eeeeeee.b\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl\nhhh_16\nhhh_32\n'))

@when(u'the ls command is invoked with -B option.')       
def step_impl(context):
    context.res_hyphen_B = subprocess.run(["ls", "-B"], capture_output=True)

@then(u'ignore files that end with ~')
def step_impl(context):
    assert_that(context.res_hyphen_B.stdout, equal_to(b'aaa.a\nbbbb.a\nccccc.b\nfff\nggg_sl\nhhh_16\nhhh_32\n'))

@when(u'the ls command is invoked with -d option.')
def step_impl(context):
    context.res_hyphen_d = subprocess.run(["ls", "-d"], capture_output=True)

@then(u'List just the names of directories')
def step_impl(context):
    assert_that(context.res_hyphen_d.stdout, equal_to(b'.\n'))