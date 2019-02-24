from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
from  COMMONTOLS.config.Config import *
from COMMONTOLS.functions.common_func import *



def before_all(context):
    # -- SETUP-FIXTURE PART: And register as context-cleanup task.
    context.chatbot_message =0
    context.display = Display(visible=0, size=(800, 800))
    context.display.start()
    context.driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
    context.driver.get("http://34.73.120.65:5000/")
    context.chatbot_message_num = 1
    context.driver.implicitly_wait(1)

    # -- CLEANUP-FIXTURE PART: browser.shutdown()

    pass

    # Fixture-cleanup is called when current context-layer is removed
def after_all(context):
    context.driver.close()
    pass



def before_step(context,step):

    """expected_steps = ["the widget expands and the chatbot starts a conversation",'the chatbot should search the database',
                      "the user ask general question",'the chatbot should reasoned to the message']
    if step  in  expected_steps:
        wait_(context)"""
    pass


def before_scenario(context,scenario):

    # -- not sending a message scenarios

    context.driver.get("http://34.73.120.65:5000//")
    ignored = []



def after_scenario(context,scenario):

    pass

