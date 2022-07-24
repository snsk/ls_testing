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

  Scenario: test case id 3
    Given with Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed directory.
    When the ls command is invoked -A option.
    Then do not ignore all file names that start with . ignore only . and ..

  Scenario: test case id 4
    Given with Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed directory.
    When the ls command is invoked with -B option.
    Then ignore files that end with ~

  Scenario: test case id 5
    Given with Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed directory.
    When the ls command is invoked with -d option.
    Then List just the names of directories

  Scenario: test case id 6
    Given with Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed directory.
    When the ls command is invoked with -H option and specifies a symbolic link
    Then show information for the file the link references


  