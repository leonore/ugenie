Feature: Handle user  questions about a subject
  Scenario: the answer is not in database
    Given chatbot is accessible
    When the user open the chat
    When the user ask question about a specific subject
    Then the chatbot should search for the information in the database
    When it dose not fine the information required
    Then it should send that a message that  it dose not understand the question


  Scenario: the chatbot answer the question from the database
    Given chatbot is accessible
     When the user open the chat
    When  the user ask question about a specific subject
    Then the chatbot should search the database It found the answer
    Then should send it back to the user
