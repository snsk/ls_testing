import string
import math
import random
import subprocess
import os

class ArgumentsFuzzing():

    @staticmethod
    def run_ls_command(workdir):
        os.chdir(workdir)
        ret = subprocess.run([
            "ls", "-a", "-R", "-l" 
            ], capture_output=True)
        return ret.returncode


