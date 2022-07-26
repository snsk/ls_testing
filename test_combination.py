import os
import combi_testware

combi_testware.gen_testdata()
new_dir_path = 'Functional_SpecConfirmance_Arguments_Combination_WhichFilesAreListed'

if new_dir_path in os.getcwd(): #this "given" will call many times in this feature.
    pass
else:
    os.chdir('./'+new_dir_path+'/')

def test_tmp():
    ret = combi_testware.run_ls_command(combi_testware.combi_testcase_list[0])
    assert ret == combi_testware.combi_expected_result[1]
