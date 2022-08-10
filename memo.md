# HierarchyFuzzing Design

Various directory and file structures will be generated and given to the ls command to verify that no serious malfunctions such as crashes or freezes occur. The following elements of directory and file structures are assumed.

* Number of directories
* Length of directory name
* directory hierarchy
* Number of files
* Length of file names

## General restrictions for Linux and file systems are as follows

Maximum length of file names (directory names) is 255 bytes
Maximum length of path names is 1023 bytes

## Typically Use case

1. Generate test environment.
2. Run ls command as follows.
    1. run fuzzing root directory with no argument.
    2. run fuzzing root directory with random argument combination.
3. Check return value the ls command and watch timeout
4. repeat step2, and step3.

## Import modules 

import randomfiletree

## Classes

### TestEnvironmentGenerator

* static gen_random_file_name()

Return 0-255 byte random file name include printable character.

### HierarchyFuzzing

* run_ls_command(args, seed)

Exec ls command one times with specified args, seed and monitoring return value. Arguments are optional. Seed value will pass to `gen_random_directory_hierarchy_and_put_files()`. If ls command return illegler value, this function raise exception with seed value. It value is necessary to re-procedure illegler behavior.

* main(args)

Execute Hierarchy Fuzzing process and provide information the process follows:

-Elapsed time since process start
-Number of successful test runs
-Occurred exceptions and seed values





