def valued(the_text,subject = None):

        return the_text==subject



def flask_page(context):
        return "Flask Chat" ==  context.driver.title




def only_widget_seen(context):
        if context.driver.find_element_by_class_name(('close').is_displayed()):
                return False
        if context.driver.find_element_by_class_name(('open-button').is_displayed()):
                return False
        else :
                return True




def chatbot_open_assert(context):
        if( context.driver.find_element_by_class_name('close').is_displayed()  or context.driver.find_element_by_class_name('open-button').is_displayed()==False):
                return False
        else :
                return True
def search_answer_databas(context):
      """  context.expected_answer ="""

