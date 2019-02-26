from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
import psutil

def update_virsion(driver):
    try :
       driver.get("http://34.73.120.65:5000//")
       return driver

    except:
        raise Exception("the driver dose not update")





def write_into_felid(driver,chatbot_message,text):
    driver.find_element_by_xpath('//*[@id="myForm"]/div/form/input').clear()
    driver.find_element_by_xpath('//*[@id="myForm"]/div/form/input').send_keys(text)
    driver.find_element_by_xpath('//*[@id="myForm"]/div/form').submit()
    chatbot_message +=2
    driver.implicitly_wait(1)
    return driver,chatbot_message



def run_browser(driver,chatbot_message =0):

        driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
        chatbot_message = 1
        driver = update_virsion(driver)
        return driver,chatbot_message





def run_display(context):
    context.display = Display(visible=0, size=(800, 800))
    context.display.start()




def chatbot_message_xpath(context):
    try:
     context.chatbot_message =contect.driver.find_element_by_xpath(('//*[@id="myForm"]/div/div[2]/div[{}]').format(context.chatbot_message_num))
    except:
        raise Exception("chatbot message did not reach")

def open_chatbot(context):
    context.driver.find_element_by_class_name("open-button").click();
    context.driver.implicitly_wait(1)