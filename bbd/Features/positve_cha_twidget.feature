Feature: finding the widget in the  page
  Scenario: the widget is there
    Given the user in the specific page
    When the wedge is seen
    When the user clicks on the widget
    Then the widget expands and the chatbot starts a conversation
