Feature: interacting with chatbot
  Scenario: the chatbot remember what the user is talking about

    Given user asked a question about a subject
    When chatbot respond with details
    And the user asks for more details without mentioning the subject
    Then the chatbot should be able to remember the subject
