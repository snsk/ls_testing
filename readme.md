[![CI](https://github.com/snsk/ls_testing/actions/workflows/ls_test.yml/badge.svg)](https://github.com/snsk/ls_testing/actions/workflows/ls_test.yml)
[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)

# ls command test development

## SUT
ls command for ubuntsu-latest Ubuntu 20.04.3 LTS as of 2020-11

## Test base
* [$man ls](https://github.com/snsk/ls_testing/wiki/man-ls(1))
* Detail page https://www.gnu.org/software/coreutils/manual/html_node/ls-invocation.html#ls-invocation

## Source code(Coreutils)
* https://github.com/coreutils/coreutils/blob/master/src/ls.c
* argument switch
    * https://github.com/coreutils/coreutils/blob/5e36c0ce078a65c7dac6ac5ebdfb0cf096856427/src/ls.c#L1916

## Test Development/Design Document:

https://github.com/snsk/ls_testing/wiki/test_development

## How to test exection

### Functional_SpecConfirmance_BasicBehavior
### Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed
### Robustness_Consider_Noise

Test Case Execution:
```sh
git clone https://github.com/snsk/ls_testing.git
sudo apt install python3-behave
cd ls_testing
behave
```
*Currently IDs 6, 7, 8, 10, 12, and 15 for "Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed" fail. This does not appear to be working properly for the GNU specification.

### Functional_SpecConfirmance_Arguments_Combination_WhichFilesAreListed

Test Case Execution:
```sh
git clone https://github.com/snsk/ls_testing.git
pip install pytest
cd ls_testing
pytest
```

### Robustness_Hierarchy_Fuzzing

Test Case Execution:
```sh
git clone https://github.com/snsk/ls_testing.git
pip install randomfiletree
cd ls_testing/HierarchyFuzzing
python3 run_hf.py
```

![image](https://user-images.githubusercontent.com/462430/184812739-337c471d-a366-47ce-bf31-0bb1b68794dd.png)

## CI Integration Sample

CI by Github Actions is supported(see /workflows/ls_test.yml). In the example below, fuzzing is executed in parallel with Functional Testing because it takes time.

![image](https://user-images.githubusercontent.com/462430/185539169-005bd0df-7bc9-4c66-8457-a1478163c1a2.png)

## License
MIT
