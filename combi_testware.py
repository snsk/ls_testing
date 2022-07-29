import subprocess
import os

def run_ls_command(args_pair):

    new_dir_path = 'Functional_SpecConfirmance_Arguments_Combination_WhichFilesAreListed'
    if new_dir_path in os.getcwd(): 
        pass
    else:
        os.chdir('./'+new_dir_path+'/')

    ret = subprocess.run([
        "ls", 
        args_pair[0],
        args_pair[1],  
    ], capture_output=True)
    return ret.stdout

def gen_testdata():

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

testcase_expected_pair_list =[
(('-a', '-A'), (b'.eeeeeee.b\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n')),
(('-a', '-B'), (b'.\n..\n.eeeeeee.b\naaa.a\nbbbb.a\nccccc.b\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n')),
(('-a', '-d'), (b'.\n')),
(('-a', '-H'), (b'.\n..\n.eeeeeee.b\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n')),
(('-a', '--sort=size'), (b'.\n..\nfff\nggg_sl_d\nhhh_32\nhhh_16\nggg_sl_f\n.eeeeeee.b\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\n')),
(('-a', '--sort=width'), (b'')),
(('-a', '--sort=extension'), (b'fff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n.\n..\naaa.a\nbbbb.a\n.eeeeeee.b\nccccc.b\ndddddd.b~\n')),
(('-a', '--sort=none'), (b'.\n..\n.eeeeeee.b\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n')),
(('-a', '--hide=`*.a'), (b'.\n..\n.eeeeeee.b\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n')),
(('-a', '--ignore=*.a'), (b'.\n..\n.eeeeeee.b\nccccc.b\ndddddd.b~\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n')),
(('-a', '-L'), (b'.\n..\n.eeeeeee.b\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n')),
(('-a', '-R'), (b'.:\n.\n..\n.eeeeeee.b\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n\n./fff:\n.\n..\n\n./ggg_sl_d:\n.\n..\n')),
(('-A', '-B'), (b'.eeeeeee.b\naaa.a\nbbbb.a\nccccc.b\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n')),
(('-A', '-d'), (b'.\n')),
(('-A', '-H'), (b'.eeeeeee.b\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n')),
(('-A', '--sort=size'), (b'fff\nggg_sl_d\nhhh_32\nhhh_16\nggg_sl_f\n.eeeeeee.b\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\n')),
(('-A', '--sort=width'), (b'')),
(('-A', '--sort=extension'), (b'fff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\naaa.a\nbbbb.a\n.eeeeeee.b\nccccc.b\ndddddd.b~\n')),
(('-A', '--sort=none'), (b'.eeeeeee.b\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n')),
(('-A', '--hide=`*.a'), (b'.eeeeeee.b\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n')),
(('-A', '--ignore=*.a'), (b'.eeeeeee.b\nccccc.b\ndddddd.b~\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n')),
(('-A', '-L'), (b'.eeeeeee.b\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n')),
(('-A', '-R'), (b'.:\n.eeeeeee.b\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n\n./fff:\n\n./ggg_sl_d:\n')),
(('-B', '-d'), (b'.\n')),
(('-B', '-H'), (b'aaa.a\nbbbb.a\nccccc.b\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n')),
(('-B', '--sort=size'), (b'fff\nggg_sl_d\nhhh_32\nhhh_16\nggg_sl_f\naaa.a\nbbbb.a\nccccc.b\n')),
(('-B', '--sort=width'), (b'')),
(('-B', '--sort=extension'), (b'fff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\naaa.a\nbbbb.a\nccccc.b\n')),
(('-B', '--sort=none'), (b'aaa.a\nbbbb.a\nccccc.b\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n')),
(('-B', '--hide=`*.a'), (b'aaa.a\nbbbb.a\nccccc.b\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n')),
(('-B', '--ignore=*.a'), (b'ccccc.b\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n')),
(('-B', '-L'), (b'aaa.a\nbbbb.a\nccccc.b\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n')),
(('-B', '-R'), (b'.:\naaa.a\nbbbb.a\nccccc.b\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n\n./fff:\n\n./ggg_sl_d:\n')),
(('-d', '-H'), (b'.\n')),
(('-d', '--sort=size'), (b'.\n')),
(('-d', '--sort=width'), (b'')),
(('-d', '--sort=extension'), (b'.\n')),
(('-d', '--sort=none'), (b'.\n')),
(('-d', '--hide=`*.a'), (b'.\n')),
(('-d', '--ignore=*.a'), (b'.\n')),
(('-d', '-L'), (b'.\n')),
(('-d', '-R'), (b'.\n')),
(('-H', '--sort=size'), (b'fff\nggg_sl_d\nhhh_32\nhhh_16\nggg_sl_f\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\n')),
(('-H', '--sort=width'), (b'')),
(('-H', '--sort=extension'), (b'fff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\n')),
(('-H', '--sort=none'), (b'aaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n')),
(('-H', '--hide=`*.a'), (b'aaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n')),
(('-H', '--ignore=*.a'), (b'ccccc.b\ndddddd.b~\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n')),
(('-H', '-L'), (b'aaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n')),
(('-H', '-R'), (b'.:\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n\n./fff:\n\n./ggg_sl_d:\n')),
(('--sort=size', '--sort=width'), (b'')),
(('--sort=size', '--sort=extension'), (b'fff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\n')),
(('--sort=size', '--sort=none'), (b'aaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n')),
(('--sort=size', '--hide=`*.a'), (b'fff\nggg_sl_d\nhhh_32\nhhh_16\nggg_sl_f\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\n')),
(('--sort=size', '--ignore=*.a'), (b'fff\nggg_sl_d\nhhh_32\nhhh_16\nggg_sl_f\nccccc.b\ndddddd.b~\n')),
(('--sort=size', '-L'), (b'fff\nggg_sl_d\nhhh_32\nhhh_16\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nggg_sl_f\n')),
(('--sort=size', '-R'), (b'.:\nfff\nggg_sl_d\nhhh_32\nhhh_16\nggg_sl_f\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\n\n./fff:\n\n./ggg_sl_d:\n')),
(('--sort=width', '--sort=extension'), (b'')),
(('--sort=width', '--sort=none'), (b'')),
(('--sort=width', '--hide=`*.a'), (b'')),
(('--sort=width', '--ignore=*.a'), (b'')),
(('--sort=width', '-L'), (b'')),
(('--sort=width', '-R'), (b'')),
(('--sort=extension', '--sort=none'), (b'aaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n')),
(('--sort=extension', '--hide=`*.a'), (b'fff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\n')),
(('--sort=extension', '--ignore=*.a'), (b'fff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\nccccc.b\ndddddd.b~\n')),
(('--sort=extension', '-L'), (b'fff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\n')),
(('--sort=extension', '-R'), (b'.:\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\n\n./fff:\n\n./ggg_sl_d:\n')),
(('--sort=none', '--hide=`*.a'), (b'aaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n')),
(('--sort=none', '--ignore=*.a'), (b'ccccc.b\ndddddd.b~\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n')),
(('--sort=none', '-L'), (b'aaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n')),
(('--sort=none', '-R'), (b'.:\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n\n./fff:\n\n./ggg_sl_d:\n')),
(('--hide=`*.a', '--ignore=*.a'), (b'ccccc.b\ndddddd.b~\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n')),
(('--hide=`*.a', '-L'), (b'aaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n')),
(('--hide=`*.a', '-R'), (b'.:\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n\n./fff:\n\n./ggg_sl_d:\n')),
(('--ignore=*.a', '-L'), (b'ccccc.b\ndddddd.b~\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n')),
(('--ignore=*.a', '-R'), (b'.:\nccccc.b\ndddddd.b~\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n\n./fff:\n\n./ggg_sl_d:\n')),
(('-L', '-R'), (b'.:\naaa.a\nbbbb.a\nccccc.b\ndddddd.b~\nfff\nggg_sl_d\nggg_sl_f\nhhh_16\nhhh_32\n\n./fff:\n\n./ggg_sl_d:\n')),
]
