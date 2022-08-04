# HierarchyFuzzing　Design

Various directory and file structures will be generated and given to the ls command to verify that no serious malfunctions such as crashes or freezes occur. The following elements of directory and file structures are assumed.

* Number of directories
* Length of directory name
* directory hierarchy
* Number of files
* Length of file names
* number of symbolic links
* length of symbolic link names

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

## Classes

### TestEnvironmentGenerator

* static gen_random_file_name()

return 0-255 byte random file name include printable character.

* static gen_random_directory_hierarchy_and_put_files()

generate random directory hierarchy between 1-255 levels and put random name and number of files. It is mono function due to generated directory name could not pre defined.