Feature: Functional_SpecConfirmance_BasicBehavior

# test case id has refer from:
# https://gihoz.com/users/snsk/repositories/ls_testing/documents/cause_flow_diagram/991c7722-3cee-4519-aba7-86b0de69bc93

  Scenario: test case id 1
    Given current directory.
    When the ls command is invoked with non-option.
    Then same as invoked with a single argument of ‘.’.

  Scenario: test case id 2
    Given current directory.
    When the ls command is invoked with Terminal.
    Then the output is in columns (sorted vertically).

  Scenario: test case id 3
    Given current directory.
    When the ls command is invoked with Terminal.
    Then control characters are output as question marks    

  Scenario: test case id 4
    Given current directory.
    When the ls command is invoked with non-option.
    Then the output is listed one per line

  Scenario: test case id 5
    When the ls command is invoked with non-option.
    Then control characters are output as-is

  Scenario: test case id 6
    Given current directory.
    When the ls command is invoked with non-option.
    Then lists the contents of directories
  