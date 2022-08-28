import string
import math
import random
import subprocess
import os

class TestEnvironmentGenerator():

    __char_array = list(string.printable)
    __char_array.remove('/')

    @classmethod
    def gen_random_file_name(cls):    
        filename = ''
        for _ in range(math.floor(random.random()*255)):
            filename = filename + random.choice(cls.__char_array)
        return filename

class ArgumentsFuzzing():

    # generate random arguments combination to __run_arg_array
    __arg_array = ["-a", "-A", "-B", "-d", "-H", "--dereference-command-line-symlink-to-dir", "--sort=size", "--sort=extension","--sort=none", "--hide=*.a","--ignore=*.a", "-L","-R", "."]
    __run_arg_array = ["ls"]
        
    @classmethod
    def run_ls_command(cls, workdir):

        for i in range(math.floor(random.random()*len(cls.__arg_array))):
            cls.__run_arg_array.append(random.choice(cls.__arg_array))

        os.chdir(workdir)
        ret = subprocess.run(cls.__run_arg_array, capture_output=True)
        return ret.returncode, ret.stdout, ret.stderr, cls.__run_arg_array


