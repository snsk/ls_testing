Feature: Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed

# test case id has refer from:
#https://gihoz.com/users/snsk/repositories/ls_testing/documents/cause_flow_diagram/ffb93c29-1194-4d49-bf7c-aa66abc107d4

  Scenario: test case id 1
    Given with Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed directory.
    When the ls command is invoked with -a option.
    Then do not ignore file names that start with dot.

  Scenario: test case id 2
    Given with Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed directory.
    When the ls command is invoked with -a and -A option.
    Then ignore cause -a option.

TODO: next, test case id 3 on
https://gihoz.com/users/snsk/repositories/ls_testing/documents/cause_flow_diagram/ffb93c29-1194-4d49-bf7c-aa66abc107d4