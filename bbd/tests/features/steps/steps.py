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
        context.driver=open_chatbot(context.driver)
    except:
        raise Exception("chatbot cannot be opened ,either because it is already open or the open button is not working ")



@when(u'the user ask question about a specific subject')
def step_impl(context):
    try :
        context.driver,context.chatbot_message_num =write_into_felid(context.driver,context.chatbot_message_num,"what is biology")

    except:
        raise Exception("cannot send a message as a user ")




@then(u'the chatbot should search for the information in the database')
def step_impl(context):
    """code implemented to the query"""
    pass




@when(u'it dose not fine the information required')
def step_impl(context):
   """code implemented  for local version"""
   pass



@then(u'it should send that a message that  it dose not understand the question')
def step_impl(context):
    pass




@then(u'the chatbot should search the database It found the answer')
def step_impl(context):
    pass


@then(u'should send it back to the user')
def step_impl(context):
    context.chatbot_message = chatbot_xpath(context.driver,context.chatbot_message_num)
    print(context.chatbot_message.text)
    assert ('Ecology & Environmental Biology is a Life Sciences PGT course' == context.chatbot_message.text)





@given(u'the user in the specific page')
def step_impl(context):
    assert(flask_page(context))




@then(u'the widget expands and the chatbot starts a conversation')
def step_impl(context):
    assert (chatbot_open_assert(context) == False)
    try:
     context.chatbot_message = chatbot_xpath(context.driver,context.chatbot_message_num)
     print(context.chatbot_message.text)
    except:
        raise Exception("the chatbot message cannot be seen  ")

    assert(context.chatbot_message.text=="Hello, I'm GUVA, the Glasgow University Virtual Assistant. How can I help you?")







@Given ('the chatbot have already answerd a qusetion was asked by the user')
def setp_impl(context):
    context.execute_steps('''
    given chatbot is accessible
    When the user open the chat
    When  the user ask question about a specific subject
    Then the chatbot should search the database It found the answer
    Then should send it back to the user

        ''')
    assert (flask_page(context))





@when(u'the user asks for further')
def step_impl(context):
    context.driver, context.chatbot_message_num = write_into_felid(context.driver, context.chatbot_message_num,"how much is it ")

    context.user_message =  chatbot_xpath(context.driver,4)
    print(context.user_message.text)





@then(u'the chatbot should send the requierd information if it dose exist')
def step_impl(context):
    context.chatbot_message = chatbot_xpath(context.driver,context.chatbot_message_num)
    print(context.chatbot_message.text)
    assert ("Did you want the course: Ecology & Environmental Biology? (yes/no)" == context.chatbot_message.text)





@when(u'chatbot is accessible')
def step_impl(context):
    context.driver=open_chatbot(context.driver)
