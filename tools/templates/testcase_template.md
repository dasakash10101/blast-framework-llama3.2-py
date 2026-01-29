# Feature: {feature_name}

{feature_description}

## Scenarios

  @TC01 @P1
  Scenario: Successful {feature_name}
    Given {precondition}
    When {action}
    Then {expected_result}

  @TC02 @P2
  Scenario Outline: Failure in {feature_name} due to <reason>
    Given {precondition}
    When {invalid_action}
    Then {error_message}

    Examples:
      | reason | invalid_action | error_message |
      |        |                |               |

## Edge Cases

  @TC_EDGE_01 @P3
  Scenario: {edge_case_title}
    Given {precondition}
    When {edge_case_action}
    Then {expected_result}
