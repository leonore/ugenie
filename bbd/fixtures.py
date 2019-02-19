from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display



@fixture(name="chrome.run")
def browser_chrome(context):
    # -- SETUP-FIXTURE PART: And register as context-cleanup task.


    display = Display(visible=0, size=(800, 800))
    display.start()
    driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
    driver.get("http://34.73.99.181:5000/")
    context.driver = driver
    context.add_cleanup(browser.close())
    return driver
    # -- CLEANUP-FIXTURE PART: browser.shutdown()
    # Fixture-cleanup is called when current context-layer is removed