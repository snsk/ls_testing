Feature: Robustness_Consider_Noise

# test case id has refer from:
# https://github.com/snsk/ls_testing/wiki/test_development#robustness_consider_noise

  Scenario: test case id 1
    Given current directory.
    When the ls command is invoked in not permitted file. 
    Then Error message like "Permission denied" occurs.

  Scenario: test case id 2
    Given current directory.
    When the ls command specified not exist file/directory name.
    Then Error message like "No such file or directory" occurs.
