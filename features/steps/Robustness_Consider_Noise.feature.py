import os
import subprocess, sys
from hamcrest import assert_that, equal_to

# # Functional_SpecConfirmance_BasicBehavior Test Case Imprement

@when(u'the ls command is invoked in not permitted file.')       
def step_impl(context):
    context.res_npf  = subprocess.run(["ls", "/root"], capture_output=True)

@then(u'Error message like "Permission denied" occurs.')
def step_impl(context):
    assert_that(context.res_npf.stderr, equal_to(b"ls: cannot open directory '/root': Permission denied\n"))

@when(u'the ls command specified not exist file/directory name.')
def step_impl(context):
    context.res_npf  = subprocess.run(["ls", "/hogehoge_not_exist_file"], capture_output=True)

@then(u'Error message like "No such file or directory" occurs.') 
def step_impl(context):
    assert_that(context.res_npf.stderr, equal_to(b"ls: cannot access '/hogehoge_not_exist_file': No such file or directory\n"))








