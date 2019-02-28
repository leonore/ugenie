from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display


def update_virsion(driver):
    try :
       driver.get("http://34.73.120.65:5000//")
       return driver

    except:
        raise Exception("the driver dose not update")





def write_into_felid(driver,chatbot_message,text):
    elem = driver.find_element_by_xpath('//*[@id="myForm"]/div/form/input')
    elem.click()
    elem.clear()
    elem.send_keys(text)
    elem.submit()
    chatbot_message +=2
    driver.implicitly_wait(1)
    return driver,chatbot_message



def run_browser():
        driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
        chatbot_message = 1
        driver = update_virsion(driver)
        return driver,chatbot_message





def run_display():
    display = Display(visible=0, size=(800, 800))
    display.start()
    return display




def chatbot_xpath(driver,chatbot_message_num):
    try:
     chatbot_message =driver.find_element_by_xpath(('//*[@id="myForm"]/div/div[2]/div[{}]').format(chatbot_message_num))
     return chatbot_message
    except:
        raise Exception("chatbot message did not reach")




def open_chatbot(driver):
    driver.find_element_by_class_name("open-button").click();
    driver.implicitly_wait(1)
    return driver