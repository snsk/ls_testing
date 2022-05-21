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