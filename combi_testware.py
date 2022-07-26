import subprocess
import os

def run_ls_command(args_pair):
        ret = subprocess.run([
            "ls", 
            args_pair[0],
            args_pair[1],  
        ], capture_output=True)
        return ret.stdout

def gen_testdata():
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

combi_testcase_list = [('-a', '-A'), ('-a', '-B'), ('-a', '-d'), ('-a', '-H'), ('-a', '--sort=size'), ('-a', '--sort=width'), ('-a', '--sort=extension'), ('-a', '--sort=none'), ('-a', '--hide=`*.a'), ('-a', '--ignore=*.a'), ('-a', '-L'), ('-a', '-R'), ('-A', '-B'), ('-A', '-d'), ('-A', '-H'), ('-A', '--sort=size'), ('-A', '--sort=width'), ('-A', '--sort=extension'), ('-A', '--sort=none'), ('-A', '--hide=`*.a'), ('-A', '--ignore=*.a'), ('-A', '-L'), ('-A', 
'-R'), ('-B', '-d'), ('-B', '-H'), ('-B', '--sort=size'), ('-B', '--sort=width'), ('-B', '--sort=extension'), ('-B', '--sort=none'), ('-B', '--hide=`*.a'), ('-B', '--ignore=*.a'), ('-B', '-L'), ('-B', '-R'), ('-d', '-H'), ('-d', '--sort=size'), ('-d', '--sort=width'), ('-d', '--sort=extension'), ('-d', '--sort=none'), ('-d', '--hide=`*.a'), ('-d', '--ignore=*.a'), ('-d', '-L'), ('-d', '-R'), ('-H', '--sort=size'), ('-H', '--sort=width'), ('-H', '--sort=extension'), ('-H', '--sort=none'), ('-H', '--hide=`*.a'), ('-H', '--ignore=*.a'), ('-H', '-L'), ('-H', '-R'), ('--sort=size', 
'--sort=width'), ('--sort=size', '--sort=extension'), ('--sort=size', '--sort=none'), ('--sort=size', '--hide=`*.a'), ('--sort=size', '--ignore=*.a'), ('--sort=size', '-L'), ('--sort=size', '-R'), ('--sort=width', '--sort=extension'), ('--sort=width', '--sort=none'), ('--sort=width', '--hide=`*.a'), ('--sort=width', '--ignore=*.a'), ('--sort=width', '-L'), ('--sort=width', '-R'), ('--sort=extension', '--sort=none'), ('--sort=extension', '--hide=`*.a'), ('--sort=extension', '--ignore=*.a'), ('--sort=extension', '-L'), ('--sort=extension', '-R'), ('--sort=none', '--hide=`*.a'), ('--sort=none', '--ignore=*.a'), ('--sort=none', '-L'), ('--sort=none', '-R'), ('--hide=`*.a', '--ignore=*.a'), ('--hide=`*.a', '-L'), ('--hide=`*.a', '-R'), ('--ignore=*.a', '-L'), ('--ignore=*.a', '-R'), ('-L', '-R')]

combi_expected_result = [
(b'.eeeeeee.b\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl\nhhh_16\nhhh_32\n'),
(b'.\n..\n.eeeeeee.b\naaa.a\nbbbb.a\nccccc.b\nfff\nggg_sl\nhhh_16\nhhh_32\n'),
(b'Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed\n'),  
(b'.\n..\n.eeeeeee.b\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl\nhhh_16\nhhh_32\n'),
(b'.\n..\nfff\nhhh_32\nhhh_16\nggg_sl\n.eeeeeee.b\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\n'),
(b''),
(b'fff\nggg_sl\nhhh_16\nhhh_32\n.\n..\naaa.a\nbbbb.a\n.eeeeeee.b\nccccc.b\ndddddd.b~\n'),
(b'.\n..\n.eeeeeee.b\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl\nhhh_16\nhhh_32\n'),
(b'.\n..\n.eeeeeee.b\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl\nhhh_16\nhhh_32\n'),
(b'.\n..\n.eeeeeee.b\nccccc.b\ndddddd.b~\nfff\nggg_sl\nhhh_16\nhhh_32\n'),
(b'.\n..\n.eeeeeee.b\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl\nhhh_16\nhhh_32\n'),
(b'Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed:\n.\n..\n.eeeeeee.b\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl\nhhh_16\nhhh_32\n\nFunctional_SpecConfirmance_Arguments_Single_WhichFilesAreListed/fff:\n.\n..\n'),
(b'.eeeeeee.b\naaa.a\nbbbb.a\nccccc.b\nfff\nggg_sl\nhhh_16\nhhh_32\n'),  
(b'Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed\n'),
(b'.eeeeeee.b\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl\nhhh_16\nhhh_32\n'),
(b'fff\nhhh_32\nhhh_16\nggg_sl\n.eeeeeee.b\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\n'),
(b''),
(b'fff\nggg_sl\nhhh_16\nhhh_32\naaa.a\nbbbb.a\n.eeeeeee.b\nccccc.b\ndddddd.b~\n'),
(b'.eeeeeee.b\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl\nhhh_16\nhhh_32\n'),
(b'.eeeeeee.b\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl\nhhh_16\nhhh_32\n'),
(b'.eeeeeee.b\nccccc.b\ndddddd.b~\nfff\nggg_sl\nhhh_16\nhhh_32\n'),
(b'.eeeeeee.b\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl\nhhh_16\nhhh_32\n'),
(b'Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed:\n.eeeeeee.b\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl\nhhh_16\nhhh_32\n\nFunctional_SpecConfirmance_Arguments_Single_WhichFilesAreListed/fff:\n'),
(b'Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed\n'),  
(b'aaa.a\nbbbb.a\nccccc.b\nfff\nggg_sl\nhhh_16\nhhh_32\n'),
(b'fff\nhhh_32\nhhh_16\nggg_sl\naaa.a\nbbbb.a\nccccc.b\n'),
(b''),
(b'fff\nggg_sl\nhhh_16\nhhh_32\naaa.a\nbbbb.a\nccccc.b\n'),
(b'aaa.a\nbbbb.a\nccccc.b\nfff\nggg_sl\nhhh_16\nhhh_32\n'),
(b'aaa.a\nbbbb.a\nccccc.b\nfff\nggg_sl\nhhh_16\nhhh_32\n'),
(b'ccccc.b\nfff\nggg_sl\nhhh_16\nhhh_32\n'),
(b'aaa.a\nbbbb.a\nccccc.b\nfff\nggg_sl\nhhh_16\nhhh_32\n'),
(b'Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed:\naaa.a\nbbbb.a\nccccc.b\nfff\nggg_sl\nhhh_16\nhhh_32\n\nFunctional_SpecConfirmance_Arguments_Single_WhichFilesAreListed/fff:\n'),
(b'Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed\n'),  
(b'Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed\n'),
(b''),
(b'Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed\n'),
(b'Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed\n'),
(b'Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed\n'),  
(b'Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed\n'),
(b'Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed\n'),
(b'Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed\n'),
(b'fff\nhhh_32\nhhh_16\nggg_sl\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\n'),
(b''),
(b'fff\nggg_sl\nhhh_16\nhhh_32\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\n'),
(b'aaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl\nhhh_16\nhhh_32\n'),   
(b'aaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl\nhhh_16\nhhh_32\n'),
(b'ccccc.b\ndddddd.b~\nfff\nggg_sl\nhhh_16\nhhh_32\n'),
(b'aaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl\nhhh_16\nhhh_32\n'),   
(b'Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed:\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl\nhhh_16\nhhh_32\n\nFunctional_SpecConfirmance_Arguments_Single_WhichFilesAreListed/fff:\n'),
(b''),
(b'fff\nggg_sl\nhhh_16\nhhh_32\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\n'),
(b'aaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl\nhhh_16\nhhh_32\n'),
(b'fff\nhhh_32\nhhh_16\nggg_sl\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\n'),
(b'fff\nhhh_32\nhhh_16\nggg_sl\nccccc.b\ndddddd.b~\n'),
(b'fff\nhhh_32\nhhh_16\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nggg_sl\n'),
(b'Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed:\nfff\nhhh_32\nhhh_16\nggg_sl\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\n\nFunctional_SpecConfirmance_Arguments_Single_WhichFilesAreListed/fff:\n'),
(b''),
(b''),
(b''),
(b''),
(b''),
(b''),
(b'aaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl\nhhh_16\nhhh_32\n'),
(b'fff\nggg_sl\nhhh_16\nhhh_32\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\n'),
(b'fff\nggg_sl\nhhh_16\nhhh_32\nccccc.b\ndddddd.b~\n'),
(b'fff\nggg_sl\nhhh_16\nhhh_32\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\n'),
(b'Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed:\nfff\nggg_sl\nhhh_16\nhhh_32\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\n\nFunctional_SpecConfirmance_Arguments_Single_WhichFilesAreListed/fff:\n'),
(b'aaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl\nhhh_16\nhhh_32\n'),
(b'ccccc.b\ndddddd.b~\nfff\nggg_sl\nhhh_16\nhhh_32\n'),
(b'aaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl\nhhh_16\nhhh_32\n'),
(b'Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed:\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl\nhhh_16\nhhh_32\n\nFunctional_SpecConfirmance_Arguments_Single_WhichFilesAreListed/fff:\n'),
(b'ccccc.b\ndddddd.b~\nfff\nggg_sl\nhhh_16\nhhh_32\n'),
(b'aaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl\nhhh_16\nhhh_32\n'),
(b'Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed:\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl\nhhh_16\nhhh_32\n\nFunctional_SpecConfirmance_Arguments_Single_WhichFilesAreListed/fff:\n'),
(b'ccccc.b\ndddddd.b~\nfff\nggg_sl\nhhh_16\nhhh_32\n'),
(b'Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed:\nccccc.b\ndddddd.b~\nfff\nggg_sl\nhhh_16\nhhh_32\n\nFunctional_SpecConfirmance_Arguments_Single_WhichFilesAreListed/fff:\n'),
(b'Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed:\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl\nhhh_16\nhhh_32\n\nFunctional_SpecConfirmance_Arguments_Single_WhichFilesAreListed/fff:\n'),
]