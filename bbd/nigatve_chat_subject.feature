Feature: Handle user  questions about a subject
  Scenario: the answer is not in database
    Given the chatbot started a conversation
    When the user ask question about a specific subject
    Then the chatbot should search for the information in the database
    When it dose not fine the information required
    Then it should send that subject dose not exist
