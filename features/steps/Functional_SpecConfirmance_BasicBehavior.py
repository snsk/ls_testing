import os
import subprocess, sys
from hamcrest import assert_that, equal_to

# # Functional_SpecConfirmance_BasicBehavior Test Case Imprement

new_dir_path = 'Functional_SpecConfirmance_BasicBehavior'

if not os.path.exists(new_dir_path):
    os.makedirs(new_dir_path)

file_list = ['aaa', 'bbb', 'ccc', 'd\ad']

for file_name in file_list:
    f = open('./'+new_dir_path+'/'+file_name, 'w')
    f.close()

if not os.path.exists('./'+new_dir_path+'/eee/'):
    os.makedirs('./'+new_dir_path+'/eee/')

expected_normal_output = b'aaa\nbbb\nccc\nd\x07d\neee\n'

@given(u'current directory.')
def step_impl(context):
    if new_dir_path in os.getcwd(): #this "given" will call many times in this feature.
        pass
    else:
        os.chdir('./'+new_dir_path+'/')

@when(u'the ls command is invoked with non-option.')
def step_impl(context):
    context.res_no_arg = subprocess.run("ls", capture_output=True)
    print(context.res_no_arg.stdout)

@then(u'same as invoked with a single argument of ‘.’.')
def step_impl(context):
    context.res_dot  = subprocess.run(["ls", "."], capture_output=True)
    assert_that(context.res_no_arg.stdout, equal_to(context.res_dot.stdout))

@when(u'the ls command is invoked with Terminal.') #TODO: make not clear the "invoked Terminal"
def step_impl(context):
    context.hyphen1  = subprocess.run(["ls", "-1"], capture_output=True)

@then(u'the output is in columns (sorted vertically).')
@then(u'control characters are output as question marks') #TODO: make not clear the "invoked Terminal"
def step_impl(context):
    assert_that(context.hyphen1.stdout, equal_to(expected_normal_output))

@then(u'the output is listed one per line')
@then(u'control characters are output as-is')
@then(u'lists the contents of directories')
@then(u'not recursively')
@then(u'omitting files with names beginning with ‘.’')
@then(u'the output is sorted alphabetically')
def step_impl(context):
    assert_that(context.res_no_arg.stdout, equal_to(expected_normal_output))








