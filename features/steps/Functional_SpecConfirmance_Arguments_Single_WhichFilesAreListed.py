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
    assert_that(context.res_hyphen_a.stdout, equal_to(b'.\n..\n.eeeeeee.b\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n'))

@when(u'the ls command is invoked -A option.')
def step_impl(context):
    context.res_hyphen_a = subprocess.run(["ls", "-A"], capture_output=True) 

@then(u'do not ignore all file names that start with . ignore only . and ..')        
def step_impl(context):
    assert_that(context.res_hyphen_a.stdout, equal_to(b'.eeeeeee.b\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n'))

@when(u'the ls command is invoked with -a and -A option.')
def step_impl(context):
    context.res_hyphen_a_A = subprocess.run(["ls", "-a", "-A"], capture_output=True)

@then(u'ignore cause -a option.')
def step_impl(context):
    assert_that(context.res_hyphen_a_A.stdout, equal_to(b'.eeeeeee.b\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n'))

@when(u'the ls command is invoked with -B option.')       
def step_impl(context):
    context.res_hyphen_B = subprocess.run(["ls", "-B"], capture_output=True)

@then(u'ignore files that end with ~')
def step_impl(context):
    assert_that(context.res_hyphen_B.stdout, equal_to(b'aaa.a\nbbbb.a\nccccc.b\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n'))

@when(u'the ls command is invoked with -d option.')
def step_impl(context):
    context.res_hyphen_d = subprocess.run(["ls", "-d"], capture_output=True)

@then(u'List just the names of directories')
def step_impl(context):
    assert_that(context.res_hyphen_d.stdout, equal_to(b'.\n'))

@when(u'the ls command is invoked with -H option and specifies a symbolic link')
def step_impl(context):        
    context.res_hyphen_H = subprocess.run(["ls","ggg_sl_f", "-H"], capture_output=True)

@then(u'show information for the file the link references')   
def step_impl(context):
    assert_that(context.res_hyphen_H.stdout, equal_to(b'aaa.a\n'))

@when(u'the ls command is invoked with --dereference-command-line-symlink-to-dir option and specifies a symbolic link to directory')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the ls command is invoked with --dereference-command-line-symlink-to-dir option and specifies a symbolic link to directory')
    #could not create symlink to directory

@then(u'show information for that directory')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then show information for that directory')
    #could not create symlink to directory

@then(u'Do not dereference symbolic links')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Do not dereference symbolic links')
    #could not create symlink to directory

@when(u'the ls command is invoked with --sort=size')
def step_impl(context):
    context.res_hyphen_sort_size = subprocess.run(["ls","--sort=size"], capture_output=True)

@then(u'Group all the directories before the files and then sort the directories and the files separately using the selected sort key =size')
def step_impl(context):
    assert_that(context.res_hyphen_sort_size.stdout, equal_to(b'fff\nggg_sl_d\nhhh_32\nhhh_16\nggg_sl_f\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\n'))

@when(u'the ls command is invoked with --sort=width')
def step_impl(context):
    context.res_hyphen_sort_width = subprocess.run(["ls","--sort=width"], capture_output=True)

@then(u'Group all the directories before the files and then sort the directories and the files separately using the selected sort key =width')
def step_impl(context):
    assert_that(context.res_hyphen_sort_width.stdout, equal_to(b'fff\naaa.a\nhhh_32\nhhh_16\nbbbb.a\nccccc.b\ndddddd.b~\nggg_sl_f\nggg_sl_d\n'))

@when(u'the ls command is invoked with --sort=extension')
def step_impl(context):
    context.res_hyphen_sort_ext = subprocess.run(["ls","--sort=extension"], capture_output=True)

@then(u'Group all the directories before the files and then sort the directories and the files separately using the selected sort key =extension')
def step_impl(context):
    assert_that(context.res_hyphen_sort_ext.stdout, equal_to(b'fff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\n'))

@when(u'the ls command is invoked with --sort=size --sort=none')
def step_impl(context):
    context.res_hyphen_sort_s_and_n = subprocess.run(["ls","--sort=size", "--sort=none"], capture_output=True)

@then(u'Ignore cause --sort=size option')
def step_impl(context):
    assert_that(context.res_hyphen_sort_s_and_n.stdout, equal_to(b'ggg_sl_f\nhhh_16\nccccc.b\nhhh_32\nggg_sl_d\ndddddd.b~\nfff\nbbbb.a\naaa.a\n'))

@when(u'the ls command is invoked with --hide=*.a')
def step_impl(context):
    context.res_hyphen_hyde = subprocess.run(["ls","--hide=*.a"], capture_output=True)

@when(u'the ls command is invoked with --ignore=*.a')
def step_impl(context):
    context.res_hyphen_hyde = subprocess.run(["ls","--ignore=*.a"], capture_output=True)

@then(u'ignore files whose names match the shell pattern pattern')
def step_impl(context):
    assert_that(context.res_hyphen_hyde.stdout, equal_to(b'ccccc.b\ndddddd.b~\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n'))

@when(u'the ls command is invoked with -L')
def step_impl(context):
    context.res_hyphen_L = subprocess.run(["ls","-L"], capture_output=True)

@then(u'show information for the file the link references and still prints the name of the link itself,')
def step_impl(context):
    assert_that(context.res_hyphen_L.stdout, equal_to(b'aaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl_d\naaa.a\nhhh_16\nhhh_32\n'))

@when(u'the ls command is invoked with -R')
def step_impl(context):
    context.res_hyphen_R = subprocess.run(["ls","-R"], capture_output=True)

@then(u'List the contents of all directories recursively.')
def step_impl(context):
    assert_that(context.res_hyphen_R.stdout, equal_to(b'.:\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n\n./fff:\n\n./ggg_sl_d:\n'))