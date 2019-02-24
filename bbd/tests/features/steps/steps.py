from behave import then ,when, given
from  COMMONTOLS.config.Config import *
from COMMONTOLS.functions.common_func import *
from COMMONTOLS.Assertions import *
@given("chatbot is accessible")

def one_chatbot(context):
      print(context.driver.title)

      assert(chatbot_open_assert(context) ==True)



@when(u'the user open the chat')
def step_impl(context):
    try:
        context.driver.find_element_by_class_name("open-button").click()
        context.driver.implicitly_wait(1)
    except:
        raise Exception("NOO ")

@when(u'the user ask question about a specific subject')
def step_impl(context):
    try :
        context.driver.find_element_by_xpath('//*[@id="myForm"]/div/form/input').click()
        context.driver.find_element_by_xpath('//*[@id="myForm"]/div/form/input').send_keys("what is biology")
        context.driver.find_element_by_xpath('//*[@id="myForm"]/div/form/input').submit()
        context.chatbot_message_num += 2
        context.driver.implicitly_wait(1)

    except:
        raise Exception("cannot change driver values")

@then(u'the chatbot should search for the information in the database')
def step_impl(context):
    """code implemented to the query"""
    pass

@when(u'it dose not fine the information required')
def step_impl(context):
   """code iomplemented  for local virision"""
   pass

@then(u'it should send that a message that  it dose not understand the question')
def step_impl(context):
    pass


@then(u'the chatbot should search the database It found the answer')
def step_impl(context):
    pass


@then(u'should send it back to the user')
def step_impl(context):
    context.chatbot_message = context.driver.find_element_by_xpath(
        ('//*[@id="myForm"]/div/div[2]/div[{}]').format(context.chatbot_message_num))
    print(context.chatbot_message.text)
    assert ('Ecology & Environmental Biology is a Life Sciences PGT course' == context.chatbot_message.text)

@given(u'the user in the specific page')
def step_impl(context):
    assert(flask_page(context))


@when(u'the wedge is seen')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the wedge is seen')


@when(u'the user clicks on the widget')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user clicks on the widget')


@then(u'the widget expands and the chatbot starts a conversation')
def step_impl(context):
    assert (chatbot_open_assert(context) == False)
    try:
     context.chatbot_message =context.driver.find_element_by_xpath(('//*[@id="myForm"]/div/div[2]/div[{}]').format(context.chatbot_message_num))
     print(context.chatbot_message.text)
    except:
        raise Exception("chatbot message did not reach")

    assert(context.chatbot_message.text=="Hello, I'm GUVA, the Glasgow University Virtual Assistant. How can I help you?")






"""will be fixed

@given(u'user asked a question about a subject')
def step_impl(context):
    try:
        context.driver.find_element_by_class_name("open-button").click()
        context.driver.implicitly_wait(1)


        context.driver.find_element_by_xpath('//*[@id="myForm"]/div/form/input').send_keys("what is biology")
        context.driver.find_element_by_xpath('//*[@id="myForm"]/div/form/input').submit()
        context.chatbot_message_num +=1
        context.driver.implicitly_wait(1)
        context.chatbot_message = context.driver.find_element_by_xpath(
            ('//*[@id="myForm"]/div/div[2]/div[{}]').format(context.chatbot_message_num))
        print(context.chatbot_message.text)
    except:
        raise Exception("cannot change driver values")


@when(u'chatbot respond with details')
def step_impl(context):
    context.chatbot_message = context.driver.find_element_by_xpath(
        ('//*[@id="myForm"]/div/div[2]/div[{}]').format(context.chatbot_message_num))
    print(context.chatbot_message.text)
    assert ('A History Of Germany is: The course will examine the history '
            'of the German speaking peoples from their first contacts with '
            'the Roman Empire, their invasions of southern Europe, and their'
            ' subsequent failure to create a united nation state until Bismarck '
            'at last reunited the component regions. We will then consider the'
            ' rise and fall of both the Second Reich and Third Reich, followed '
            'by the second reunification of Germany in 1990 and the status of '
            'Germany as the leading political and economic power in Europe.' == context.chatbot_message.text)


@when(u'the user asks for more details without mentioning the subject')
def step_impl(context):
    try:
        context.driver.find_element_by_xpath('//*[@id="myForm"]/div/form/input').click()
        context.driver.find_element_by_xpath('//*[@id="myForm"]/div/form/input').clean()
        context.driver.find_element_by_xpath('//*[@id="myForm"]/div/form/input').send_keys("how much is it")
        context.driver.find_element_by_xpath('//*[@id="myForm"]/div/form/input').submit()
        context.chatbot_message_num += 1
        context.driver.implicitly_wait(1)

    except:
        raise Exception("cannot change driver values")"""



@when(u'chatbot is accessible')
def step_impl(context):
    print(context.driver.title)

    assert (chatbot_open_assert(context) == True)


@then(u'the chatbot should be able to remember the subject')
def step_impl(context):
    context.chatbot_message = context.driver.find_element_by_xpath(
        ('//*[@id="myForm"]/div/div[2]/div[{}]').format(context.chatbot_message_num))
    print(context.chatbot_message.text)
    assert("Did you want the course: A History Of Germany? (yes/no)"== context.chatbot_message.text)