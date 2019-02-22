Feature: Handle user general question
  Scenario: the answer is not in database
    Given the user ask general question
    Then the chatbot should search the database
    When when the answer is not found
    Then chatbot send a correction back to the user
