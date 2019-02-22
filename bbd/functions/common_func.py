from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
import psutil

def update_virsion(context):
    if driver.expexted_page  in context:
       return  driver.get("http://34.73.99.181:5000/")
    else:
        if   "someProgram" in (p.name() for p in psutil.process_iter())
        else:






def write_into_felid(context,text):
    driver.find_element_by_xpath('//*[@id="myForm"]/div/form/input').clear()
    context.driver.find_element_by_xpath('//*[@id="myForm"]/div/form/input').send_keys(text)
    context.driver.find_element_by_xpath('//*[@id="myForm"]/div/form').submit()
    context.chatbot_message +=2
    context.driver.implicitly_wait(1)



def run_browser(context):
    try :
        driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
        context.driver = driver
        context.chatbot_message_num = 1

    catch :
        raise DriverOpenExeption("cannot run the browser")



def run_display(context):
    context.display = Display(visible=0, size=(800, 800))
    context.display.start()




def chatbot_message_xpath(context):
    try:
     context.chatbot_message =contect.driver.find_element_by_xpath(('//*[@id="myForm"]/div/div[2]/div[{}]').format(context.chatbot_message_num))
    catch:
        raise PathDoseNotExistException("chatbot message did not reach")

def open_chatbot(context):
    driver.find_element_by_class_name("open-button").click();
    context.driver.implicitly_wait(1)