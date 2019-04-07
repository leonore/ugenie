# Behaviour-Driven Development

This technique is used in the project in order to test the chatbot from  user-side
The test was designed to test the following functionalities :
- the widget chatbot  are in the page and fully working when maximize and minimize
- the chatbot can answer user questions and look into the database to extract information
- in case the the answer is not in the database would ask the user for more clarification
- the chatbot should remember what is the user talking about so user can not repeat himself

## Getting Started

these tests were mainly coded to suit linux subsystem of windows, some steps for other platforms might be needed

### Prerequisites

Google chrome should be installed
also some other libraries :
```
sudo apt-get install xvfb
pip3 install behave
pip3 install selenium
pip3 install pyvirtualdisplay
```
also chrome webdriver should be installed from
http://chromedriver.chromium.org/downloads


### Running the tests
To run the tests

```
cd tests/bdd
behave
```
