Feature: answering user question about a subjet
  Scenario: the chatbot talk back
    Given the chatbot started a conversation
    When the user ask question about a specific subject
    Then the chatbot should search for the information in the database
    When it fine the information required
    Then it should send it to the user
