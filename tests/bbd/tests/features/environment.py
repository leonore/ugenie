from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
from  COMMONTOLS.config.Config import *
from COMMONTOLS.functions.common_func import *



def before_all(context):
    # -- SETUP-FIXTURE PART: And register as context-cleanup task.
    context.display =run_display()
    context.driver = run_browser()
    context.chatbot_message_num = 1
    context.user_message_num =0


    # -- CLEANUP-FIXTURE PART: browser.shutdown()

    pass

    # Fixture-cleanup is called when current context-layer is removed
def after_all(context):
    context.driver.close()
    pass



def before_step(context,step):


    pass


def before_scenario(context,scenario):

    # -- not sending a message scenarios

    context.driver.get("http://34.73.120.65:5000//")



def after_scenario(context,scenario):

    pass

