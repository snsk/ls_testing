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

  Scenario: test case id 7
    Given with Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed directory.
    When the ls command is invoked with --dereference-command-line-symlink-to-dir option and specifies a symbolic link to directory
    Then show information for that directory

  Scenario: test case id 8
    Given with Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed directory.
    When the ls command is invoked with --dereference-command-line-symlink-to-dir option and specifies a symbolic link to directory
    Then Do not dereference symbolic links

  Scenario: test case id 9
    Given with Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed directory.
    When the ls command is invoked with --sort=size
    Then Group all the directories before the files and then sort the directories and the files separately using the selected sort key =size

  Scenario: test case id 10
    Given with Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed directory.
    When the ls command is invoked with --sort=width
    Then Group all the directories before the files and then sort the directories and the files separately using the selected sort key =width

  Scenario: test case id 11
    Given with Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed directory.
    When the ls command is invoked with --sort=extension
    Then Group all the directories before the files and then sort the directories and the files separately using the selected sort key =extension

  Scenario: test case id 12
    Given with Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed directory.
    When the ls command is invoked with --sort=size --sort=none
    Then Ignore cause --sort=size option