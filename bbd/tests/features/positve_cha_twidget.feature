Feature: finding the widget in the  page
  Scenario: the widget is there
    Given the user in the specific page
    When chatbot is accessible
    When the user open the chat
    Then the widget expands and the chatbot starts a conversation
