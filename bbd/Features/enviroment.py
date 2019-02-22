from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display




def before_all(context):
    # -- SETUP-FIXTURE PART: And register as context-cleanup task.
    run_display(context)

    # -- CLEANUP-FIXTURE PART: browser.shutdown()



    # Fixture-cleanup is called when current context-layer is removed
def after_all(context):
    context.driver.close()




def before_step(context,step):

    expected_steps = ["the widget expands and the chatbot starts a conversation",'the chatbot should search the database',
                      "the user ask general question",'the chatbot should reasoned to the message']
    if step  in  expected_steps:
        wait_(context)


def before_scenario(context,scenario):
    # -- not sending a message scenarios
   ignored = []
   if scenario not in ignored:




def after_scenario(context,scenario):
    if scenario is not None :
        cotext.driver.close()

d