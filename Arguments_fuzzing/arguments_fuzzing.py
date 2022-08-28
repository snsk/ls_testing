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

    @staticmethod
    def run_ls_command(workdir):
        os.chdir(workdir)
        ret = subprocess.run([
            "ls", "-a", "-R", "-l" 
            ], capture_output=True)
        return ret.returncode


