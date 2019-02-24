from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display

def this_try():
    display = Display(visible=0, size=(800, 800))
    display.start()
    driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
    driver.get("http://34.73.99.181:5000/")
    driver.find_element_by_class_name("open-button").click();
    driver.implicitly_wait(1)
    driver.find_element_by_xpath('//*[@id="myForm"]/div/form/input').click()
    driver.find_element_by_xpath('//*[@id="myForm"]/div/form/input').clear()
    driver.find_element_by_xpath('//*[@id="myForm"]/div/form/input').send_keys("tell me about biology")
    driver.find_element_by_xpath('//*[@id="myForm"]/div/form').submit()
    driver.implicitly_wait(1)

    text = driver.find_element_by_xpath('//*[@id="myForm"]/div/div[2]/div[3]').text
    print(text )
    driver.close()

    print(text)
if __name__ == '__main__':
    this_try()