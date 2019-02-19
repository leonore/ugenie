from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display


display = Display(visible=0, size=(800, 800))
display.start()
"""this path only works with linuxs....other user have to fallow other path for their crhome"""
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver.get("http://34.73.99.181:5000/")

    # -- CLEANUP-FIXTURE PART: browser.shutdown()
    # Fixture-cleanup is called when current context-layer is removed

@Given("the user in the specific page")
def in_the_chat_page(context):
    context.text_1 =''
    print(driver.title)
    assert ("Flask Chat" ==  driver.title )


@When("the wedge is seen")
def widget_seen(context):
    driver.get("http://34.73.99.181:5000/")
    assert (driver.find_element_by_class_name('close').is_displayed() == False)
    assert(driver.find_element_by_class_name('open-button').is_displayed())




@When("the user clicks on the widget")
def in_widget_clicked(context):
    driver.find_element_by_class_name("open-button").click();
    assert (driver.find_element_by_class_name('close').is_displayed())
    assert (driver.find_element_by_class_name('open-button').is_displayed()==False)
    driver.implicitly_wait(1)


@Then("the widget expands and the chatbot starts a conversation")
def chatbot_accessable(context):
    text = driver.find_element_by_xpath('//*[@id="myForm"]/div/div[2]/div[1]').text
    print(text)
    assert(text =="Hello, I'm GUVA, the Glasgow University Virtual Assistant. How can I help you?")
    driver.close()

@given(u'the user ask general question')
def step_impl(context):
    driver.get("http://34.73.99.181:5000/")
    driver.find_element_by_class_name("open-button").click();
    driver.implicitly_wait(1)
    driver.find_element_by_xpath('//*[@id="myForm"]/div/form/input').click()
    driver.find_element_by_xpath('//*[@id="myForm"]/div/form/input').clear()
    driver.find_element_by_xpath('//*[@id="myForm"]/div/form/input').send_keys("tell me about biology")
    driver.find_element_by_xpath('//*[@id="myForm"]/div/form').submit()
    driver.implicitly_wait(1)

    context.text_1 = driver.find_element_by_xpath('//*[@id="myForm"]/div/div[2]/div[3]').text




@then(u'the chatbot should search the database')
def step_impl(context):
    """code from query db while working on a local version"""
    pass


@when(u'when the answer is not found')
def step_impl(context):
    """code from query db while working on a local version"""
    assert(context.text_1 == "Ecology & Environmental Biology is a Life Sciences PGT course")


@then(u'chatbot send a correction back to the user')
def step_impl(context):
    assert(context.text_1 == "Ecology & Environmental Biology is a Life Sciences PGT course")


@given(u'the chatbot started a conversation')
def step_impl(context):
    driver.get("http://34.73.99.181:5000/")
    driver.find_element_by_class_name("open-button").click();
    driver.implicitly_wait(1)
    driver.find_element_by_xpath('//*[@id="myForm"]/div/form/input').click()
    driver.find_element_by_xpath('//*[@id="myForm"]/div/form/input').clear()
    driver.find_element_by_xpath('//*[@id="myForm"]/div/form/input').send_keys("tell me about biology")
    driver.find_element_by_xpath('//*[@id="myForm"]/div/form').submit()
    driver.implicitly_wait(1)

    context.text_1 = driver.find_element_by_xpath('//*[@id="myForm"]/div/div[2]/div[3]').text


@when(u'the user ask question about a specific subject')
def step_impl(context):
    driver.find_element_by_xpath('//*[@id="myForm"]/div/form/input').send_keys("tell me about nnm")
    driver.find_element_by_xpath('//*[@id="myForm"]/div/form').submit()
    driver.implicitly_wait(1)

    context.text_1 = driver.find_element_by_xpath('//*[@id="myForm"]/div/div[2]/div[3]').text


@then(u'the chatbot should search for the information in the database')
def step_impl(context):
    """code from query db while working on a local version"""
    pass

@when(u'it dose not fine the information required')
def step_impl(context):
    """code from query db while working on a local version"""
    pass

@then(u'it should send that subject dose not exist')
def step_impl(context):
    assert(context.text_1 == "Sorry, I didn't understand, could you rephrase that?")


@given(u'the chatbot is open')
def step_impl(context):
    driver.get("http://34.73.99.181:5000/")
    driver.find_element_by_class_name("open-button").click();
    driver.implicitly_wait(1)

@given(u'the text field is empty')
def step_impl(context):
    pass


@when(u'the user  type something')
def step_impl(context):
    driver.find_element_by_xpath('//*[@id="myForm"]/div/form/input').send_keys("thfxh nnm")
    driver.find_element_by_xpath('//*[@id="myForm"]/div/form').submit()

@when(u'click on  enter')
def step_impl(context):
    driver.find_element_by_xpath('//*[@id="myForm"]/div/form').submit()


@then(u'the chatbot should reasoned to the message')
def step_impl(context):
    driver.implicitly_wait(1)

    context.text_1 = driver.find_element_by_xpath('//*[@id="myForm"]/div/div[2]/div[3]').text


@given(u'I asked a question about a subject')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I asked a question about a subject')


@given(u'chatbot respond with details')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given chatbot respond with details')


@when(u'the user asks for more details without mentioning the subject')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user asks for more details without mentioning the subject')


@then(u'the chatbot should be able to remember the subject')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the chatbot should be able to remember the subject')


@when(u'it fine the information required')
def step_impl(context):
    raise NotImplementedError(u'STEP: When it fine the information required')


@then(u'it should send it to the user')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then it should send it to the user')


@given(u'chatbot is accessible')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given chatbot is accessible')


@when(u'the user ask general question')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user ask general question')


@when(u'It found the answer')
def step_impl(context):
    raise NotImplementedError(u'STEP: When It found the answer')


@then(u'should send it back to the user')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then should send it back to the user')