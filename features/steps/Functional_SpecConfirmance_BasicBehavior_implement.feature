Feature: Functional_SpecConfirmance_BasicBehavior

  Scenario: test case id 1
    Given current directory.
    When the ls command is invoked with non-option.
    Then same as invoked with a single argument of ‘.’.