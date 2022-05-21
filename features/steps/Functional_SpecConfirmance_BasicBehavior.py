import os
import subprocess, sys
from hamcrest import assert_that, equal_to

# # Functional_SpecConfirmance_BasicBehavior Test Case Imprement

new_dir_path = 'Functional_SpecConfirmance_BasicBehavior'

if not os.path.exists(new_dir_path):
    os.makedirs(new_dir_path)

file_list = ['aaa', 'bbb', 'ccc']

for file_name in file_list:
    f = open('./'+new_dir_path+'/'+file_name, 'w')
    f.close()

@given(u'current directory.')
def step_impl(context):
    if new_dir_path in os.getcwd(): #this "given" will call many times in this feature.
        pass
    else:
        os.chdir('./'+new_dir_path+'/')

@when(u'the ls command is invoked with non-option.')
def step_impl(context):
    context.res_no_arg = subprocess.run("ls", capture_output=True)
    context.res_dot  = subprocess.run(["ls", "."], capture_output=True)

@then(u'same as invoked with a single argument of ‘.’.')
def step_impl(context):
    assert_that(context.res_no_arg.stdout, equal_to(context.res_dot.stdout))

@when(u'the ls command is invoked with Terminal.')#TODO: make not clear the "invoked Terminal"
def step_impl(context):
    context.hyphen1  = subprocess.run(["ls", "-1"], capture_output=True)

@then(u'the output is in columns (sorted vertically).')
def step_impl(context):
    print(context.hyphen1.stdout)
    assert_that(context.hyphen1.stdout, equal_to(b'aaa\nbbb\nccc\n'))
