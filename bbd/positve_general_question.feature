 Feature: answering user general question
  Scenario: the chatbot talk back
    Given chatbot is accessible
    When  the user ask general question
    Then the chatbot should search the database
    When It found the answer
    Then should send it back to the user
