Feature: interacting with chatbot


    Scenario: the remember  the user questions_1
    Given the chatbot have already answerd a qusetion was asked by the user
    When the user asks for further
    Then the chatbot should send the requierd information if it dose exist
