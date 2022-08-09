import string
import math
import random

class TestEnvironmentGenerator():

    @staticmethod
    def gen_random_file_name():
        char_array = list(string.printable)
        char_array.remove('/')
        filename_length_seed = math.floor(random.random()*255)
        filename = ''
        for _ in range(filename_length_seed):
            filename = filename + random.choice(char_array)
        return filename

    @staticmethod
    def gen_random_directory_hierarchy_and_put_files(seed, root_dir):
        pass

class HierarchyFuzzing():

    def run_ls_command(args, seed):
        pass