Feature: interacting with chatbot
  Scenario: the chatbot talk back

    Given I asked a question about a subject
    And chatbot respond with details
    When the user asks for more details without mentioning the subject
    Then the chatbot should be able to remember the subject
