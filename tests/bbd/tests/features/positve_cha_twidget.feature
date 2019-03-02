Feature: finding the widget in the  page
  Scenario: the widget is there
    Given the user in the specific page
    When chatbot is accessible
    Then the widget expands and the chatbot starts a conversation
