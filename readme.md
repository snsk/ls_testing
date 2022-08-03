# ls command test development

Test Development/Design Document:

https://github.com/snsk/ls_testing/wiki/test_development

## How to test exection

### Functional_SpecConfirmance_BasicBehavior
### Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed

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
