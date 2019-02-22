
Feature: interacting with chatbot
  Scenario: the chatbot talk back
    Given the chatbot is open
    And the text field is empty
    When the user  type something
    And  click on  enter
    Then the chatbot should reasoned to the message
