# Feature: {feature_name}

{feature_description}

## Scenarios

Scenario: Successful {feature_name}
  Given {precondition}
  When {action}
  Then {expected_result}

Scenario Outline: Failure in {feature_name} due to <reason>
  Given {precondition}
  When {invalid_action}
  Then {error_message}

  Examples:
    | reason | invalid_action | error_message |
    |        |                |               |

## Edge Cases

Scenario: {edge_case_title}
  Given {precondition}
  When {edge_case_action}
  Then {expected_result}
