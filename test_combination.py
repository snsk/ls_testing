import os
import combi_testware
import pytest

combi_testware.gen_testdata()
new_dir_path = 'Functional_SpecConfirmance_Arguments_Combination_WhichFilesAreListed'

if new_dir_path in os.getcwd(): #this "given" will call many times in this feature.
    pass
else:
    os.chdir('./'+new_dir_path+'/')

@pytest.mark.parametrize('val, expected', combi_testware.testcase_expected_pair_list)
def test_multiple(val, expected):
    assert combi_testware.run_ls_command(val) == expected

